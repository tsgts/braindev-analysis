import numpy as np
import keras
from keras.models import Model
from keras.layers import Input, Dense, Dropout
from keras.optimizers import SGD
from keras.callbacks import Callback
from keras.callbacks import TensorBoard
import tensorflow as tf
import matplotlib.pyplot as plt
import json
tf.python.control_flow_ops = tf
with tf.device('/cpu:0'):
	target = np.loadtxt("allen_data/dev_mouse/mouse_numpy_array.txt")

	#fit target expression values to range (0,1)
	target_max = np.amax(target)
	target_min = np.amin(target)
	print(np.amax(target))
	print(np.amin(target))
	target_range = target_max - target_min
	target = np.add(target,-1*target_min)
	target = np.multiply(target,1/target_range)
	print(np.amax(target))
	print(np.amin(target))

	input_img = Input(shape=(77,))
	encoded = Dense(128, activation='relu')(input_img)
	encoded = Dropout(0.25)(encoded)
	encoded = Dense(64, activation='relu')(encoded)
	encoded = Dropout(0.25)(encoded)
	encoded = Dense(32, activation='relu')(encoded)
	encoded = Dropout(0.25)(encoded)

	decoded = Dense(64, activation='relu')(encoded)
	decoded = Dropout(0.25)(decoded)
	decoded = Dense(128, activation='relu')(decoded)
	decoded = Dropout(0.25)(decoded)
	decoded = Dense(77, activation='sigmoid')(decoded)

	model = Model(input_img, decoded)
	model.summary()

	model.compile(loss='poisson',
	              optimizer="adam",
	              metrics=['accuracy'])

	model.fit(target, target, 
			  shuffle=True, 
			  nb_epoch=512, 
			  verbose=1,
			  callbacks=[TensorBoard(log_dir='tensorboard/mouse/autoencoder')]
			  )

	model.save("mouse_no_conv.h5")

	weights = []
	for layer in model.layers:
		g=layer.get_config()
		h=layer.get_weights()
		print (g)
		#print (h)
		weights.append(np.asarray(h).tolist())

	print(weights)
	#json.dump(weights.tolist(), open("allen_data/dev_mouse/weights.txt",'w'), indent=4)

	prediction = model.predict(target)

	encoder = Model(input=input_img, output=encoded)
	encoded_imgs = encoder.predict(target)
	print(encoded_imgs.shape)
	np.savetxt('allen_data/dev_mouse/encode.txt', encoded_imgs)

	plt.figure(figsize=(20, 4))
	n = 16
	for i in range(n):
		#original
	    ax = plt.subplot(2, n, i + 1)
	    plt.imshow(target[i].reshape(7, 11), interpolation='none')
	    plt.gray()
	    ax.get_xaxis().set_visible(False)
	    ax.get_yaxis().set_visible(False)

	    #predicted
	    ax = plt.subplot(2, n, i + 1 + n)
	    plt.imshow(prediction[i].reshape(7, 11), interpolation='none')
	    plt.gray()
	    ax.get_xaxis().set_visible(False)
	    ax.get_yaxis().set_visible(False)
	plt.show()
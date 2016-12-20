import numpy as np
import keras
from keras.models import Model
from keras.layers import Input, Dense, Dropout
from keras.optimizers import SGD
from keras.callbacks import Callback
from keras.callbacks import TensorBoard
from keras.regularizers import l2, activity_l2
import tensorflow as tf
import matplotlib.pyplot as plt
import json
from mpl_toolkits.mplot3d import Axes3D

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
	encoded = Dense(64, activation='tanh')(input_img)
	encoded = Dense(32, activation='tanh')(encoded)
	encoded = Dense(16, activation='tanh')(encoded)

	encoded = Dense(4, activation='tanh')(encoded)

	decoded = Dense(16, activation='tanh')(encoded)
	decoded = Dense(32, activation='tanh')(decoded)
	decoded = Dense(64, activation='tanh')(decoded)
	decoded = Dense(77, activation='sigmoid')(decoded)

	model = Model(input_img, decoded)
	model.summary()

	model.compile(loss='poisson',
	              optimizer="adam",
	              metrics=['accuracy'])

	model.fit(target, target, 
			  shuffle=True, 
			  nb_epoch=1000, 
			  verbose=2,
			  callbacks=[TensorBoard(log_dir='tensorboard/mouse/autoencoder')]
			  )

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
	    ax.get_xaxis().set_visible(False)
	    ax.get_yaxis().set_visible(False)

	    #predicted
	    ax = plt.subplot(2, n, i + 1 + n)
	    plt.imshow(prediction[i].reshape(7, 11), interpolation='none')
	    ax.get_xaxis().set_visible(False)
	    ax.get_yaxis().set_visible(False)
	plt.show()
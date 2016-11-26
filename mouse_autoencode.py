import numpy as np
import keras
from keras.models import Sequential
from keras.layers.core import Activation, Dense
from keras.optimizers import SGD
from keras.callbacks import Callback
from keras.callbacks import TensorBoard
import tensorflow as tf
import matplotlib.pyplot as plt

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

	model = Sequential([
	        Dense(32, input_dim=77, init="normal"),
	        Activation('relu'),
	        Dense(77, init="normal"),
	        Activation('sigmoid'),
	    ])

	model.compile(loss='mean_squared_error',
	              optimizer="adam",
	              metrics=['accuracy'])

	model.fit(target, target, shuffle=True, nb_epoch=512, verbose=1,callbacks=[TensorBoard(log_dir='tensorboard/mouse/autoencoder')])

	prediction = model.predict(target)

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
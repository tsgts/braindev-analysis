import numpy as np
import keras
from keras.models import Sequential
from keras.layers.core import Activation, Dense
from keras.optimizers import SGD
from keras.callbacks import Callback
import tensorflow as tf

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
	        Dense(64, input_dim=77, init="normal"),
	        Activation('relu'),
	        Dense(64, init="normal"),
	        Activation('relu'),
	        Dense(77, init="normal"),
	        Activation('sigmoid'),
	    ])

	model.compile(loss='mean_squared_error',
	              optimizer="adam",
	              metrics=['accuracy'])

	model.fit(target, target, shuffle=True, nb_epoch=10, verbose=1)

	random_indices = np.random.randint(2011, size=16)
	encode_test = target[random_indices,:]
	print(encode_test.shape)
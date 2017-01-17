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
	target = np.loadtxt("allen_data/dev_human/human_numpy_array.txt")

	#fit target expression values to range (0,1)
	target_max = np.amax(target)
	target_min = np.amin(target)
	print(np.amax(target))
	print(np.amin(target))
	target_range = target_max - target_min
	target = np.add(target,-1*target_min)
	target = np.add(np.multiply(target,1/target_range)*2,-1)
	print(np.amax(target))
	print(np.amin(target))

	input_img = Input(shape=(150,))
	encoded = Dense(64, activation='tanh',init='glorot_normal')(input_img)
	# encoded = Dense(32, activation='sigmoid')(encoded)
	# encoded = Dense(16, activation='sigmoid')(encoded)
	# encoded = Dense(8, activation='sigmoid')(encoded)

	# encoded = Dense(8, activation='sigmoid')(encoded)

	# decoded = Dense(8, activation='sigmoid')(encoded)
	# decoded = Dense(16, activation='sigmoid')(decoded)
	# decoded = Dense(32, activation='sigmoid')(decoded)
	# decoded = Dense(64, activation='sigmoid')(decoded)
	decoded = Dense(150, activation='tanh')(encoded)

	model = Model(input_img, decoded)
	model.summary()

	model.compile(loss='mean_squared_error',
	              optimizer="adam",
	              metrics=['accuracy'])

	model.fit(target, target, 
			  shuffle=True, 
			  nb_epoch=100, 
			  verbose=2
			  )

	prediction = model.predict(target)

	plt.figure(figsize=(20, 4))
	n = 32
	for i in range(n):
		#original
	    ax = plt.subplot(2, n, i + 1)
	    plt.imshow(target[i].reshape(15, 10), interpolation='none')
	    ax.get_xaxis().set_visible(False)
	    ax.get_yaxis().set_visible(False)

	    #predicted
	    ax = plt.subplot(2, n, i + 1 + n)
	    plt.imshow(prediction[i].reshape(15, 10), interpolation='none')
	    ax.get_xaxis().set_visible(False)
	    ax.get_yaxis().set_visible(False)
	plt.show()
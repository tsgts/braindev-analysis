import numpy as np
import keras
from keras.layers import Input, Activation, Dense, Convolution2D, MaxPooling2D, UpSampling2D, Reshape
from keras.models import Model
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
	target = target.reshape(2012,1,7,11)
	print(np.amax(target))
	print(np.amin(target))


	input_img = Input(shape=(1, 7, 11))

	x = Convolution2D(16, 3, 3, activation='relu', border_mode='same')(input_img)
	x = MaxPooling2D((2, 2), border_mode='same')(x)
	x = Convolution2D(8, 3, 3, activation='relu', border_mode='same')(x)
	x = MaxPooling2D((2, 2))(x)

	x = Convolution2D(8, 3, 3, activation='relu', border_mode='same')(x)
	x = UpSampling2D((2, 2))(x)
	x = Convolution2D(16, 3, 3, activation='relu', border_mode='same')(x)
	x = UpSampling2D((2, 2))(x)

	x = Convolution2D(1, 3, 3, activation='sigmoid', border_mode='same')(x)
	
	x = Reshape((96,))(x)
	x = Dense(77)(x)
	x = Reshape((1, 7, 11))(x)
	decoded = x

	autoencoder = Model(input_img, decoded)
	autoencoder.compile(optimizer='adam', loss='mean_squared_error',metrics=['accuracy'])

	autoencoder.fit(target, target, 
					shuffle=True, 
					nb_epoch=512, 
					verbose=1,
                	callbacks=[TensorBoard(log_dir='tensorboard/mouse/autoencoder')])

	prediction = autoencoder.predict(target)

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
# with tf.device('/cpu:0'):
# 	from keras.layers import Input, Dense, Convolution2D, MaxPooling2D, UpSampling2D
# 	from keras.models import Model

# 	input_img = Input(shape=(1, 28, 28))

# 	x = Convolution2D(16, 3, 3, activation='relu', border_mode='same')(input_img)
# 	x = MaxPooling2D((2, 2), border_mode='same')(x)
# 	x = Convolution2D(8, 3, 3, activation='relu', border_mode='same')(x)
# 	encoded = MaxPooling2D((2, 2), border_mode='same')(x)

# 	x = Convolution2D(8, 3, 3, activation='relu', border_mode='same')(encoded)
# 	x = UpSampling2D((2, 2))(x)
# 	x = Convolution2D(8, 3, 3, activation='relu', border_mode='same')(x)
# 	x = UpSampling2D((2, 2))(x)
# 	decoded = Convolution2D(1, 3, 3, activation='sigmoid', border_mode='same')(x)

# 	autoencoder = Model(input_img, decoded)
# 	autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

# 	from keras.datasets import mnist
# 	import numpy as np

# 	(x_train, _), (x_test, _) = mnist.load_data()

# 	x_train = x_train.astype('float32') / 255.
# 	x_test = x_test.astype('float32') / 255.
# 	x_train = np.reshape(x_train, (len(x_train), 1, 28, 28))
# 	x_test = np.reshape(x_test, (len(x_test), 1, 28, 28))

# 	autoencoder.fit(x_train, x_train,
# 	                nb_epoch=50,
# 	                batch_size=128,
# 	                shuffle=True,
# 	                validation_data=(x_test, x_test))
'''This script demonstrates how to build a variational autoencoder with Keras.

Reference: "Auto-Encoding Variational Bayes" https://arxiv.org/abs/1312.6114
'''
import numpy as np
import math
import keras
import matplotlib.pyplot as plt
from scipy.stats import norm

from keras.layers import Input, Dense, Lambda
from keras.models import Model
from keras import backend as K
from keras import objectives
from keras.datasets import mnist
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

	batch_size = 2012
	original_dim = 77
	latent_dim = 2
	intermediate_dim = 32
	nb_epoch = 100000
	epsilon_std = 1

	x = Input(batch_shape=(batch_size, original_dim))
	h = Dense(intermediate_dim, activation='relu')(x)
	z_mean = Dense(latent_dim)(h)
	z_log_var = Dense(latent_dim)(h)


	def sampling(args):
	    z_mean, z_log_var = args
	    epsilon = K.random_normal(shape=(batch_size, latent_dim), mean=0.,
	                              std=epsilon_std)
	    return z_mean + K.exp(z_log_var / 2) * epsilon

	# note that "output_shape" isn't necessary with the TensorFlow backend
	z = Lambda(sampling, output_shape=(latent_dim,))([z_mean, z_log_var])


	# we instantiate these layers separately so as to reuse them later
	decoder_h = Dense(intermediate_dim, activation='relu')
	decoder_mean = Dense(original_dim, activation='sigmoid')
	h_decoded = decoder_h(z)
	x_decoded_mean = decoder_mean(h_decoded)


	def vae_loss(x, x_decoded_mean):
	    xent_loss = original_dim * objectives.binary_crossentropy(x, x_decoded_mean)
	    kl_loss = - 0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)

	    return xent_loss #+ kl_loss

	vae = Model(x, x_decoded_mean)
	vae.summary()

	vae.compile(optimizer="adam", loss=vae_loss, metrics=['accuracy'])

	# train the VAE on MNIST digits
	(x_train, y_train), (x_test, y_test) = (target,target), (target,target)
	#x_test,y_test = x_train,y_train

	x_train = x_train.astype('float32') / 255.
	x_test = x_test.astype('float32') / 255.
	x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
	x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

	vae.fit(x_train, x_train,
	        shuffle=True,
	        nb_epoch=nb_epoch,
	        batch_size=batch_size)

	# build a model to project inputs on the latent space
	encoder = Model(x, z_mean)

	# display a 2D plot of the digit classes in the latent space
	x_test_encoded = encoder.predict(x_test, batch_size=batch_size)
	plt.figure(figsize=(6, 6))
	plt.scatter(x_test_encoded[:, 0], x_test_encoded[:, 1])
	#plt.colorbar()
	plt.show()

	# build a digit generator that can sample from the learned distribution
	decoder_input = Input(shape=(latent_dim,))
	_h_decoded = decoder_h(decoder_input)
	_x_decoded_mean = decoder_mean(_h_decoded)
	generator = Model(decoder_input, _x_decoded_mean)

	# display a 2D manifold of the digits
	n = 25  # figure with 15x15 digits
	figure = np.zeros((7 * n, 11 * n))
	# linearly spaced coordinates on the unit square were transformed through the inverse CDF (ppf) of the Gaussian
	# to produce values of the latent variables z, since the prior of the latent space is Gaussian
	grid_x = norm.ppf(np.linspace(0.05, 0.95, n))
	grid_y = norm.ppf(np.linspace(0.05, 0.95, n))

	for i, yi in enumerate(grid_x):
	    for j, xi in enumerate(grid_y):
	        z_sample = np.array([[xi, yi]])
	        x_decoded = generator.predict(z_sample)
	        digit = x_decoded[0].reshape(7, 11)
	        figure[i * 7: (i + 1) * 7,
	               j * 11: (j + 1) * 11] = digit

	plt.figure(figsize=(10, 10))
	plt.imshow(figure, interpolation='none')
	plt.show()

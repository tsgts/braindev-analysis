import numpy as np
import keras
from keras.models import Sequential
from keras.layers.core import Activation, Dense
from keras.optimizers import SGD
from keras.callbacks import Callback
from keras.callbacks import TensorBoard
from keras.models import load_model
import tensorflow as tf
import matplotlib.pyplot as plt

with tf.device('/cpu:0'):
	target = np.loadtxt("allen_data/dev_mouse/mouse_numpy_array.txt")

	target_max = np.amax(target)
	target_min = np.amin(target)
	print(np.amax(target))
	print(np.amin(target))
	target_range = target_max - target_min
	target = np.add(target,-1*target_min)
	target = np.multiply(target,1/target_range)
	print(np.amax(target))
	print(np.amin(target))

	model = load_model('mouse_no_conv.h5')
	model.pop()

	print(model.layers)
	prediction = model.predict(target)
	print(prediction.shape)
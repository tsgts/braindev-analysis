import numpy as np
import keras
from keras.models import Sequential
from keras.layers.core import Activation, Dense
from keras.optimizers import SGD
from keras.callbacks import Callback
import tensorflow as tf

target = np.loadtxt("allen_data/dev_mouse/mouse_numpy_array.txt")

#fit target expression values to range (0,1)
target_max = np.amax(target)
target_min = np.amin(target)
target_range = target_max - target_min
target = np.add(target,-1*target_min)
target = np.multiply(target,1/target_range)
print(np.amax(target))
print(np.amin(target))

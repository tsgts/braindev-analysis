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
from keras.datasets import mnist
(x_train, _), (x_test, _) = mnist.load_data()

tf.python.control_flow_ops = tf
with tf.device('/cpu:0'):
    target = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.
    target = target.reshape((len(x_train), np.prod(x_train.shape[1:])))
    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

    input_img = Input(shape=(784,))
    # encoded = Dense(16, activation='tanh')(encoded)

    encoded = Dense(4, activation='relu')(input_img)

    # decoded = Dense(16, activation='tanh')(encoded)
    # decoded = Dense(32, activation='tanh')(decoded)
    decoded = Dense(784, activation='sigmoid')(encoded)

    model = Model(input_img, decoded)
    model.summary()

    model.compile(loss='binary_crossentropy',
                  optimizer="adam",
                  metrics=['accuracy'])

    model.fit(target, target, 
              shuffle=True, 
              nb_epoch=25, 
              batch_size=256,
              verbose=1,
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
        plt.imshow(target[i].reshape(28, 28), interpolation='none')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        #predicted
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(prediction[i].reshape(28, 28), interpolation='none')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()
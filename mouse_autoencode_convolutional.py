import numpy as np
import keras
from keras.layers import Input, Activation, Dense, Convolution2D, MaxPooling2D, UpSampling2D, Reshape, Dropout, Flatten
from keras.models import Model
from keras.callbacks import TensorBoard
import tensorflow as tf
import matplotlib.pyplot as plt

config = tf.ConfigProto()
config.gpu_options.allow_growth=True
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
    encoded = Dense(64, activation='relu')(input_img)
    encoded = Reshape((1, 8, 8))(encoded)
    encoded = Convolution2D(8, 3, 3, activation='relu', border_mode='same')(encoded)
    encoded = MaxPooling2D((2, 2), border_mode='same')(encoded)
    encoded = Convolution2D(4, 3, 3, activation='relu', border_mode='same')(encoded)
    encoded = MaxPooling2D((2, 2))(encoded)
    encoded = Convolution2D(1, 2, 2, activation='sigmoid', border_mode='same')(encoded)
    # decoded = Convolution2D(16, 3, 3, activation='relu', border_mode='same')(encoded)
    # decoded = UpSampling2D((2, 2))(decoded)
    # decoded = Convolution2D(32, 3, 3, activation='relu', border_mode='same')(decoded)
    # decoded = UpSampling2D((2, 2))(decoded)

    # decoded = Convolution2D(1, 3, 3, activation='sigmoid', border_mode='same')(decoded)

    encoded = Flatten()(encoded)

    decoded = Dense(77)(encoded)

    model = Model(input_img, decoded)
    model.summary()

    model.compile(optimizer='adam', loss='mean_squared_error',metrics=['accuracy'])

    model.fit(target, target, 
    				shuffle=True, 
    				nb_epoch=4000, 
    				verbose=2,
                	callbacks=[TensorBoard(log_dir='tensorboard/mouse/autoencoder')])

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

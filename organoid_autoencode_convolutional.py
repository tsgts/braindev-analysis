import numpy as np
import keras
from keras.layers import Input, Activation, Dense, Convolution2D, MaxPooling2D, UpSampling2D, Reshape, Dropout, Flatten
from keras.models import Model
from keras.callbacks import TensorBoard
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.optimizers import RMSprop, Adam, Adamax

config = tf.ConfigProto()
config.gpu_options.allow_growth=True
with tf.device('/cpu:0'):
    target = np.loadtxt("allen_data/organoid/organoid_numpy_array.txt")
    print(target.shape)
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

    input_img = Input(shape=(224,))
    encoded = Dense(128, activation='relu',init='glorot_normal')(input_img)
    encoded = Reshape((1, 8, 16))(encoded)
    encoded = Convolution2D(16, 3, 3, activation='relu', border_mode='same',init='glorot_normal')(encoded)
    encoded = MaxPooling2D((2, 2))(encoded)
    encoded = Convolution2D(8, 3, 3, activation='relu', border_mode='same',init='glorot_normal')(encoded)
    encoded = MaxPooling2D((2, 2))(encoded)
    encoded = Convolution2D(4, 3, 3, activation='relu', border_mode='same',init='glorot_normal')(encoded)

    encoded = Flatten()(encoded)
    encoded = Dense(4, activation='relu',init='glorot_normal')(encoded)

    decoded = Dense(32, activation='relu',init='glorot_normal')(encoded)
    decoded = Reshape((4, 2, 4))(decoded)

    decoded = Convolution2D(4, 3, 3, activation='relu', border_mode='same',init='glorot_normal')(decoded)
    decoded = UpSampling2D((2, 2))(decoded)
    decoded = Convolution2D(8, 3, 3, activation='relu', border_mode='same',init='glorot_normal')(decoded)
    decoded = UpSampling2D((2, 2))(decoded)
    decoded = Convolution2D(16, 3, 3, activation='relu', border_mode='same',init='glorot_normal')(decoded)
    decoded = Flatten()(decoded)
    decoded = Dense(224, activation='tanh',init='glorot_normal')(decoded)

    model = Model(input_img, decoded)
    model.summary()

    model.compile(optimizer="rmsprop", loss='mean_squared_error',metrics=['accuracy'])

    class current_prediction(keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs={}):
            if epoch % 50 == 0:
                encoder = Model(input=input_img, output=encoded)
                encoded_imgs = encoder.predict(target)
                np.savetxt('allen_data/organoid/autoencoder/encode_' + str(epoch) + '.txt', encoded_imgs)
            else:
                pass
            # prediction = model.predict(target[:8])
            # plt.figure(figsize=(20, 4))
            # n = 8
            # for i in range(n):
            #     #original
            #     ax = plt.subplot(2, n, i + 1)
            #     plt.imshow(target[i].reshape(7, 11), interpolation='none')
            #     ax.get_xaxis().set_visible(False)
            #     ax.get_yaxis().set_visible(False)

            #     #predicted
            #     ax = plt.subplot(2, n, i + 1 + n)
            #     plt.imshow(prediction[i].reshape(7, 11), interpolation='none')
            #     ax.get_xaxis().set_visible(False)
            #     ax.get_yaxis().set_visible(False)
            # plt.savefig("figures/dev_mouse/iterations/convolutional_"+str(epoch)+".png", dpi = 25)
            # plt.close()

    prediction = current_prediction()

    model.fit(target, target, 
    				shuffle=True, 
    				nb_epoch=20000, 
    				verbose=2,
                	callbacks=[prediction,TensorBoard(log_dir='tensorboard/organoid/autoencoder')])

    prediction = model.predict(target)

    encoder = Model(input=input_img, output=encoded)
    encoded_imgs = encoder.predict(target)
    print(encoded_imgs.shape)
    np.savetxt('allen_data/organoid/autoencoder/encode.txt', encoded_imgs)

    plt.figure(figsize=(20, 4))
    n = 16
    for i in range(n):
    	#original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(target[i].reshape(7, 32), interpolation='none')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        #predicted
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(prediction[i].reshape(7, 32), interpolation='none')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()
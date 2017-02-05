import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import json
from matplotlib import pyplot as plt
# import pyqtgraph as pg
# from pyqtgraph.Qt import QtGui, QtCore
   
# data = data=np.loadtxt('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt')

#===========RAW DATA=================

data=np.loadtxt("allen_data/dev_mouse/mouse_numpy_array.txt")
data=np.reshape(data,(1912,77))

#==============AUTOENCODER============

#data = np.loadtxt('allen_data/dev_mouse/encode.txt')

pca = PCA(n_components=8)
transformed = pca.fit_transform(data) 
print(transformed.shape)
print(pca.explained_variance_ratio_) 
print(sum(pca.explained_variance_ratio_))
transformed = np.transpose(transformed)

np.savetxt('allen_data/dev_mouse/pca.txt', transformed)


# fig = plt.figure()
# plt.scatter(transformed[0], transformed[1], c='r', marker='o')
# plt.show()

# app = QtGui.QApplication([])
# pg.setConfigOption('background', 'w')
# pg.plot(transformed[0], transformed[1], pen=None, symbol="o")

# app.exec_()
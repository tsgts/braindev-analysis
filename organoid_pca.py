import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import json
from matplotlib import pyplot as plt
# import pyqtgraph as pg
# from pyqtgraph.Qt import QtGui, QtCore

# with open('allen_data/dev_human/mouse_corr_spearman_matrix.txt') as data_file:    
#     data = json.load(data_file)

#===========RAW DATA=================

data=np.loadtxt("allen_data/organoid/organoid_numpy_array.txt")
data=np.reshape(data,(1675,224))

#==============AUTOENCODER============

#data = np.loadtxt('allen_data/dev_human/encode.txt')

pca = PCA(n_components=4)
transformed = pca.fit_transform(data) 
print(transformed.shape)
print(pca.explained_variance_ratio_) 
print(sum(pca.explained_variance_ratio_))
transformed = np.transpose(transformed)

np.savetxt('allen_data/organoid/pca.txt', transformed)


# fig = plt.figure()
# plt.scatter(transformed[0], transformed[1], c='r', marker='o')
# plt.show()

# app = QtGui.QApplication([])
# pg.setConfigOption('background', 'w')
# pg.plot(transformed[0], transformed[1], pen=None, symbol="o")

# app.exec_()
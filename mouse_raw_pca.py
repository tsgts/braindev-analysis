import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import json
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# import pyqtgraph as pg
# from pyqtgraph.Qt import QtGui, QtCore

# with open('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt') as data_file:    
#     data = json.load(data_file)

#===========RAW DATA=================

with open('allen_data/dev_mouse/raw_dictionary_no_days.txt') as data_file:    
    data = json.load(data_file)

for key, value in data.items():
	data[key] = [item for sublist in value for item in sublist]

data = list(data.values())
data = np.array(data)

#==============AUTOENCODER============

#data = np.loadtxt('allen_data/dev_mouse/encode.txt')

pca = PCA(n_components=4)
transformed = pca.fit_transform(data) 
print(transformed.shape)
print(pca.explained_variance_ratio_) 

np.savetxt('allen_data/dev_mouse/pca.txt', transformed)

transformed = np.transpose(transformed)

fig = plt.figure()
plt.scatter(transformed[0], transformed[1], c='r', marker='o')
plt.show()

# app = QtGui.QApplication([])
# pg.setConfigOption('background', 'w')
# pg.plot(transformed[0], transformed[1], pen=None, symbol="o")

# app.exec_()
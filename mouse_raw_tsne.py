import numpy as np
from sklearn.manifold import TSNE
import pandas as pd
import json
from matplotlib import pyplot as plt
# import pyqtgraph as pg
# from pyqtgraph.Qt import QtGui, QtCore

#===========CORRELATIONS===============

# with open('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt') as data_file:    
#     data = json.load(data_file)

#===========RAW DATA=================

# with open('allen_data/dev_mouse/raw_dictionary_no_days.txt') as data_file:    
#     data = json.load(data_file)

# for key, value in data.items():
# 	data[key] = [item for sublist in value for item in sublist]

# data = list(data.values())
# data = np.array(data)

#AUTOENCODER

data = np.loadtxt('allen_data/dev_mouse/autoencoder/encode_50.txt')

model = TSNE(n_components=2, random_state=0, n_iter=10000,metric='correlation',verbose=2)
transformed = model.fit_transform(data) 
print(transformed.shape)
transformed = np.transpose(transformed)

np.savetxt('allen_data/dev_mouse/tsne.txt', transformed)

fig = plt.figure()
plt.scatter(transformed[0], transformed[1], c='r', marker='o')
plt.show()

# app = QtGui.QApplication([])
# pg.setConfigOption('background', 'w')
# pg.plot(transformed[0], transformed[1], pen=None, symbol="o")

# app.exec_()
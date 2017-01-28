import numpy as np
from sklearn.manifold import TSNE
import pandas as pd
import json
from matplotlib import pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
# import pyqtgraph as pg
# from pyqtgraph.Qt import QtGui, QtCore

#===========CORRELATIONS===============

# with open('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt') as data_file:    
#     data = json.load(data_file)

#===========RAW DATA=================

# data=np.loadtxt("allen_data/dev_mouse/mouse_numpy_array.txt")
# data=np.reshape(data,(1912,77))

#===========AUTOENCODER============
#10400
#14200
#11550
#13650 use this
data = np.loadtxt('allen_data/dev_mouse/autoencoder_2/encode_0.txt')

#===========PCA===================

# data = np.loadtxt('allen_data/dev_mouse/pca.txt')
# data = np.transpose(data)

#=================================

model = TSNE(n_components=2, random_state=0, n_iter=10000,metric='correlation',verbose=2)
transformed = model.fit_transform(data) 
print(transformed.shape)
transformed = np.transpose(transformed)

np.savetxt('allen_data/dev_mouse/tsne.txt', transformed)

fig = plt.figure()
plt.scatter(transformed[0], transformed[1], c='r', marker='o')
fig.savefig('figures/dev_mouse/tsne/tsne.png')

# app = QtGui.QApplication([])
# pg.setConfigOption('background', 'w')
# pg.plot(transformed[0], transformed[1], pen=None, symbol="o")

# app.exec_()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(transformed[0], transformed[1], transformed[2], c='r', marker='o')
# plt.show()

#===============loop===================

# for i in range(0,500):
# 	i *= 50
# 	data = np.loadtxt('allen_data/dev_mouse/autoencoder/encode_' + str(i) + '.txt')

# 	#===========PCA===================

# 	# data = np.loadtxt('allen_data/dev_mouse/pca.txt')

# 	model = TSNE(n_components=2, random_state=0, n_iter=10000,metric='correlation',verbose=2)
# 	transformed = model.fit_transform(data) 
# 	print(transformed.shape)
# 	transformed = np.transpose(transformed)

# 	np.savetxt('allen_data/dev_mouse/tsne/tsne_' + str(i) + '.txt', transformed)

# 	# fig = plt.figure()
# 	# plt.scatter(transformed[0], transformed[1], c='r', marker='o')
# 	# fig.savefig('figures/dev_mouse/tsne/tsne_' + str(i) + '.png')
# 	# plt.close()

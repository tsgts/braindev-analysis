import numpy as np
from sklearn.manifold import TSNE
import pandas as pd
import json
from matplotlib import pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
# import pyqtgraph as pg
# from pyqtgraph.Qt import QtGui, QtCore

#===========RAW DATA=================

# data=np.loadtxt("allen_data/organoid/organoid_numpy_array.txt")
# data=np.reshape(data,(1912,150))

#===========AUTOENCODER============

#9000
#9900
# data = np.loadtxt('allen_data/organoid/autoencoder/encode_9050.txt')

#===========PCA===================

data = np.loadtxt('allen_data/organoid/pca.txt')
data = np.transpose(data)

#==================================

model = TSNE(n_components=2, random_state=0, n_iter=10000,metric='correlation',verbose=2)
transformed = model.fit_transform(data) 
print(transformed.shape)
transformed = np.transpose(transformed)

np.savetxt('allen_data/organoid/tsne.txt', transformed)

fig = plt.figure()
plt.scatter(transformed[0], transformed[1], c='r', marker='o')
fig.savefig('figures/organoid/tsne.png')

#====================================

# app = QtGui.QApplication([])
# pg.setConfigOption('background', 'w')
# pg.plot(transformed[0], transformed[1], pen=None, symbol="o")

# app.exec_()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(transformed[0], transformed[1], transformed[2], c='r', marker='o')
# plt.show()

#===============loop===================

# for i in range(0,400):
# 	i *= 50
# 	data = np.loadtxt('allen_data/organoid/autoencoder/encode_' + str(i) + '.txt')

# 	model = TSNE(n_components=2, random_state=0, n_iter=10000,metric='correlation',verbose=2)
# 	transformed = model.fit_transform(data) 
# 	print(transformed.shape)
# 	transformed = np.transpose(transformed)

# 	np.savetxt('allen_data/organoid/tsne/tsne_' + str(i) + '.txt', transformed)

# 	fig = plt.figure()
# 	plt.scatter(transformed[0], transformed[1], c='r', marker='o')
# 	fig.savefig('figures/organoid/tsne/tsne_' + str(i) + '.png')
# 	plt.close()
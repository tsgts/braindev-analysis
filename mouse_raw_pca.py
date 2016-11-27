import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore

data = np.loadtxt("allen_data/dev_mouse/encode.txt")

pca = PCA(n_components=2)
transformed = pca.fit_transform(data) 
print(transformed.shape)
print(pca.explained_variance_ratio_) 
transformed = np.transpose(transformed)

# fig = plt.figure(figsize=(50, 40))
# plt.scatter(transformed[0], transformed[1], c='r', marker='o')
# plt.show()

app = QtGui.QApplication([])
pg.setConfigOption('background', 'w')
pg.plot(transformed[0], transformed[1], pen=None, symbol="o")

app.exec_()
import numpy as np
from sklearn.manifold import TSNE
import pandas as pd
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore

data = np.loadtxt("allen_data/dev_mouse/encode.txt")

rand_indices = np.random.randint(2012*16, size=10000)

model = TSNE(n_components=2)
transformed = model.fit_transform(data[rand_indices,:]) 
print(transformed.shape)
transformed = np.transpose(transformed)

np.savetxt('allen_data/dev_mouse/tsne.txt', transformed)

app = QtGui.QApplication([])
pg.setConfigOption('background', 'w')
pg.plot(transformed[0], transformed[1], pen=None, symbol="o")

app.exec_()
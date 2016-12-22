import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.loadtxt('allen_data/dev_mouse/autoencoder/encode_100.txt')
data = np.transpose(data)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[0], data[1], data[2], c='r', marker='o')
plt.show()

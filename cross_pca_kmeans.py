import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN, KMeans
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import json
from sklearn.metrics import calinski_harabaz_score, silhouette_score
import pylab

mouse_data = np.loadtxt('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt')

mouse_data = np.subtract(np.ones_like(mouse_data),mouse_data)

mouse_clustering = AgglomerativeClustering(n_clusters=8,linkage="complete")
mouse_labels=mouse_clustering.fit_predict(mouse_data)

# mouse_matrices = np.loadtxt('allen_data/dev_human/human_numpy_array.txt')

# mouse_matrices = StandardScaler().fit_transform(mouse_matrices)

# mouse_db = KMeans(n_clusters=3, random_state=0).fit(mouse_matrices)

# mouse_labels = mouse_db.labels_

mouse_X = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne/tsne_13650.txt'))

pylab.scatter(mouse_X[:,0], mouse_X[:,1], c=mouse_labels)
plt.savefig('figures/dev_human/tsne/tsne_cluster.png',dpi=256)

# human_matrices = np.loadtxt('allen_data/dev_human/human_numpy_array.txt')

# human_matrices = StandardScaler().fit_transform(human_matrices)

# human_db = KMeans(n_clusters=8, random_state=0).fit(human_matrices)

# human_labels = human_db.labels_

# print(adjusted_rand_score(human_labels,mouse_labels))

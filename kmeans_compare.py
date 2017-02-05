import numpy as np

from sklearn.cluster import DBSCAN, KMeans
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import json
from sklearn.metrics import calinski_harabaz_score, silhouette_score
import pylab

# mouse_matrices = np.loadtxt('allen_data/dev_mouse/mouse_numpy_array.txt')

# mouse_matrices = StandardScaler().fit_transform(mouse_matrices)

# mouse_db = KMeans(n_clusters=2, random_state=0).fit(mouse_matrices)

# mouse_labels = mouse_db.labels_

# human_matrices = np.loadtxt('allen_data/dev_human/human_numpy_array.txt')

# human_matrices = StandardScaler().fit_transform(human_matrices)

# human_db = KMeans(n_clusters=2, random_state=0).fit(human_matrices)

# human_labels = human_db.labels_

# print(adjusted_rand_score(human_labels,mouse_labels))

for i in range(2,15):

	print(i)

	mouse_matrices = np.loadtxt('allen_data/dev_human/human_numpy_array.txt')

	mouse_matrices = StandardScaler().fit_transform(mouse_matrices)

	mouse_db = AgglomerativeClustering(linkage='ward', n_clusters=i).fit(mouse_matrices)

	mouse_labels = mouse_db.labels_

	print("Silhouette score: ", silhouette_score(mouse_matrices,mouse_labels))

# human_matrices = np.loadtxt('allen_data/dev_human/human_numpy_array.txt')

# human_matrices = StandardScaler().fit_transform(human_matrices)

# human_db = AgglomerativeClustering(linkage='ward', n_clusters=20).fit(human_matrices)

# human_labels = human_db.labels_

# print("Silhouette score: ", silhouette_score(human_matrices,human_labels))

# print(adjusted_rand_score(human_labels,mouse_labels))


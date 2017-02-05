import numpy as np

from sklearn.cluster import DBSCAN, KMeans
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import json
from sklearn.metrics import calinski_harabaz_score
import pylab

centers = [[1, 1], [-1, -1], [1, -1]]

X = np.loadtxt('allen_data/dev_mouse/mouse_numpy_array.txt')
print(X.shape)
# X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
#                             random_state=0)

X = StandardScaler().fit_transform(X)

db = KMeans(n_clusters=8, random_state=3).fit(X)
core_samples_mask = np.ones_like(db.labels_, dtype=bool)

labels = db.labels_

print("CH score: ", calinski_harabaz_score(X,labels))

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
 
print('Estimated number of clusters: %d' % n_clusters_)
# print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
# print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
#====CAN BE USED FOR COMPARISON===========
# print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
# print("Adjusted Rand Index: %0.3f"
#       % metrics.adjusted_rand_score(labels_true, labels))
# print("Adjusted Mutual Information: %0.3f"
#       % metrics.adjusted_mutual_info_score(labels_true, labels))
# print("Silhouette Coefficient: %0.3f"
#       % metrics.silhouette_score(X, labels))

import matplotlib.pyplot as plt

X = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne/tsne_13650.txt'))

# # Black removed and is used for noise instead.
# unique_labels = set(labels)
# colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
# for k, col in zip(unique_labels, colors):
#     if k == -1:
#         # Black used for noise.
#         col = 'k'

#     class_member_mask = (labels == k)

#     xy = X[class_member_mask]
#     plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=8)

#     xy = X[class_member_mask]
#     plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=4)

print("CH score: ", calinski_harabaz_score(X,labels))

# plt.axis('off')
# plt.ylim([-2.5,2.5])
# plt.xlim([-2.5,2.5])
# plt.savefig('figures/dev_mouse/tsne/tsne_cluster.png',dpi=256)
# json.dump(labels.tolist(), open("allen_data/dev_mouse/tsne_colors.txt",'w'), indent=4)

pylab.scatter(X[:,0], X[:,1], c=labels)
plt.savefig('figures/dev_mouse/tsne/tsne_cluster.png',dpi=256)

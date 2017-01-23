import json
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics.cluster import adjusted_mutual_info_score
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import random
import numpy as np
import collections
import seaborn as sns
import matplotlib.pyplot as plt

#human===============================
# U = np.transpose(np.loadtxt('allen_data/dev_human/tsne/tsne_7400.txt'))

#with organoid
# human_mask = json.load(open('allen_data/organoid/human_mask.txt'))
# human_mask = np.asarray(human_mask)
# U = U[human_mask]
#===============================

# U = StandardScaler().fit_transform(U)
# db_U = DBSCAN(eps=0.13, min_samples=8).fit(U)

#mouse
U = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne/tsne_15650.txt'))
U = StandardScaler().fit_transform(U)
db_U = DBSCAN(eps=0.13, min_samples=10).fit(U)

#organoid

labels_U = db_U.labels_
#labels_U = np.random.randint(24, size=1912)
unique_labels_U = sorted(list(set(labels_U)))

# core_samples_mask_U = np.zeros_like(db_U.labels_, dtype=bool)
# core_samples_mask_U[db_U.core_sample_indices_] = True

# colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels_U)))
# for k, col in zip(unique_labels_U, colors):
#     if k == -1:
#         # Black used for noise.
#         col = 'k'

#     class_member_mask = (labels_U == k)

#     xy = U[class_member_mask & core_samples_mask_U]
#     plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=8)

#     xy = U[class_member_mask & ~core_samples_mask_U]
#     plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=4)
    
# plt.axis('off')
# plt.ylim([-2.5,2.5])
# plt.xlim([-2.5,2.5])
# plt.savefig('figures/comparison/dbscans/cluster_U.png',dpi=256)
# plt.close()

#human
# V = np.transpose(np.loadtxt('allen_data/dev_human/tsne/tsne_8950.txt'))
# V = StandardScaler().fit_transform(V)
# db_V = DBSCAN(eps=0.12, min_samples=8).fit(V)

#mouse
V = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne/tsne_10600.txt'))
V = StandardScaler().fit_transform(V)
db_V = DBSCAN(eps=0.13, min_samples=10).fit(V)

#organoid
# V = np.transpose(np.loadtxt('allen_data/organoid/tsne/tsne_15550.txt'))
# V = StandardScaler().fit_transform(V)
# db_V = DBSCAN(eps=0.13, min_samples=8).fit(V)

labels_V = db_V.labels_
#labels_V = np.random.randint(24, size=1912)
unique_labels_V = list(set(labels_V))

# core_samples_mask_V = np.zeros_like(db_V.labels_, dtype=bool)
# core_samples_mask_V[db_V.core_sample_indices_] = True

# colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels_V)))
# for k, col in zip(unique_labels_V, colors):
#     if k == -1:
#         # Black used for noise.
#         col = 'k'

#     class_member_mask = (labels_V == k)

#     xy = V[class_member_mask & core_samples_mask_V]
#     plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=8)

#     xy = V[class_member_mask & ~core_samples_mask_V]
#     plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=4)
    
# plt.axis('off')
# plt.ylim([-2.5,2.5])
# plt.xlim([-2.5,2.5])
# plt.savefig('figures/comparison/dbscans/cluster_V.png',dpi=256)

matrix = []

# labels_U,labels_V = labels_V,labels_U
# unique_labels_U, unique_labels_V = unique_labels_V, unique_labels_U

for unique_label in unique_labels_U:
	row = {i:0 for i in unique_labels_V}
	for index, label in enumerate(labels_U):
		if label == unique_label:
			row[labels_V[index]]+=1
		else:
			row[labels_V[index]]+=0
	matrix.append(row)

matrix = [collections.OrderedDict(sorted(val.items())) for val in matrix]


matrix = [[i[1] for i in row.items()] for row in matrix]

for index,row in enumerate(matrix):
	row_sum = sum(row)
	matrix[index] = [int(float(val)/row_sum*100) for val in matrix[index]]

flattened_matrix = [item for sublist in matrix for item in sublist]


matrix = np.array(matrix)

plt.figure(figsize=(10, 10))
ax = sns.heatmap(matrix, square=True,cmap="viridis", annot=True,fmt="d",vmin=0,vmax=100)
plt.savefig('figures/comparison/correlation_heatmaps/cross_cluster',dpi=256)

flattened_matrix = [item for sublist in matrix for item in sublist]
flattened_matrix = [i for i in flattened_matrix if i!=0]

plt.figure(figsize=(8,2))
sns.set_style("white")
plt.ylim(0, 150)
sns.distplot(flattened_matrix, kde=False, bins= np.linspace(0,100,25), rug=False,color="black")
plt.savefig("figures/comparison/histograms/homogeneity.png",dpi=256)


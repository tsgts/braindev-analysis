import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import json
from sklearn.metrics import calinski_harabaz_score

centers = [[1, 1], [-1, -1], [1, -1]]

X = np.transpose(np.loadtxt('allen_data/dev_human/tsne/tsne_9000.txt'))
print(X.shape)
# X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
#                             random_state=0)

X = StandardScaler().fit_transform(X)

db = DBSCAN(eps=0.12, min_samples=8).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True

json.dump(core_samples_mask.tolist(), open("allen_data/dev_human/tsne_outliers.txt",'w'), indent=4)

labels = db.labels_

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

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=8)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=4)

print("CH score: ", calinski_harabaz_score(X,labels))

plt.axis('off')
plt.ylim([-2.5,2.5])
plt.xlim([-2.5,2.5])
plt.savefig('figures/dev_human/tsne/tsne_cluster.png',dpi=256)
json.dump(labels.tolist(), open("allen_data/dev_human/tsne_colors.txt",'w'), indent=4)

# for i in range(0,100):
#     print(i)
#     X = np.transpose(np.loadtxt('allen_data/dev_human/tsne/tsne_' + str(50*i+5000) + '.txt'))
#     print(X.shape)
#     # X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
#     #                             random_state=0)

#     X = StandardScaler().fit_transform(X)

#     db = DBSCAN(eps=0.13, min_samples=8).fit(X)
#     core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#     core_samples_mask[db.core_sample_indices_] = True

#     # json.dump(core_samples_mask.tolist(), open("allen_data/organoid/tsne_outliers.txt",'w'), indent=4)

#     labels = db.labels_

#     # Number of clusters in labels, ignoring noise if present.
#     n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
     
#     print('Estimated number of clusters: %d' % n_clusters_)
#     # print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
#     # print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
#     #====CAN BE USED FOR COMPARISON===========
#     # print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
#     # print("Adjusted Rand Index: %0.3f"
#     #       % metrics.adjusted_rand_score(labels_true, labels))
#     # print("Adjusted Mutual Information: %0.3f"
#     #       % metrics.adjusted_mutual_info_score(labels_true, labels))
#     # print("Silhouette Coefficient: %0.3f"
#     #       % metrics.silhouette_score(X, labels))

#     import matplotlib.pyplot as plt

#     # Black removed and is used for noise instead.
#     unique_labels = set(labels)
#     colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
#     for k, col in zip(unique_labels, colors):
#         if k == -1:
#             # Black used for noise.
#             col = 'k'

#         class_member_mask = (labels == k)

#         xy = X[class_member_mask & core_samples_mask]
#         plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
#                  markeredgecolor='k', markersize=8)

#         xy = X[class_member_mask & ~core_samples_mask]
#         plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
#                  markeredgecolor='k', markersize=4)
        
#     plt.axis('off')
#     plt.ylim([-2.5,2.5])
#     plt.xlim([-2.5,2.5])
#     plt.savefig('figures/dev_human/dbscan/'+str(i)+'.png',dpi=256)
#     plt.close()
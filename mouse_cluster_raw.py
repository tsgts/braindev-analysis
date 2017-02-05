import scipy
import pylab
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
import json
import numpy as np
from collections import defaultdict
from matplotlib import pyplot as plt
from sklearn.metrics import calinski_harabaz_score,silhouette_score
import pylab
from sklearn.metrics.cluster import adjusted_rand_score
import random

# mouse_X = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne.txt'))
# # mouse_data = np.loadtxt('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt')
# mouse_data = np.loadtxt('allen_data/dev_mouse/mouse_numpy_array.txt')
# mouse_data = np.subtract(np.ones_like(mouse_data),mouse_data)

# mouse_clustering = AgglomerativeClustering(n_clusters=8,linkage="ward")
# mouse_labels=mouse_clustering.fit_predict(mouse_data)

# print("Silhouette score: ", silhouette_score(mouse_data,mouse_labels))

# pylab.scatter(mouse_X[:,0], mouse_X[:,1], c=mouse_labels)
# plt.savefig('figures/dev_mouse/tsne/tsne_cluster.png',dpi=256)

# plt.clear()

# human_X = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne/tsne_13650.txt'))
# # human_data = np.loadtxt('allen_data/dev_human/human_corr_spearman_matrix.txt')
# human_data = np.loadtxt('allen_data/dev_human/human_numpy_array.txt')
# mouse_data = np.subtract(np.ones_like(human_data),human_data)

# human_clustering = AgglomerativeClustering(n_clusters=8,linkage="centroid")
# human_labels=human_clustering.fit_predict(human_data)

# print("Silhouette score: ", silhouette_score(human_data,human_labels))

# pylab.scatter(human_X[:,0], human_X[:,1], c=human_labels)
# plt.savefig('figures/dev_human/tsne/tsne_cluster.png',dpi=256)

# print(adjusted_rand_score(mouse_labels,human_labels))
# # ====================================

# plt.figure()
# sns.clustermap(data)

# plt.savefig('figures/dev_mouse/correlation_heatmaps/raw_dendrogram.png',dpi=256)

#=====================================

data = np.loadtxt('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt')\
# data = np.subtract(np.ones_like(data),data)

with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

D = data

# Compute and plot dendrogram.
fig = pylab.figure()
axdendro = fig.add_axes([0.09,0.1,0.2,0.8])
Y = sch.linkage(D, method="ward")
Z = sch.dendrogram(Y,no_labels=True,color_threshold=0.2*max(Y[:,2]),orientation="left")

assignments = sch.fcluster(Y, 75, criterion='distance')

unique_clusters = list(set(assignments))
print(len(unique_clusters))

# print("Silhouette score: ", silhouette_score(data,assignments))

hex_colors = {str(i):'#' + str(format(int(int(i) / (len(unique_clusters)+1) * 16777215),'02x')).upper() for i in range(0,len(unique_clusters)+1)}

assignments = [hex_colors[str(x)] for x in assignments]

# gene_colors = dict(zip(genes, assignments))

# #print(gene_colors


# plt.figure(figsize=(10,10))
# last = Y[-100:, 2]
# last_rev = last[::-1]
# idxs = np.arange(1, len(last) + 1)
# plt.plot(idxs, last_rev)

# acceleration = np.diff(last, 2)  # 2nd derivative of the distances
# acceleration_rev = acceleration[::-1]
# plt.plot(idxs[:-2] + 1, acceleration_rev)
#plt.show()

#axdendro.set_xticks([])
#axdendro.set_yticks([])

#Plot distance matrix.
axmatrix = fig.add_axes([0.3,0.1,0.6,0.8])
index = Z['leaves'][::-1]
D = np.array(D)[index,:]
D = np.array(D)[:,index]

np.savetxt("allen_data/dev_human/raw_indices.txt", index)

im = axmatrix.matshow(D, aspect='auto', origin='upper',vmax=1,vmin=-1)
axmatrix.set_xticks([])
axmatrix.set_yticks([])

# Plot colorbar.
axcolor = fig.add_axes([0.91,0.1,0.02,0.8])
pylab.colorbar(im, cax=axcolor)

#Display and save figure.
fig.savefig('figures/dev_mouse/correlation_heatmaps/raw_dendrogram.png',dpi=256)
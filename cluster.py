import scipy
import pylab
import scipy.cluster.hierarchy as sch
import json
import numpy as np
from collections import defaultdict
from matplotlib import pyplot as plt

with open('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt') as data_file:    
    data = json.load(data_file)

with open('allen_data/dev_mouse/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

D = data

# Compute and plot dendrogram.
fig = pylab.figure()
axdendro = fig.add_axes([0.09,0.1,0.2,0.8])
Y = sch.linkage(D, method='ward')
Z = sch.dendrogram(Y,no_labels=True,color_threshold=75,orientation="left")

assignments = sch.fcluster(Y, 75, criterion='distance')

unique_clusters = list(set(assignments))
print(len(unique_clusters))

hex_colors = {str(i):'#' + str(format(int(int(i) / (len(unique_clusters)-1) * 16777215),'02x')).upper() for i in range(0,len(unique_clusters)+1)}

assignments = [hex_colors[str(x)] for x in assignments]

gene_colors = dict(zip(genes, assignments))

#print(gene_colors)

json.dump(gene_colors, open("allen_data/dev_mouse/dendrogram_colors.txt",'w'), indent=4)

# plt.figure(figsize=(10,10))
# last = Y[-100:, 2]
# last_rev = last[::-1]
# idxs = np.arange(1, len(last) + 1)
# plt.plot(idxs, last_rev)

# acceleration = np.diff(last, 2)  # 2nd derivative of the distances
# acceleration_rev = acceleration[::-1]
# plt.plot(idxs[:-2] + 1, acceleration_rev)
plt.show()

#axdendro.set_xticks([])
#axdendro.set_yticks([])

# #Plot distance matrix.
# axmatrix = fig.add_axes([0.3,0.1,0.6,0.8])
# index = Z['leaves'][::-1]
# D = np.array(D)[index,:]
# D = np.array(D)[:,index]
# json.dump(D.tolist(), open("allen_data/dev_mouse/corr_matrix_array_block_sort.txt",'w'), indent=4)
# json.dump(index, open("allen_data/dev_mouse/corr_matrix_array_block_sort_indices.txt",'w'), indent=4)
# im = axmatrix.matshow(D, aspect='auto', origin='upper')
# axmatrix.set_xticks([])
# axmatrix.set_yticks([])

# # Plot colorbar.
# axcolor = fig.add_axes([0.91,0.1,0.02,0.8])
# pylab.colorbar(im, cax=axcolor)

# #Display and save figure.
# fig.show()
# fig.savefig('dendrogram.png')
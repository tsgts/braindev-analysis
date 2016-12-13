import scipy
import pylab
import scipy.cluster.hierarchy as sch
import json
import numpy as np
from collections import defaultdict

with open('allen_data/dev_mouse/mouse_corr_pearson_matrix.txt') as data_file:    
    data = json.load(data_file)

with open('allen_data/dev_mouse/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

D = data

# Compute and plot dendrogram.
fig = pylab.figure()
axdendro = fig.add_axes([0.09,0.1,0.2,0.8])
Y = sch.linkage(D, method='centroid')
Z = sch.dendrogram(Y,no_labels=True,color_threshold=0.5*max(Y[:,2]),orientation="left")
#print(Z["leaves"])
print(Z["ivl"])

cluster_idxs = defaultdict(list)
for c, pi in zip(Z['color_list'], Z['icoord']):
    for leg in pi[1:3]:
        i = (leg - 5.0) / 10.0
        if abs(i - int(i)) < 1e-5:
            cluster_idxs[c].append(int(i))

json.dump(cluster_idxs, open("allen_data/dev_mouse/dendrogram_colors.txt",'w'), indent=4)
axdendro.set_xticks([])
axdendro.set_yticks([])

#Plot distance matrix.
axmatrix = fig.add_axes([0.3,0.1,0.6,0.8])
index = Z['leaves'][::-1]
D = np.array(D)[index,:]
D = np.array(D)[:,index]
json.dump(D.tolist(), open("allen_data/dev_mouse/corr_matrix_array_block_sort.txt",'w'), indent=4)
json.dump(index, open("allen_data/dev_mouse/corr_matrix_array_block_sort_indices.txt",'w'), indent=4)
im = axmatrix.matshow(D, aspect='auto', origin='upper')
axmatrix.set_xticks([])
axmatrix.set_yticks([])

# Plot colorbar.
axcolor = fig.add_axes([0.91,0.1,0.02,0.8])
pylab.colorbar(im, cax=axcolor)

#Display and save figure.
fig.show()
fig.savefig('dendrogram.png')
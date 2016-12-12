import scipy
import pylab
import scipy.cluster.hierarchy as sch
import json
import numpy as np

with open('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt') as data_file:    
    data = json.load(data_file)

with open('allen_data/dev_mouse/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

D = data

# Compute and plot dendrogram.
fig = pylab.figure()
axdendro = fig.add_axes([0.09,0.1,0.2,0.8])
Y = sch.linkage(D, method='centroid')
Z = sch.dendrogram(Y, orientation='right')
print(Z["leaves"])
axdendro.set_xticks([])
axdendro.set_yticks([])

# Plot distance matrix.
axmatrix = fig.add_axes([0.3,0.1,0.6,0.8])
index = Z['leaves']
D = np.array(D)[index,:]
D = np.array(D)[:,index]
json.dump(D.tolist(), open("allen_data/dev_mouse/corr_matrix_array_block_sort.txt",'w'), indent=4)
json.dump(index, open("allen_data/dev_mouse/corr_matrix_array_block_sort_indices.txt",'w'), indent=4)
im = axmatrix.matshow(D, aspect='auto', origin='lower')
axmatrix.set_xticks([])
axmatrix.set_yticks([])

# Plot colorbar.
axcolor = fig.add_axes([0.91,0.1,0.02,0.8])
pylab.colorbar(im, cax=axcolor)

# Display and save figure.
fig.show()
fig.savefig('dendrogram.png')
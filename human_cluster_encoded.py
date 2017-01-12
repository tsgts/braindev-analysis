import scipy
import pylab
import scipy.cluster.hierarchy as sch
import json
import numpy as np
from collections import defaultdict
from matplotlib import pyplot as plt

with open('allen_data/dev_human/human_encoded_corr_pearson_matrix.txt') as data_file:    
    data = json.load(data_file)

with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

D = data
fig = pylab.figure()


#===============use new indices================
# axdendro = fig.add_axes([0.09,0.1,0.2,0.8])
# Y = sch.linkage(D, method='ward')
# Z = sch.dendrogram(Y,no_labels=True,color_threshold=0.2*max(Y[:,2]),orientation="left")

# assignments = sch.fcluster(Y, 50, criterion='distance')

# unique_clusters = list(set(assignments))
# print(len(unique_clusters))

# hex_colors = {str(i):'#' + str(format(int(int(i) / (len(unique_clusters)+1) * 16777215),'02x')).upper() for i in range(0,len(unique_clusters)+1)}

# assignments = [hex_colors[str(x)] for x in assignments]

# gene_colors = dict(zip(genes, assignments))

# index = Z['leaves'][::-1]

#===============================================

axmatrix = fig.add_axes([0.3,0.1,0.6,0.8])

plt.set_cmap('jet_r')
#with raw clustering indices
index = np.loadtxt("allen_data/dev_human/raw_indices.txt").tolist()

#random
#index = np.random.permutation(np.loadtxt("allen_data/dev_mouse/raw_indices.txt")).tolist()

D = np.array(D)[index,:]
D = np.array(D)[:,index]
im = axmatrix.matshow(D, aspect='auto', origin='upper')
axmatrix.set_xticks([])
axmatrix.set_yticks([])

# Plot colorbar.
axcolor = fig.add_axes([0.91,0.1,0.02,0.8])
pylab.colorbar(im, cax=axcolor)

#Display and save figure.

fig.savefig('figures/dev_human/correlation_heatmaps/encoded_dendrogram.png',dpi=256)
#fig.savefig('figures/dev_mouse/correlation_heatmaps/encoded_dendrogram_random.png',dpi=256)
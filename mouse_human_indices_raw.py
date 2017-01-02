import scipy
import pylab
import scipy.cluster.hierarchy as sch
import json
import numpy as np
from collections import defaultdict
from matplotlib import pyplot as plt

with open('allen_data/dev_mouse/mouse_raw_corr_pearson_matrix.txt') as data_file:    
    data = json.load(data_file)

with open('allen_data/dev_mouse/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

D = data
fig = pylab.figure()
axmatrix = fig.add_axes([0.3,0.1,0.6,0.8])
index = np.loadtxt("allen_data/dev_human/raw_indices.txt").tolist()
D = np.array(D)[index,:]
D = np.array(D)[:,index]
im = axmatrix.matshow(D, aspect='auto', origin='upper')
axmatrix.set_xticks([])
axmatrix.set_yticks([])

# Plot colorbar.
axcolor = fig.add_axes([0.91,0.1,0.02,0.8])
pylab.colorbar(im, cax=axcolor)

#Display and save figure.
fig.savefig('figures/comparison/correlation_heatmaps/mouse_human_indices_raw.png',dpi=256)
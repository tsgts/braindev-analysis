import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import json
import numpy as np

X = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne/tsne_13650.txt'))
X = StandardScaler().fit_transform(X)

# between trials

# with open('allen_data/dev_mouse/tsne_colors.txt') as data_file:    
#     labels = np.asarray(json.load(data_file))

# with open('allen_data/dev_mouse/tsne_outliers.txt') as data_file:    
#     core_samples_mask = np.asarray(json.load(data_file))

#between organisms

with open('allen_data/dev_human/tsne_colors.txt') as data_file:    
    labels = np.asarray(json.load(data_file))

with open('allen_data/dev_human/tsne_outliers.txt') as data_file:    
    core_samples_mask = np.asarray(json.load(data_file))


n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print(labels)

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
             markeredgecolor='k', markersize=4)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=4)
plt.axis('off')
plt.ylim([-2.5,2.5])
plt.xlim([-2.5,2.5])

# between trials
# plt.savefig('figures/dev_mouse/tsne/tsne_compare.png',dpi=256)

# between trials
plt.savefig('figures/comparison/cross_color/human_coords.png',dpi=256)
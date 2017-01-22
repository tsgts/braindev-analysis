import json
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics.cluster import adjusted_mutual_info_score
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from itertools import compress

# class MaskableList(list):
#     def __getitem__(self, index):
#         try: return super(MaskableList, self).__getitem__(index)
#         except TypeError: return MaskableList(compress(self, index))

# human_mask = json.load(open('allen_data/organoid/human_mask.txt'))

# # with open('allen_data/dev_mouse/tsne_colors.txt') as data_file:    
# #     mouse_labels = json.load(data_file)

# with open('allen_data/dev_human/tsne_colors.txt') as data_file:    
#     human_labels = MaskableList(json.load(data_file))[human_mask]

# with open('allen_data/organoid/tsne_colors.txt') as data_file:    
#     organoid_labels = json.load(data_file)

# #random.shuffle(human_labels)

# print(adjusted_rand_score(organoid_labels,human_labels))
# print(adjusted_mutual_info_score(organoid_labels,human_labels))

# aris = []
# amis = []
# log = []

# num = 100

# for i in range(0,num):


# 	#human
# 	U = np.transpose(np.loadtxt('allen_data/dev_human/tsne/tsne_' + str(50*i+5000) + '.txt'))
# 	human_mask = json.load(open('allen_data/organoid/human_mask.txt'))
# 	human_mask = np.asarray(human_mask)
# 	U = U[human_mask]

# 	#mouse
# 	# U = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne/tsne_' + str(50*i+20000) + '.txt'))

# 	U = StandardScaler().fit_transform(U)
# 	db_U = DBSCAN(eps=0.13, min_samples=8).fit(U)
# 	labels_U = db_U.labels_

# 	for j in range(0,num):

# 		#cross_comparison
# 		# V = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne/tsne_' + str(50*j+20000) + '.txt'))

# 		#human data
# 		#V = np.transpose(np.loadtxt('allen_data/dev_human/tsne/tsne_' + str(50*j+5000) + '.txt'))

# 		#organoid data
# 		V = np.transpose(np.loadtxt('allen_data/organoid/tsne/tsne_' + str(50*j+15000) + '.txt'))

# 		V = StandardScaler().fit_transform(V)

# 		#mouse
# 		#db_V = DBSCAN(eps=0.13, min_samples=10).fit(V)

# 		#human
# 		#db_V = DBSCAN(eps=0.12, min_samples=8).fit(V)

# 		#organoid
# 		db_V = DBSCAN(eps=0.13, min_samples=8).fit(V)

# 		labels_V = db_V.labels_

# 		# print("ARI: ",adjusted_rand_score(labels_U,labels_V))
# 		# print("AMI: ",adjusted_mutual_info_score(labels_U,labels_V))
# 		aris.append(adjusted_rand_score(labels_U,labels_V))
# 		amis.append(adjusted_mutual_info_score(labels_U,labels_V))
# 		log.append(str(i)+"_"+str(j)+"--"+str(adjusted_rand_score(labels_U,labels_V))+"--")
# 		print(str(i)+"_"+str(j)+"--"+str(adjusted_rand_score(labels_U,labels_V))+"--")


# json.dump(aris, open("allen_data/organoid/aris.txt",'w'), indent=4)
# json.dump(log, open("allen_data/organoid/aris_log.txt",'w'), indent=4)

# sns.set(color_codes=True)
# plt.figure()
# sns.set_style("white")
# plt.ylim(0, 1400)
# sns.distplot(aris, kde=False, bins= np.linspace(0,0.25,100), rug=False)
# plt.savefig("figures/organoid/histograms/aris.png",dpi=256)

# sns.set(color_codes=True)
# plt.figure()
# sns.set_style("white")
# sns.distplot(amis, kde=False, bins= np.linspace(0,0.25,100), rug=False)
# plt.savefig("figures/organoid/histograms/amis.png",dpi=256)


aris = json.load(open('allen_data/organoid/aris.txt'))

print(sorted(aris)[::-1][0])

# plt.figure()
# sns.set_style("white")
# plt.ylim(0, 1400)
# sns.distplot(aris, kde=False, bins= np.linspace(0,0.25,100), rug=False)
# plt.savefig("figures/organoid/histograms/aris.png",dpi=256)


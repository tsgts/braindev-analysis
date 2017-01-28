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

# with open('allen_data/dev_mouse/tsne_colors.txt') as data_file:    
#     mouse_labels = json.load(data_file)

# with open('allen_data/dev_human/tsne_colors.txt') as data_file:    
#     human_labels = json.load(data_file)

# #random.shuffle(human_labels)

# print(adjusted_rand_score(mouse_labels,human_labels))
# print(adjusted_mutual_info_score(mouse_labels,human_labels))

U = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne.txt'))

U = StandardScaler().fit_transform(U)
db_U = DBSCAN(eps=0.13, min_samples=10).fit(U)
labels_U = db_U.labels_


V = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne/tsne_13650.txt'))

V = StandardScaler().fit_transform(V)
db_V = DBSCAN(eps=0.13, min_samples=10).fit(V)

labels_V = db_V.labels_

print(adjusted_rand_score(labels_U,labels_V))

# aris = []
# amis = []

# num = 100

# for i in range(0,num):


# 	#human
# 	#U = np.transpose(np.loadtxt('allen_data/dev_human/tsne/tsne_' + str(50*i+5000) + '.txt'))

# 	#mouse
# 	U = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne/tsne_' + str(50*i+20000) + '.txt'))

# 	U = StandardScaler().fit_transform(U)
# 	db_U = DBSCAN(eps=0.13, min_samples=10).fit(U)
# 	labels_U = db_U.labels_

# 	for j in range(0,num):

# 		#cross_comparison
# 		# V = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne/tsne_' + str(50*j+20000) + '.txt'))

# 		#human data
# 		V = np.transpose(np.loadtxt('allen_data/dev_human/tsne/tsne_' + str(50*j+5000) + '.txt'))

# 		V = StandardScaler().fit_transform(V)
# 		#mouse
# 		# db_V = DBSCAN(eps=0.13, min_samples=10).fit(V)

# 		#human
# 		db_V = DBSCAN(eps=0.12, min_samples=8).fit(V)
# 		labels_V = db_V.labels_

# 		# print("ARI: ",adjusted_rand_score(labels_U,labels_V))
# 		# print("AMI: ",adjusted_mutual_info_score(labels_U,labels_V))
# 		aris.append(adjusted_rand_score(labels_U,labels_V))
# 		amis.append(adjusted_mutual_info_score(labels_U,labels_V))
# 		print(i*num+j)

# # print(aris)
# # print(amis)

# sns.set(color_codes=True)
# plt.figure()
# sns.set_style("white")
# sns.distplot(aris, kde=False, bins= np.linspace(0,0.25,100), rug=False,vmax=1400)
# plt.savefig("figures/dev_mouse/histograms/aris.png",dpi=256)

# sns.set(color_codes=True)
# plt.figure()
# sns.set_style("white")
# sns.distplot(amis, kde=False, bins= np.linspace(0,0.25,100), rug=False)
# plt.savefig("figures/dev_mouse/histograms/amis.png",dpi=256)


# sns.set(color_codes=True)
# plt.figure()
# sns.jointplot(x="ARI", y="AMI", data=pd.DataFrame(data=np.transpose([aris,amis]),columns=["ARI","AMI"]),kind="reg")
# plt.savefig("figures/comparison/regression/ari_ami.png")
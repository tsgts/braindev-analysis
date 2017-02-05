import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import json
import random

# mouse_correlations = np.loadtxt('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt')
# human_correlations = np.loadtxt('allen_data/dev_human/human_corr_spearman_matrix.txt')

# human_pvals = np.nan_to_num(np.loadtxt('allen_data/dev_human/human_spearman_pvals.txt').flatten())

# human_pvals= [x for x in human_pvals if x < 0.001]

with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

intersections=[]

# 309,239 for -0.8 - compare with 53
# 681,516 for -0.75 - compare with 229
# 299,300 for -0.7 > 7, 8 - compare with 70
# 224,209 for 0.7 > 7, 8 - compare with 40

for i in range(0,10000):
	if(i%1000)==0:
		print(i)

	mouse_sample = random.sample(genes,224)
	human_sample = random.sample(genes,209)

	intersections.append(len(list(set(mouse_sample) & set(human_sample))))

sns.set(color_codes=True)
sns.set_style("white")
plt.figure()
sns.kdeplot(np.array(intersections))
plt.show()

# #REGRESSION HISTOGRAM==============

# sns.set_style("white")
# plt.figure()
# # sns.distplot(mouse_correlations, rug=False)
# sns.distplot(human_pvals, rug=False)
# plt.show()

# #==================================

# mouse_counts=[]
# human_counts= []

# mouse_regulators = []
# human_regulators = []

# for row_index,row in enumerate(mouse_correlations):
# 	if len([i for i in row if i > 0.88]) > 10:
# 		mouse_regulators.append(genes[row_index])
# 		# mouse_counts.append(len([i for i in row if i < -0.7]))

# for row_index,row in enumerate(human_correlations):
# 	if len([i for i in row if i > 0.8]) > 8:
# 		human_regulators.append(genes[row_index])
# 		# human_counts.append(len([i for i in row if i < -0.7]))

# print(mouse_regulators)

# print(len(mouse_regulators))
# print(len(human_regulators))

# print(list(set(mouse_regulators) & set(human_regulators)))
# print(len(list(set(mouse_regulators) & set(human_regulators))))

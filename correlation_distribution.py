import numpy as np
import json
import random
import pandas as pd

binders = pd.read_csv("allen_data/dev_human/dna_binders.txt")
binders = binders["Gene"]

# mouse_correlations = np.loadtxt('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt')
# human_correlations = np.nan_to_num(np.loadtxt('allen_data/dev_human/human_corr_spearman_matrix.txt'))


# human_pvals = np.nan_to_num(np.loadtxt('allen_data/dev_human/human_spearman_pvals.txt').flatten())

# human_pvals= [x for x in human_pvals if x < 0.001]

with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

intersections=[]

# 309,239 for -0.8 - compare with 53
# 681,516 for -0.75 - compare with 229
# 299,300 for -0.7 > 7, 8 - compare with 70
# 224,209 for 0.7 > 7, 8 - compare with 40

for i in range(0,100000):
	if(i%1000)==0:
		print(i)

	mouse_sample = random.sample(genes,207)
	human_sample = random.sample(genes,210)

	intersections.append(len(list(set(mouse_sample) & set(human_sample))))


from matplotlib import pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
sns.set_style("white")
plt.figure()
sns.kdeplot(np.array(intersections))
plt.show()

#REGRESSION HISTOGRAM==============

# sns.set_style("white")
# plt.figure()
# sns.distplot(mouse_correlations.flatten(), rug=False)
# sns.distplot(human_correlations.flatten(), rug=False)
# plt.show()

#==================================

# mouse_counts=[]
# human_counts= []

# mouse_regulators = []
# human_regulators = []

# for row_index,row in enumerate(human_correlations):
# 	if len([i for i in row if i < -0.65]) > 30:
# 		human_regulators.append(genes[row_index])
# 		# human_counts.append(len([i for i in row if i < -0.7]))

# for row_index,row in enumerate(mouse_correlations):
# 	if len([i for i in row if i < -0.65]) > 20:
# 		mouse_regulators.append(genes[row_index])
# 		# mouse_counts.append(len([i for i in row if i < -0.7]))

# print("Human hubs: ",str(len(human_regulators)))
# print("Human true binders: ",str(len(list(set(human_regulators) & set(binders)))))

# print("Mouse hubs: ",str(len(mouse_regulators)))
# print("Mouse true binders: ",str(len(list(set(mouse_regulators) & set(binders)))))


# print("Total number of binders: ",str(len(list(set(genes) & set(binders)))))


# print("Shared hubs: ",str(list(set(mouse_regulators) & set(human_regulators))))
# print("Number: ",str(len(list(set(mouse_regulators) & set(human_regulators)))))

# print("Shared hubs binders: ", str(list((set(mouse_regulators) & set(human_regulators)&set(binders)))))

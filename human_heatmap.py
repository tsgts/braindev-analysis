import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import json

matrix = np.loadtxt("allen_data/dev_human/human_cropped_numpy_array.txt")

print(matrix.shape)

matrix_max = np.amax(matrix)
matrix_min = np.amin(matrix)

with open('allen_data/dev_human/raw_dictionary_no_days.txt') as data_file:    
    expression_data = json.load(data_file)

with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

for i in range(1912):
	print(genes[i])
	fig = plt.figure()
	ax = sns.heatmap(matrix[i].reshape(8,10), cmap='inferno',square=True)
	fig.savefig('figures/dev_human/heatmaps_cropped/' + genes[i] + '.png')
	plt.close()
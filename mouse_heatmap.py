import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import json

matrix = np.loadtxt("allen_data/dev_mouse/mouse_numpy_array.txt")

matrix_max = np.amax(matrix)
matrix_min = np.amin(matrix)

with open('allen_data/dev_mouse/raw_dictionary_no_days.txt') as data_file:    
    expression_data = json.load(data_file)

with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

for gene in genes:
	print(gene)
	fig = plt.figure()
	gene = gene.capitalize()
	ax = sns.heatmap(expression_data[gene], cmap='inferno',square=True)
	fig.savefig('figures/dev_mouse/heatmaps/' + gene + '.png')
	plt.close()
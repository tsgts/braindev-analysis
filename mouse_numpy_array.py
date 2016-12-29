import numpy as np
import matplotlib.pyplot as plt
import json

data_file = json.load(open('allen_data/dev_mouse/raw_dictionary_no_days.txt'))
genes = json.load(open('allen_data/dev_human/list_of_genes.txt'))
matrix_array = []
for gene in genes:
	gene = gene.capitalize()
	print(gene)
	matrix_array.append(data_file[gene])

matrix_array = np.array(matrix_array,np.float32)
print(matrix_array.shape)
print(matrix_array)
matrix_array = np.reshape(matrix_array,(1912,77))
np.savetxt('allen_data/dev_mouse/dev_mouse_array.txt', matrix_array)

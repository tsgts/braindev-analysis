import numpy as np
import matplotlib.pyplot as plt
import json

data_file = json.load(open('allen_data/dev_mouse/raw_dictionary_no_days.txt'))
genes = json.load(open('allen_data/dev_mouse/list_of_genes.txt'))
matrix_array = []
for gene in genes:
	print(gene)
	matrix_array.append(data_file[gene])

matrix_array = np.array(matrix_array,np.float32)
print(matrix_array.shape)
print(matrix_array)
matrix_array = np.reshape(matrix_array,(2012,77))
np.savetxt('allen_data/dev_mouse/mouse_numpy_array.txt', matrix_array)

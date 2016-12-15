import pandas as pd
import json

matrix = pd.read_csv("allen_data/dev_mouse/mouse_corr_spearman_matrix.csv")
matrix = pd.DataFrame(matrix.values)
matrix = matrix.as_matrix()

matrix = matrix.tolist()

for i in range(0,len(matrix)):
	matrix[i].pop(0)

json.dump(matrix, open("allen_data/dev_mouse/mouse_corr_spearman_matrix.txt",'w'), indent=4)
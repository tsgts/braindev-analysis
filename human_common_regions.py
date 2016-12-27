import pandas as pd
import json
import numpy as np
from collections import Counter

matrix = pd.read_csv("allen_data/dev_human/normalized_genes/human_regions.csv")
matrix = pd.DataFrame(matrix.values)
matrix = matrix.as_matrix()

matrix = np.transpose(matrix).tolist()


matrix.pop(0)

flat_matrix = [item for sublist in matrix for item in sublist]

print(Counter(flat_matrix))


for i in list(set(flat_matrix)):
	print(i)
	filtered_matrix = [j for j in matrix if i in j]

	#print(set(filtered_matrix[0]).intersection(*filtered_matrix))


	print(len(set(filtered_matrix[0]).intersection(*filtered_matrix)))
	print(len(filtered_matrix))

matrix = [j for j in matrix if "cerebellum" in j]
print(set(matrix[0]).intersection(*matrix))
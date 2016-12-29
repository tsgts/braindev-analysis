import pandas as pd
import json
import numpy as np
from collections import Counter
import re
import math
import collections


matrix = pd.read_csv("allen_data/dev_human/normalized_genes/human_regions.csv")
matrix = pd.DataFrame(matrix.values)
matrix = matrix.as_matrix()

matrix = np.transpose(matrix).tolist()

matrix.pop(0)

flat_matrix = [item for sublist in matrix for item in sublist]
flat_matrix = [x for x in flat_matrix if not pd.isnull(x)]

print(Counter(flat_matrix))

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

for i in natural_sort(list(set(flat_matrix))):
	print(i)
	filtered_matrix = [j for j in matrix if i in j]

	#print(set(filtered_matrix[0]).intersection(*filtered_matrix))


	print(len(set(filtered_matrix[0]).intersection(*filtered_matrix)))
	print(len(filtered_matrix))
	print(len(set(filtered_matrix[0]).intersection(*filtered_matrix))*len(filtered_matrix))

def is_sublist(list1,list2):
	commons = [x for x in list1 if x in list2]
	return commons == list1

filtered_matrix = [j for j in matrix if "MD" in j]
regions = natural_sort(list(set(filtered_matrix[0]).intersection(*filtered_matrix)))

print(regions)

timepoints = {}

for index,timepoint in enumerate(matrix):
	timepoints[str(index+1)] = is_sublist(regions,timepoint)

timepoints=collections.OrderedDict(sorted(timepoints.items()))
print(timepoints)

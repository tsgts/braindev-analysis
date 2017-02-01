import json
import pandas as pd
import collections
import numpy as np

def ranks(input):
	seq = sorted(input)
	index = [seq.index(v) for v in input]
	return index

def spearman_rho(a,b):
	n = len(a)
	a, b = ranks(a), ranks(b)
	d_squareds = [(a[i]-b[i])**2 for i in range(0,n)]
	df = n-2
	return 1-6*sum(d_squareds)/(n*(n**2-1))

data = np.loadtxt('allen_data/dev_mouse/mouse_numpy_array.txt')

matrix = []
k=0
for i in data:
	print(k)
	correlations = []
	for j in data:
		correlations.append(spearman_rho(i, j))
	matrix.append(correlations)
	k+=1

print(len(matrix))

np.savetxt('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt', matrix)
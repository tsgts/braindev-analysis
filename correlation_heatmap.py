import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy
import json
import numpy as np

with open('allen_data/dev_mouse/raw_dictionary_no_days.txt') as data_file:    
    data = json.load(data_file)

with open('allen_data/dev_mouse/corr_matrix_array_block_sort_indices.txt') as data_file:    
	index = json.load(data_file)

with open('allen_data/dev_mouse/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

genes = [genes[i] for i in index]

matrix = json.load(open('allen_data/dev_mouse/corr_matrix_array_block_sort.txt'))

print(len(matrix))

json.dump(matrix, open("allen_data/dev_mouse/corr_matrix_array.txt",'w'), indent=4)

data = [
    go.Heatmap(
        z=matrix,
        x=genes,
        y=genes,
        colorscale='Jet',
    )
]
py.iplot(data, filename='correlations-heatmap-pearson')

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy
import json

with open('allen_data/dev_mouse/raw_dictionary_no_days.txt') as data_file:    
    data = json.load(data_file)

genes = list(data.keys())

matrix = pd.read_csv("allen_data/dev_mouse/mouse_corr_r2_matrix.csv")
matrix = pd.DataFrame(matrix.values)
matrix = matrix.as_matrix()

matrix = matrix.tolist()

for i in range(0,2012):
	matrix[i].pop(0)


json.dump(matrix, open("allen_data/dev_mouse/corr_matrix_array.txt",'w'), indent=4)

data = [
    go.Heatmap(
        z=matrix,
        x=genes,
        y=genes,
    )
]
py.iplot(data, filename='correlations-heatmap')
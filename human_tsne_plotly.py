import plotly.plotly as py
import plotly.graph_objs as go
import json
import numpy as np
import random

import colorlover as cl

data = np.loadtxt('allen_data/dev_human/tsne.txt')
with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

with open('allen_data/dev_mouse/tsne_colors.txt') as data_file:    
    labels = json.load(data_file)

#random labeling
#random.shuffle(labels)

# Create a trace

# for index, val in enumerate(labels):
#     if val != 1:
#         labels[index] = 0
#     else:
#         labels[index] = 1

layout = go.Layout(
    xaxis=dict(
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=False,
        autotick=True,
        ticks='',
        showticklabels=False
    ),
    yaxis=dict(
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=False,
        autotick=True,
        ticks='',
        showticklabels=False
    )
)

trace = go.Scatter(
    x = data[0],
    y = data[1],
    mode = 'markers',
    text = genes,
    marker=dict(
        size=8,
        color=labels,                # set color to an array/list of desired values
        colorscale='Jet',   # choose a colorscale
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)

data = [trace]
fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='basic-scatter')

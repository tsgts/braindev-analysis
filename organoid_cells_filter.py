import pandas as pd
import json
import random

data = pd.read_csv('allen_data/organoid/filtered_genes.csv')
data = data.drop("Unnamed: 0",axis=1)

regions = {
	"region53": [i for i in range(0,95)],
	"region41": [i for i in range(96,169)],
	"region35": [i for i in range(170,237)],
	"region37": [i for i in range(238,308)],
	"region33": [i for i in range(309,348)],
	"region58": [i for i in range(349,427)],
	"region65": [i for i in range(428,507)]
}

for key, val in regions.items():
	regions[key] = random.sample(val,16)

regions = list(regions.values())

regions = [item for sublist in regions for item in sublist]


filtered_genes = data[data.index.isin(regions)==True]

print(filtered_genes)
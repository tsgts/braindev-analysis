import json
from collections import OrderedDict
#import seaborn as sns
#import numpy as np
#import matplotlib.pyplot as plt

output_json = {
  "nodes": [],
  "links": [],
}


with open('allen_data/dev_mouse/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

with open('allen_data/dev_mouse/corr_matrix_array.txt') as data_file:    
	data = json.load(data_file)

with open('allen_data/dev_mouse/dendrogram_colors.txt') as data_file:    
	gene_colors = json.load(data_file)

output_json["nodes"] = [{"id":i,"color":gene_colors[i]} for i in genes]

print(genes[0:10])

for i in range(0,len(genes)):
	for j in range(0,i):
		expression_val = data[i][j]
		if expression_val < -0.85:
			output_json["links"].append({"source":genes[i],"target":genes[j],"value":expression_val,"color":"#c0392b"})
		elif expression_val > 1.5:
			output_json["links"].append({"source":genes[i],"target":genes[j],"value":expression_val,"color":"#2ecc71"})
		else:
			pass

json.dump(output_json, open("graph_visualization/graph.json",'w'), indent=4)
# plt.figure()
# data = [item for sublist in data for item in sublist]
# sns.distplot(data, rug=False)
# plt.savefig("figures/dev_mouse/histograms/rho_correlations.png")
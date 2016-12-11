import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

output_json = {
  "nodes": [],
  "links": [],
}


with open('allen_data/dev_mouse/raw_dictionary_no_days.txt') as data_file:    
    genes = json.load(data_file)

genes = list(genes.keys())

with open('allen_data/dev_mouse/corr_matrix_array.txt') as data_file:    
	data = json.load(data_file)

output_json["nodes"] = [{"id":i} for i in genes]

for i in range(0,len(genes)):
	for j in range(0,i):
		expression_val = data[i][j]
		if expression_val < -0.7:
			output_json["links"].append({"source":genes[i],"target":genes[j],"value":expression_val})
		else:
			pass

json.dump(output_json, open("graph_visualization/graph.json",'w'), indent=4)
# plt.figure()
# data = [item for sublist in data for item in sublist]
# sns.distplot(data, rug=False)
# plt.savefig("figures/dev_mouse/histograms/rho_correlations.png")
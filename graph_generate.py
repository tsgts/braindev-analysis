import json
from collections import OrderedDict
import networkx as nx
#import seaborn as sns
#import numpy as np
#import matplotlib.pyplot as plt

output_json = {
  "nodes": [],
  "links": [],
}

G=nx.Graph()

with open('allen_data/dev_mouse/mouse_corr_spearman_matrix.txt') as data_file:    
	data = json.load(data_file)

with open('allen_data/dev_mouse/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

with open('allen_data/dev_mouse/dendrogram_colors.txt') as data_file:    
	gene_colors = json.load(data_file)

genes = genes[0:len(gene_colors)]

output_json["nodes"] = [{"id":i,"color":gene_colors[i]} for i in genes]

color_map = []

def pad_hex(color):
	if len(color) < 7:
		return '#' + "0"*(7-len(color)) + color[1:]
	else:
		return color
for gene in genes:
	G.add_node(gene)
	color_map.append(pad_hex(gene_colors[gene]))
print(genes[0:10])


for i in range(0,len(genes)):
	for j in range(0,i):
		#if genes[i] in genes_of_interest or genes[j] in genes_of_interest:
		expression_val = data[i][j]
		if expression_val < -0.7:
			G.add_edge(genes[i],genes[j])
			output_json["links"].append({"source":genes[i],"target":genes[j],"value":expression_val,"color":"#c0392b"})
		elif expression_val > 1.9:
			G.add_edge(genes[i],genes[j])
			output_json["links"].append({"source":genes[i],"target":genes[j],"value":expression_val,"color":"#2ecc71"})
		else:
			pass
		# else:
		# 	pass

json.dump(output_json, open("graph_visualization/graph.json",'w'), indent=4)
#nx.draw(G, with_labels = True,node_size=1024,node_color=color_map)
#plt.savefig("graph.pdf")
nx.write_gexf(G, "graph.gexf")
# plt.figure()
# data = [item for sublist in data for item in sublist]
# sns.distplot(data, rug=False)
# plt.savefig("figures/dev_mouse/histograms/rho_correlations.png")
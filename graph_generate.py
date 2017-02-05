import json
from collections import OrderedDict
import networkx as nx
#import seaborn as sns
import numpy as np
from sklearn.cluster import AgglomerativeClustering
#import matplotlib.pyplot as plt
from collections import Counter

output_json = {
  "nodes": [],
  "links": [],
}

G=nx.Graph()

data = np.loadtxt('allen_data/dev_human/human_corr_spearman_matrix.txt')

clustering = AgglomerativeClustering(n_clusters=16,linkage="ward")
labels=clustering.fit_predict(data)

with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

gene_colors = dict(zip(genes,labels))

# output_json["nodes"] = [{"id":i,"color":str(gene_colors[i])} for i in genes]


def pad_hex(color):
	if len(color) < 7:
		return '#' + "0"*(7-len(color)) + color[1:]
	else:
		return color
for gene in genes:
	G.add_node(gene)

nodes = []
edges = []


for i in range(0,len(genes)):
	for j in range(0,i):
		#if genes[i] in genes_of_interest or genes[j] in genes_of_interest:
		expression_val = data[i][j]
		if expression_val < -1.75:
			G.add_edge(genes[i],genes[j])
			output_json["links"].append({"source":genes[i],"target":genes[j],"value":expression_val,"color":"#c0392b"})
			edges.append(genes[i])
			edges.append(genes[j])
		elif expression_val > 0.8:
			G.add_edge(genes[i],genes[j])
			output_json["links"].append({"source":genes[i],"target":genes[j],"value":expression_val,"color":"#2ecc71"})
			edges.append(genes[i])
			edges.append(genes[j])
		else:
			pass
		# else:
		# 	pass
edges = Counter(edges)

for gene,count in edges.items():
	output_json["nodes"].append({"id":gene,"color":str(gene_colors[gene]),"degree":count})

json.dump(output_json, open("graph_visualization/graph.json",'w'), indent=4)
#nx.draw(G, with_labels = True,node_size=1024,node_color=color_map)
#plt.savefig("graph.pdf")
nx.write_gexf(G, "graph.gexf")
# plt.figure()
# data = [item for sublist in data for item in sublist]
# sns.distplot(data, rug=False)
# plt.savefig("figures/dev_mouse/histograms/rho_correlations.png")
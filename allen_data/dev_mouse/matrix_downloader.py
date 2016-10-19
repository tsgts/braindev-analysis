import csv
from csv import DictReader
import urllib
from urllib.request import urlretrieve


#get a list of all genes
with open("all_the_genes.csv") as gene_list:
	genes = [row["id"] for row in DictReader(gene_list)]

#these IDs are broken
bad_ids = [129337,17954,11858]

for index, gene_id in enumerate(genes):
	#the expression matrices for gene ids 129337,17954, and 11858 are mysteriously absent...
	if gene_id not in bad_ids:
		url = "http://developingmouse.brain-map.org/expressionSummaries/{0}.png"
		url = url.format(gene_id)
		#interpolate the url and the gene ID
		urllib.request.urlretrieve(url, "expression_matrices/" + gene_id + ".png")
		#log the current progress
		print(str(index+1) + " of " + str(len(genes)))
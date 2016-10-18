import csv
from csv import DictReader
import urllib
from urllib.request import urlretrieve

bad_ids = [129337,17954,11858]
with open("all_the_genes.csv") as gene_list:
	genes = [row["id"] for row in DictReader(gene_list)]

for index, gene_id in enumerate(genes):
	#the expression matrices for gene ids 129337,17954, and 11858 are mysteriously absent...
	if gene_id not in bad_ids:
		url = "http://developingmouse.brain-map.org/expressionSummaries/{0}.png"
		url = url.format(gene_id)
		urllib.request.urlretrieve(url, "expression_matrices/" + gene_id + ".png")

		print(str(index+1) + " of " + str(len(genes)))
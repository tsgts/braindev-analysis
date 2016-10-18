import csv
from csv import DictReader

with open("all_the_genes.csv") as gene_list:
	gene = [row["id"] for row in DictReader(gene_list)]
	print(gene)
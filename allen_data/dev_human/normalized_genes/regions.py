import csv
from csv import DictReader

with open("columns_metadata.csv") as gene_list:
	regions = [row["structure_name"] for row in DictReader(gene_list)]
#print a unique set of the regions
regions = sorted(set(regions))
for region in regions:
	print(region)
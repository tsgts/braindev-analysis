import csv
from csv import DictReader
import urllib.request
import string
from string import Template

with open("all_the_genes.csv") as gene_list:
	gene = [row["id"] for row in DictReader(gene_list)]
	print(gene)

gene_id = '76994'
url = "http://api.brain-map.org/api/v2/data/query.csv?criteria=model::StructureUnionize,rma::criteria,section_data_set[delegate$eqfalse]%28genes[id$in%27{0}%27],specimen%28donor%28age[name$in%27E11.5%27,%27E13.5%27,%27E15.5%27,%27E18.5%27,%27P4%27,%27P14%27,%27P28%27]%29%29%29,structure%28structure_sets_structures%28structure_set[name$eq%27Developing%20Mouse%20-%20Coarse%27]%29%29&tabular=genes.id,ages.days,structures.acronym,structures.name,structures.graph_order,structure_unionizes.expression_energy&num_rows=10000000"
url = url.format(gene_id)
response = urllib.request.urlopen(url)
csv = response.read()
with open("express.csv", "wb") as f:
	f.write(csv)

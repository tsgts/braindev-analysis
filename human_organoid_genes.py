import json
import numpy
from collections import Counter

human_genes = json.load(open('allen_data/dev_human/list_of_genes.txt'))

organoid_genes = json.load(open('allen_data/organoid/list_of_genes.txt'))

for index,val in enumerate(human_genes):
	if val not in organoid_genes:
		human_genes[index] = False
	else:
		human_genes[index] = True

json.dump(human_genes, open("allen_data/organoid/human_mask.txt",'w'), indent=4)

print(Counter(human_genes))
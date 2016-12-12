import numpy as np
import math
import pandas as pd
from collections import Counter

mouse_genes = pd.read_csv("allen_data/dev_mouse/log_expression_values.csv")
mouse_genes = mouse_genes["gene_acronym"]
mouse_genes = [x.upper() for x in mouse_genes]

human_genes = pd.read_csv("allen_data/dev_human/normalized_genes/rows_metadata.csv")
human_genes = human_genes["gene_symbol"]

intersection = list(set(mouse_genes) & set(human_genes))

print(len(intersection))
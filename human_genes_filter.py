import pandas as pd
import json
import collections

with open('allen_data/dev_human/common_genes.txt') as data_file:    
    good_genes = json.load(data_file)

columns = [str(i) for i in range(0,525)]

expression_matrix = pd.read_csv("allen_data/dev_human/normalized_genes/expression_matrix.csv",names=columns)

print(expression_matrix)

rows_metadata = pd.read_csv("allen_data/dev_human/normalized_genes/rows_metadata.csv")
filtered_genes = rows_metadata[rows_metadata["gene_symbol"].isin(good_genes)==True]


#get rid of DTX2 duplicate
filtered_genes = filtered_genes[filtered_genes["row_num"] != 44945]

good_rows = list(filtered_genes["row_num"])

expression_matrix=expression_matrix[expression_matrix["0"].isin(good_rows) == True]

print(expression_matrix)

expression_matrix.reset_index(inplace=True,drop=True)

expression_matrix.to_csv("allen_data/dev_human/gene_filtered_expression_values.csv",sep=',', encoding='utf-8')
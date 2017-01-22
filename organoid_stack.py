import pandas as pd

expression_values = pd.read_csv("allen_data/organoid/stacked_timepoints.csv")
expression_values = expression_values.drop("Unnamed: 0", 1)
expression_values = expression_values.drop("species", 1)

genes = list(expression_values.columns.values)
genes.remove("timepoint")
genes.remove("sample_num")

expression_values = pd.melt(expression_values, id_vars=['timepoint', 'sample_num'], var_name='gene', value_name='expression_value')

print(expression_values)

expression_values.to_csv("allen_data/organoid/stacked_genes.csv",sep=',', encoding='utf-8')
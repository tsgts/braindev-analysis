import pandas as pd

expression_values = pd.read_csv("allen_data/organoid/stacked_genes.csv")
expression_values.drop("Unnamed: 0", 1)

expression_values = pd.pivot_table(expression_values,values='expression_value',index=['gene','timepoint'],columns=['sample_num'])

expression_values.to_csv("allen_data/organoid/pivot_matrix.csv",sep=',', encoding='utf-8')
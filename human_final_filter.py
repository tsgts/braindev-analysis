import pandas as pd

filtered_columns = pd.read_csv("allen_data/dev_human/filtered_columns.csv")

expression_values = pd.read_csv("allen_data/dev_human/gene_filtered_expression_values.csv")

good_columns = list(filtered_columns["column_num"])


bad_columns = [i for i in range(1,525) if i not in good_columns]

for i in bad_columns:
	expression_values = expression_values.drop(str(i),1)

expression_values = expression_values.drop("Unnamed: 0",1)
expression_values = expression_values.set_index("0")
expression_values.index.name = "gene_symbol"

expression_values = expression_values.stack()

print(expression_values)

expression_values.to_csv("allen_data/dev_human/stacked_expression_values.csv",sep=',', encoding='utf-8')
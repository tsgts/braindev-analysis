import pandas as pd

stacked_expression_values = pd.read_csv("allen_data/dev_human/stacked_expression_values.csv",names=["gene","column_num","expression_value"])

stacked_expression_values = stacked_expression_values.sort_values(by="gene")

print(stacked_expression_values)

stacked_expression_values.to_csv("allen_data/dev_human/expression_matrix.csv",sep=',', encoding='utf-8')
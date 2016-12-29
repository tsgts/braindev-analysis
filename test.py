import pandas as pd

columns = [str(i) for i in range(0,525)]
expression_matrix = pd.read_csv("allen_data/dev_human/normalized_genes/expression_matrix.csv",names=columns)
print(expression_matrix)
print(expression_matrix.at[6091,"208"])
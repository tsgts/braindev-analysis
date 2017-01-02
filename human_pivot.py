import pandas as pd

expression_values = pd.read_csv("allen_data/dev_human/expression_matrix.csv")
expression_values.drop("Unnamed: 0", 1)
expression_values.drop("index", 1)
expression_values.drop("column_num", 1)
expression_values.drop("donor", 1)
expression_values = pd.pivot_table(expression_values,values='expression_value',index=['gene','age'],columns=['structure'])

expression_values.to_csv("allen_data/dev_human/pivot_matrix.csv",sep=',', encoding='utf-8')
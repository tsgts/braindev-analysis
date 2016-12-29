import pandas as pd

stacked_expression_values = pd.read_csv("allen_data/dev_human/stacked_expression_values.csv",names=["gene","column_num","expression_value"])

columns_metadata = pd.read_csv("allen_data/dev_human/normalized_genes/columns_metadata.csv")

stacked_expression_values = stacked_expression_values.sort_values(by="gene")

stacked_expression_values.reset_index(inplace=True)

column_nums = list(stacked_expression_values["column_num"])

ages = [columns_metadata.at[i-1,"age"] for i in column_nums]
structures = [columns_metadata.at[i-1,"structure_acronym"] for i in column_nums]
donors = [columns_metadata.at[i-1,"donor_name"] for i in column_nums]

metadata = pd.DataFrame({'age':ages,'structure':structures,'donor':donors})

stacked_expression_values = pd.concat([stacked_expression_values,metadata],axis=1)

stacked_expression_values.to_csv("allen_data/dev_human/expression_matrix.csv",sep=',', encoding='utf-8')
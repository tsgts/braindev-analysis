import pandas as pd

good_timepoints = [5,6,8,9,10,11,13,15,17,18,19,20,21,22,23]

good_regions = ["A1C","AMY","CBC","HIP","IPC","MD","OFC","STC","STR","VFC"]

columns_metadata = pd.read_csv("allen_data/dev_human/normalized_genes/rearranged_columns_metadata.csv")

columns_metadata["sample_num"].astype(int)

columns_metadata = columns_metadata[columns_metadata["sample_num"].isin(good_timepoints)==True]
columns_metadata = columns_metadata[columns_metadata["structure_acronym"].isin(good_regions)==True]

print(columns_metadata)

columns_metadata.to_csv("allen_data/dev_human/filtered_columns.csv",sep=',', encoding='utf-8')
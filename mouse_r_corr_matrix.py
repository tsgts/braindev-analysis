from sklearn.metrics import r2_score
import json
import pandas as pd

with open('allen_data/dev_mouse/raw_dictionary_no_days.txt') as data_file:    
    data = json.load(data_file)

for key, value in data.items():
	data[key] = [item for sublist in value for item in sublist]

genes = data.keys()

matrix = []

for i in genes:
	print(i)
	correlations = []
	for j in genes:
		correlations.append(r2_score(data[i], data[j])  ) 
	matrix.append(correlations)

print(len(matrix))

df=pd.DataFrame(matrix,columns=genes)
print(df.shape)

df.to_csv("allen_data/dev_mouse/mouse_corr_r2_matrix.csv",sep=',', encoding='utf-8')
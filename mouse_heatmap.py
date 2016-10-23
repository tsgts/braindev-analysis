import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

# np.random.seed(0)
# sns.set()
# flights = sns.load_dataset("flights")
# print(flights)
# flights = flights.pivot("month", "year", "passengers")
# print(flights)
# ax = sns.heatmap(flights, center=300)
# plt.show()

gene_of_interest = "Foxp2"
expression_data = pd.read_csv("allen_data/dev_mouse/filtered_expression_values.csv")
matching_rows = expression_data[expression_data["gene_acronym"]==gene_of_interest]
matching_rows.reset_index(drop=True,inplace=True)


def age_adjust(age):
	if age in [4.0,14.0,28.0]:
		age += 19
	return age

matching_rows["days"] = matching_rows["days"].map(age_adjust)

sorted_rows = matching_rows.sort_values("days",axis=0)

print(sorted_rows)
ages = sorted_rows.loc[:,["days","age"]]
ages = pd.concat([ages]*11)
ages = ages.sort_values("days",axis=0)
ages.reset_index(drop=True,inplace=True)

heatmap_raw = sorted_rows.loc[:,["RSP","Tel","PHy","p3","p2","p1","M","PPH","PH","PMH","MH"]]

heatmap_raw = heatmap_raw.stack()
heatmap_raw.reset_index(drop=True,inplace=True)

regions = pd.DataFrame.from_dict({'region':["RSP","Tel","PHy","p3","p2","p1","M","PPH","PH","PMH","MH"]})
regions = pd.concat([regions]*7)
regions.reset_index(drop=True,inplace=True)

heatmap_raw = pd.concat([ages["age"],regions,heatmap_raw], axis=1)
heatmap_raw.columns = ["age","region","expression"]


heatmap_raw = heatmap_raw.pivot("age","region","expression")
heatmap_raw = heatmap_raw.reindex(index=["E11.5","E13.5","E15.5","E18.5","P4","P14","P28"],columns=["RSP","Tel","PHy","p3","p2","p1","M","PPH","PH","PMH","MH"])
print(heatmap_raw)


sns.set()
ax = sns.heatmap(heatmap_raw, center=0)
plt.show()
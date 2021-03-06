import numpy as np
import math
import pandas as pd

expression_data = pd.read_csv("allen_data/dev_human/pivot_matrix.csv")

regions = ["A1C","AMY","CBC","HIP","IPC","MD","OFC","STC","STR","VFC"]

def safe_log(x):
	if math.isnan(x):
		return -10
	x = float(x)
	if x<=0:
		return -10
	else:
   		return math.log2(x)

#single log
for region in regions:
	expression_data[region] = expression_data[region].apply(safe_log)

expression_data.to_csv("allen_data/dev_human/log_expression_values.csv",sep=',', encoding='utf-8')
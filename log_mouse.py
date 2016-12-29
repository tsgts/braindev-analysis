import numpy as np
import math
import pandas as pd

expression_data = pd.read_csv("allen_data/dev_mouse/devmouse_histogram_values.csv")

regions = ["RSP","Tel","PHy","p3","p2","p1","M","PPH","PH","PMH","MH"]

def safe_log(x):
	if math.isnan(x):
		return -8
	x = float(x)
	if x<=0:
		return -8
	else:
   		return math.log2(x)

#single log
for region in regions:
	expression_data[region] = expression_data[region].apply(safe_log)

expression_data.to_csv("allen_data/dev_mouse/log_expression_values.csv",sep=',', encoding='utf-8')
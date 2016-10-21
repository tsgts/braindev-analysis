import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from scipy.stats import spearmanr

expression_data = pd.read_csv("allen_data/dev_mouse/devmouse_histogram_values.csv")

def safe_log(x):
	if math.isnan(x):
		return -8
	x = float(x)
	if x<=0:
		return -8
	else:
   		return math.log10(x)

regions = ["RSP","Tel","PHy","p3","p2","p1","M","PPH","PH","PMH","MH"]

#single log
for region in regions:
	expression_data[region] = expression_data[region].apply(safe_log)

expression_data.to_csv("allen_data/dev_mouse/log_expression_values.csv",sep=',', encoding='utf-8')
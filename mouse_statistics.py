import csv
from csv import DictReader
import urllib
from urllib.request import urlretrieve
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math

data = csv.reader(open("allen_data/dev_mouse/devmouse_histogram_values.csv"))
col1 = next(data)
regions = col1[6:]

def safe_log(x):
	if x=='':
		return 0
	x = float(x)
	if x<=0:
		return 0
	else:
   		return math.log10(x)

region_expressions = {}

def col_vals(col):
	expression_data = open("allen_data/dev_mouse/devmouse_histogram_values.csv")
	return [row[col] for row in DictReader(expression_data)]

def log_float(vals):
	return [safe_log(val) for val in vals]

for region in regions:
	print("Completed " + region)
	region_expressions[region] = log_float(col_vals(region))
	
sns.distplot(region_expressions["RSP"], kde=False, rug=False)

sns.set(color_codes=True)
plt.show()

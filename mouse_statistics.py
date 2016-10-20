import csv
from csv import DictReader
import urllib
from urllib.request import urlretrieve
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math

def safe_log(x):
   if x<=0:
    return None
   else:
   	return math.log10(x)

def col_vals(col):
	expression_data = open("allen_data/dev_mouse/devmouse_histogram_values.csv")
	return [row[col] for row in DictReader(expression_data)]

def log_float(vals):
	return [safe_log(float(val)) for val in vals]

RSP = log_float(col_vals("RSP"))
Tel = log_float(col_vals("RSP"))

sns.set(color_codes=True)
sns.distplot(RSP, kde=False, rug=False)
plt.show()

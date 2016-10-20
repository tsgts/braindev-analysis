import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd


expression_data = pd.read_csv("allen_data/dev_mouse/devmouse_histogram_values.csv")

def safe_log(x):
	if math.isnan(x):
		return 0
	x = float(x)
	if x<=0:
		return 0
	else:
   		return math.log10(x)

regions = ["RSP","Tel","PHy","p3","p2","p1","M","PPH","PH","PMH","MH"]

for region in regions:
	expression_data[region] = expression_data[region].apply(safe_log)

#histograms for each region
def histograms():
	for region in regions:
		print(region)
		plt.figure(figsize=(60, 30))
		sns.distplot(expression_data[region], kde=False, rug=False)

		plt.savefig("figures/dev_mouse/histograms/"+region+".png")
		plt.clf()

#correlations between the regions
def correlations():
	for region1 in regions:
		for region2 in regions:
			print(region1 + "-" + region2)
			plt.figure(figsize=(60, 30))
			sns.regplot(x=region1, y=region2, data=expression_data)
			plt.savefig("figures/dev_mouse/linregs/"+region1+"-"+region2+".png")
			plt.clf()

correlations()
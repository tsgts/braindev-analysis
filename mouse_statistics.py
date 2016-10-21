import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from scipy.stats import kendalltau

expression_data = pd.read_csv("allen_data/dev_mouse/devmouse_histogram_values.csv")

def safe_log(x):
	if math.isnan(x):
		return 0.0
	x = float(x)
	if x<=0:
		return 0.0
	else:
   		return math.log10(x)

regions = ["RSP","Tel","PHy","p3","p2","p1","M","PPH","PH","PMH","MH"]

#single log
for region in regions:
	expression_data[region] = expression_data[region].apply(safe_log)

#histograms for each region
def histograms():
	for region in regions:
		print(region)
		plt.figure(figsize=(60, 30))
		sns.distplot(expression_data[region], rug=False)
		plt.savefig("figures/dev_mouse/histograms/"+region+".png")

#all on one figure		
def all_histograms():
	sns.set(color_codes=True)
	plt.figure(figsize=(60, 30))
	for region in regions:
		print(region)
		sns.distplot(expression_data[region], rug=False)
		plt.savefig("figures/dev_mouse/histograms/all.png")

#correlations between the regions
def correlations():
	for region1 in regions:
		for region2 in regions:
			if region1 != region2:
				print(region1 + "-" + region2)
				plt.figure(figsize=(60, 30))
				sns.jointplot(x=region1, y=region2, data=expression_data,kind="reg", marker=".")
				plt.savefig("figures/dev_mouse/linregs/"+region1+"-"+region2+".png")

#hexplot with plot density
def hexplots():
	for region1 in regions:
		for region2 in regions:
			if region1 != region2:
				print(region1 + "-" + region2)
				sns.jointplot(x=region1, y=region2, data=expression_data,kind="hex", stat_func=spearmanr, color="#c0392b")
				plt.savefig("figures/dev_mouse/hexplots/"+region1+"-"+region2+".png")

#contours
def contours():
	for region1 in regions:
		for region2 in regions:
			if region1 != region2:
				print(region1 + "-" + region2)
				sns.jointplot(x=region1, y=region2, data=expression_data,kind="kde", color="g", stat_func=spearmanr)
				plt.savefig("figures/dev_mouse/contours/"+region1+"-"+region2+".png")

#contours with scatter points
def scatter_contours():
	for region1 in regions:
		for region2 in regions:
			if region1 != region2:
				print(region1 + "-" + region2)
				sns.jointplot(region1, region2, data=expression_data, color="b", marker="+",s=4).plot_joint(sns.kdeplot, zorder=0, n_levels=6)
				plt.savefig("figures/dev_mouse/scatter_contours/"+region1+"-"+region2+".png")

#adjust post-birth ages
index=0
for age in expression_data["days"]:
	if age in [4.0,14.0,28.0]:
		expression_data.loc[index,"days"]=age+19
	index+=1
print("Completed age adjustment.")

#linear regression between age, expression
def ages_linregs():
	sns.set(color_codes=True)
	plt.figure(figsize=(60, 30))
	for region in regions:
		print(region)
		sns.jointplot(x="days", y=region, data=expression_data,kind="reg", stat_func=spearmanr)
		plt.savefig("figures/dev_mouse/time_linregs/"+region+".png")

#contour plots of age vs expression
def ages_contours():
	sns.set(color_codes=True)
	plt.figure(figsize=(60, 30))
	for region in regions:
		print(region)
		sns.jointplot(x="days", y=region, data=expression_data,kind="kde", stat_func=spearmanr)
		plt.savefig("figures/dev_mouse/time_contours/"+region+".png")

#quartic regression between age, expression
def ages_quartregs():
	sns.set(color_codes=True)
	plt.figure(figsize=(60, 30))
	for region in regions:
		print(region)
		sns.lmplot(x="days", y=region, data=expression_data,order=4, stat_func=spearmanr)
		plt.savefig("figures/dev_mouse/time_quartregs/"+region+".png")

#swarm diagrams		
def time_swarm():
	sns.set(color_codes=True)
	plt.figure(figsize=(60, 30))
	for region in regions:
		print(region)
		sns.swarmplot(x="days", y=region, data=expression_data)
		plt.savefig("figures/dev_mouse/time_swarm/"+region+".png")

histograms()
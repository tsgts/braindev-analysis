import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

#log2
expression_data = pd.read_csv("allen_data/organoid/pivot_matrix.csv")

#raw
#expression_data = pd.read_csv("allen_data/organoid/pivot_matrix.csv")

regions = [str(i) for i in range(1,21)]

#histograms for each region
def histograms():
	sns.set(color_codes=True)
	sns.set_style("white")
	for region in regions:
		print(region)
		fig = plt.figure()
		sns.distplot(expression_data[region], rug=False, kde=False)
		plt.savefig("figures/organoid/histograms/"+region+".png",dpi=256)
		fig.clear()

#all on one figure		
def all_histograms():
	sns.set(color_codes=True)
	sns.set_style("white")
	for region in regions:
		print(region)
		sns.distplot(expression_data[region], kde=False, bins= 50, rug=False)
	plt.savefig("figures/organoid/histograms/all.png",dpi=256)

#correlations between the regions
def correlations():
	for region1 in regions:
		for region2 in regions:
			if region1 != region2:
				print(region1 + "-" + region2)
				fig = plt.figure()
				sns.jointplot(x=region1, y=region2, data=expression_data,kind="reg", marker=".")
				plt.savefig("figures/organoid/linregs/"+region1+"-"+region2+".png",dpi=256)
				fig.clear()

#hexplot with plot density
def hexplots():
	for region1 in regions:
		for region2 in regions:
			if region1 != region2:
				print(region1 + "-" + region2)
				fig = plt.figure()
				sns.jointplot(x=region1, y=region2, data=expression_data,kind="hex", stat_func=spearmanr, color="#c0392b")
				plt.savefig("figures/organoid/hexplots/"+region1+"-"+region2+".png",dpi=256)
				fig.clear()

#contours
def contours():
	for region1 in regions:
		for region2 in regions:
			if region1 != region2:
				print(region1 + "-" + region2)
				fig = plt.figure()
				sns.jointplot(x=region1, y=region2, data=expression_data,kind="kde", color="g", stat_func=spearmanr)
				plt.savefig("figures/organoid/contours/"+region1+"-"+region2+".png",dpi=256)
				fig.clear()

#contours with scatter points
def scatter_contours():
	for region1 in regions:
		for region2 in regions:
			if region1 != region2:
				print(region1 + "-" + region2)
				fig = plt.figure()
				sns.jointplot(region1, region2, data=expression_data, color="b", marker="+",s=4).plot_joint(sns.kdeplot, zorder=0, n_levels=6)
				plt.savefig("figures/organoid/scatter_contours/"+region1+"-"+region2+".png",dpi=256)
				fig.clear()

#linear regression between age, expression
def ages_linregs():
	sns.set(color_codes=True)
	for region in regions:
		print(region)
		fig = plt.figure()
		sns.jointplot(x="age", y=region, data=expression_data,kind="reg")
		plt.savefig("figures/organoid/time_linregs/"+region+".png")
		fig.clear()

#contour plots of age vs expression
def ages_contours():
	sns.set(color_codes=True)
	for region in regions:
		print(region)
		fig = plt.figure()
		sns.jointplot(x="age", y=region, data=expression_data,kind="kde")
		plt.savefig("figures/organoid/time_contours/"+region+".png",dpi=256)
		fig.clear()

#quartic regression between age, expression
def ages_quartregs():
	sns.set(color_codes=True)
	for region in regions:
		print(region)
		fig = plt.figure()
		sns.lmplot(x="age", y=region, data=expression_data,order=4)
		plt.savefig("figures/organoid/time_quartregs/"+region+".png",dpi=256)
		fig.clear()

#swarm diagrams		
def time_swarm():
	sns.set(color_codes=True)
	for region in regions:
		print(region)
		fig = plt.figure()
		sns.swarmplot(x="age", y=region, data=expression_data)
		plt.savefig("figures/organoid/time_swarm/"+region+".png",dpi=256)
		fig.clear()

histograms()
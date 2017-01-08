import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

#log2
expression_data = pd.read_csv("allen_data/dev_human/log_expression_values.csv")

#raw
#expression_data = pd.read_csv("allen_data/dev_human/pivot_matrix.csv")

regions = ["A1C","AMY","CBC","HIP","IPC","MD","OFC","STC","STR","VFC"]

#histograms for each region
def histograms():
	for region in regions:
		print(region)
		fig = plt.figure()
		sns.distplot(expression_data[region], rug=False)
		plt.savefig("figures/dev_human/histograms/"+region+".png",dpi=256)
		fig.clear()

#all on one figure		
def all_histograms():
	sns.set(color_codes=True)
	sns.set_style("white")
	for region in regions:
		print(region)
		sns.distplot(expression_data[region], kde=False, bins= np.linspace(-15,10,40), rug=False)
	plt.savefig("figures/dev_human/histograms/all.png",dpi=256)

#correlations between the regions
def correlations():
	for region1 in regions:
		for region2 in regions:
			if region1 != region2:
				print(region1 + "-" + region2)
				fig = plt.figure()
				sns.jointplot(x=region1, y=region2, data=expression_data,kind="reg", marker=".")
				plt.savefig("figures/dev_human/linregs/"+region1+"-"+region2+".png",dpi=256)
				fig.clear()

#hexplot with plot density
def hexplots():
	for region1 in regions:
		for region2 in regions:
			if region1 != region2:
				print(region1 + "-" + region2)
				fig = plt.figure()
				sns.jointplot(x=region1, y=region2, data=expression_data,kind="hex", stat_func=spearmanr, color="#c0392b")
				plt.savefig("figures/dev_human/hexplots/"+region1+"-"+region2+".png",dpi=256)
				fig.clear()

#contours
def contours():
	for region1 in regions:
		for region2 in regions:
			if region1 != region2:
				print(region1 + "-" + region2)
				fig = plt.figure()
				sns.jointplot(x=region1, y=region2, data=expression_data,kind="kde", color="g", stat_func=spearmanr)
				plt.savefig("figures/dev_human/contours/"+region1+"-"+region2+".png",dpi=256)
				fig.clear()

#contours with scatter points
def scatter_contours():
	for region1 in regions:
		for region2 in regions:
			if region1 != region2:
				print(region1 + "-" + region2)
				fig = plt.figure()
				sns.jointplot(region1, region2, data=expression_data, color="b", marker="+",s=4).plot_joint(sns.kdeplot, zorder=0, n_levels=6)
				plt.savefig("figures/dev_human/scatter_contours/"+region1+"-"+region2+".png",dpi=256)
				fig.clear()

#adjust post-birth ages

int_age = {

	"16 pcw": -22,
	"17 pcw": -21,
	"24 pcw": -14,
	"37 pcw": -1,
	"4 mos": 0.33,
	"1 yrs": 1,
	"8 yrs": 8,
	"13 yrs": 13,
	"19 yrs": 19,
	"21 yrs": 21,
	"23 yrs": 23,
	"30 yrs": 30,
	"36 yrs": 36,
	"37 yrs": 37,
	"40 yrs": 40,

}

index=0
for age in expression_data["age"]:
	expression_data.loc[index,"age"]=int_age[age]
	index+=1

print("Completed age adjustment.")

print(expression_data)

#linear regression between age, expression
def ages_linregs():
	sns.set(color_codes=True)
	for region in regions:
		print(region)
		fig = plt.figure()
		sns.jointplot(x="age", y=region, data=expression_data,kind="reg")
		plt.savefig("figures/dev_human/time_linregs/"+region+".png")
		fig.clear()

#contour plots of age vs expression
def ages_contours():
	sns.set(color_codes=True)
	for region in regions:
		print(region)
		fig = plt.figure()
		sns.jointplot(x="age", y=region, data=expression_data,kind="kde")
		plt.savefig("figures/dev_human/time_contours/"+region+".png",dpi=256)
		fig.clear()

#quartic regression between age, expression
def ages_quartregs():
	sns.set(color_codes=True)
	for region in regions:
		print(region)
		fig = plt.figure()
		sns.lmplot(x="age", y=region, data=expression_data,order=4)
		plt.savefig("figures/dev_human/time_quartregs/"+region+".png",dpi=256)
		fig.clear()

#swarm diagrams		
def time_swarm():
	sns.set(color_codes=True)
	for region in regions:
		print(region)
		fig = plt.figure()
		sns.swarmplot(x="age", y=region, data=expression_data)
		plt.savefig("figures/dev_human/time_swarm/"+region+".png",dpi=256)
		fig.clear()

all_histograms()
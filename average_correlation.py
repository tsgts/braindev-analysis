import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ranks(input):
	seq = sorted(input)
	index = [seq.index(v) for v in input]
	return index

def spearman_rho(a,b):
	n = len(a)
	a, b = ranks(a), ranks(b)
	d_squareds = [(a[i]-b[i])**2 for i in range(0,n)]
	df = n-2
	return 1-6*sum(d_squareds)/(n*(n**2-1))

human_numpy_array = np.loadtxt("allen_data/dev_human/human_cropped2_numpy_array.txt")
human_averages = np.mean(human_numpy_array,axis=1)

mouse_numpy_array = np.loadtxt("allen_data/dev_mouse/mouse_numpy_array.txt")
mouse_averages = np.mean(mouse_numpy_array,axis=1)

sns.set(color_codes=True)
sns.set_style("white")
plt.figure(figsize=(20, 10))

sns.regplot(x=human_averages,y=mouse_averages,logx=True,truncate=True)

print(spearman_rho(human_averages,mouse_averages))

plt.show()
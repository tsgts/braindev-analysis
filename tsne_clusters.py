import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

data = np.loadtxt('allen_data/dev_human/tsne/tsne_9000.txt')

sns.set_style("white")
print(data.shape)

sns.jointplot(x=data[0],y=data[1],kind="hex", gridsize=30, color="#c0392b",stat_func=None)
plt.savefig("figures/dev_human/tsne/hexplot.png", dpi = 256)
plt.close()

sns.jointplot(x=data[0],y=data[1],kind="kde", color="g", n_levels=10,stat_func=None)
plt.savefig("figures/dev_human/tsne/contour.png", dpi = 256)
plt.close()

sns.jointplot(x=data[0],y=data[1],color="black", marker="x",s=16,stat_func=None,marginal_kws=dict(bins=50))
plt.savefig("figures/dev_human/tsne/scatter_contour.png", dpi = 256)
plt.close()
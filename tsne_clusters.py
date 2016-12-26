import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

data = np.loadtxt('allen_data/dev_mouse/tsne.txt')

print(data.shape)

sns.jointplot(x=data[0],y=data[1],kind="hex", gridsize=30, color="#c0392b",stat_func=None)
plt.savefig("figures/dev_mouse/tsne/hexplot.png", dpi = 256)
plt.close()

sns.jointplot(x=data[0],y=data[1],kind="kde", color="g", n_levels=25,stat_func=None)
plt.savefig("figures/dev_mouse/tsne/contour.png", dpi = 256)
plt.close()

sns.jointplot(x=data[0],y=data[1],color="r", marker="+",s=16,stat_func=None)
plt.savefig("figures/dev_mouse/tsne/scatter_contour.png", dpi = 256)
plt.close()
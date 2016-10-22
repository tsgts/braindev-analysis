import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

np.random.seed(0)
sns.set()
flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
print(flights)
ax = sns.heatmap(flights, center=300)
plt.show()
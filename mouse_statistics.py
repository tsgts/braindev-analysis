import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

expression_data = pd.read_csv("allen_data/dev_mouse/devmouse_histogram_values.csv")

def safe_log(x):
	x = float(x)
	if x<=0:
		return 0
	else:
   		return math.log10(x)

expression_data["RSP"] = expression_data["RSP"].apply(safe_log)
expression_data["Tel"] = expression_data["Tel"].apply(safe_log)

sns.set(color_codes=True)
#sns.distplot(expression_data["RSP"], kde=False, rug=False)
sns.regplot(x="RSP", y="Tel", data=expression_data)
plt.show()

import pandas as pd
import json

data = pd.read_csv('allen_data/organoid/organoid.txt',sep="\t")

data.to_csv("allen_data/organoid/organoid.csv",sep=',', encoding='utf-8')
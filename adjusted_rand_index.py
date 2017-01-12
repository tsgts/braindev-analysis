import json
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics.cluster import adjusted_mutual_info_score
import random

with open('allen_data/dev_mouse/tsne_colors.txt') as data_file:    
    mouse_labels = json.load(data_file)

with open('allen_data/dev_human/tsne_colors.txt') as data_file:    
    human_labels = json.load(data_file)

#random.shuffle(human_labels)

print(adjusted_rand_score(mouse_labels,human_labels))
print(adjusted_mutual_info_score(mouse_labels,human_labels))
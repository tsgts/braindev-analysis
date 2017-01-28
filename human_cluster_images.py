import numpy as np
import matplotlib.pyplot as plt

#with human coordinates
# coords = np.transpose(np.loadtxt('allen_data/dev_human/tsne/tsne_9000.txt'))

#with mouse coordinates
coords = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne.txt'))

min_1 = coords[:,0].min()
max_1 = coords[:,0].max()
min_2 = coords[:,1].min()
max_2 = coords[:,1].max()
coords_n = coords[:]
coords_n[:,0] = (coords[:,0] - min_1) / (max_1 - min_1) 
coords_n[:,1] = (coords[:,1] - min_2) / (max_2 - min_2) 

imgs = np.loadtxt('allen_data/dev_human/human_numpy_array.txt')
imgs = imgs.reshape(1912, 15, 10)

RES = 600
can = np.zeros((RES+2,RES+2))
can.fill(100)

def pad2d(vector, pad_width, iaxis, kwargs):
	vector[:pad_width[0]] = -100
	vector[-pad_width[1]:] = -100
	return vector

for i in range(1912):
	print(i)
	y_1 = int(coords_n[i][0] * (RES - 10))
	y_2 = int(coords_n[i][1] * (RES - 15))
	can[y_1:y_1+10+2,y_2:y_2+15+2] = np.rot90(np.lib.pad(imgs[i], 1, pad2d))

can = np.ma.masked_where(can == 100, can)
cmap = plt.cm.jet
cmap.set_bad(color='white')

cmap.set_under(color='black')

plt.imshow(np.rot90(can), interpolation='none',cmap=cmap,vmin=-11,vmax=10)
plt.axis('off')
#with human coordinates
# plt.savefig("figures/dev_human/raw_scatter/scatter_"+str(RES)+".png",dpi=RES)

#with mouse coordinates
plt.savefig("figures/comparison/raw_scatter/mouse_coords_"+str(RES)+".png",dpi=RES)
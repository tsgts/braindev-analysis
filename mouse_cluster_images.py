import numpy as np
import matplotlib.pyplot as plt

coords = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne/tsne_0.txt'))

min_1 = coords[:,0].min()
max_1 = coords[:,0].max()
min_2 = coords[:,1].min()
max_2 = coords[:,1].max()
coords_n = coords[:]
coords_n[:,0] = (coords[:,0] - min_1) / (max_1 - min_1) 
coords_n[:,1] = (coords[:,1] - min_2) / (max_2 - min_2) 

imgs = np.loadtxt('allen_data/dev_mouse/mouse_numpy_array.txt')
imgs = imgs.reshape(1912, 7, 11)

RES = 500
can = np.zeros((RES,RES))
can.fill(-100)

for i in range(1912):
	print(i)
	y_1 = int(coords_n[i][0] * (RES - 7))
	y_2 = int(coords_n[i][1] * (RES - 11))
	can[y_1:y_1+7,y_2:y_2+11] = imgs[i]

can = np.ma.masked_where(can == -100, can)
cmap = plt.cm.jet
cmap.set_bad(color='white')

plt.imshow(can, interpolation='none',cmap=cmap)
plt.show()
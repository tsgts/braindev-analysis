import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import json

with open('allen_data/dev_mouse/tsne_colors.txt') as data_file:    
    labels = json.load(data_file)

mouse = np.loadtxt('allen_data/dev_mouse/tsne.txt')

mouse_x = mouse[0]
mouse_y = mouse[1]

human = np.loadtxt('allen_data/dev_human/tsne.txt')

human_x = human[0]
human_y = human[1]

#===========LINES===============

# for j in range(0,15):
# 	fig = plt.figure(figsize=(60,20))
# 	ax1 = fig.add_subplot(121)
# 	ax2 = fig.add_subplot(122)
# 	ax1.plot(mouse_x,mouse_y,'ko')
# 	ax2.plot(human_x,human_y,'ko')
# 	for i in range(0,1912):
# 		if labels[i] == j:
# 			transFigure = fig.transFigure.inverted()

# 			coord1 = transFigure.transform(ax1.transData.transform([mouse_x[i],mouse_y[i]]))
# 			coord2 = transFigure.transform(ax2.transData.transform([human_x[i],human_y[i]]))


# 			line = matplotlib.lines.Line2D((coord1[0],coord2[0]),(coord1[1],coord2[1]),
# 			                               transform=fig.transFigure)
# 			fig.lines += line

# 			ax1.plot(mouse_x[i],mouse_y[i],'ro',markersize=4)
# 			ax2.plot(human_x[i],human_y[i],'ro',markersize=4)

# 	plt.savefig('figures/comparison/paired_plots/correspondence_' + str(j) + '.png')
# 	fig.clear()

#===========NO LINES===============

for j in range(0,15):
	fig = plt.figure(figsize=(60,20))
	ax1 = fig.add_subplot(121)
	ax2 = fig.add_subplot(122)
	ax1.plot(mouse_x,mouse_y,'ko')
	ax2.plot(human_x,human_y,'ko')
	for i in range(0,1912):
		if labels[i] == j:
			transFigure = fig.transFigure.inverted()

			coord1 = transFigure.transform(ax1.transData.transform([mouse_x[i],mouse_y[i]]))
			coord2 = transFigure.transform(ax2.transData.transform([human_x[i],human_y[i]]))


			# line = matplotlib.lines.Line2D((coord1[0],coord2[0]),(coord1[1],coord2[1]),
			#                                transform=fig.transFigure)
			# fig.lines += line

			ax1.plot(mouse_x[i],mouse_y[i],'ro',markersize=12)
			ax2.plot(human_x[i],human_y[i],'ro',markersize=12)

	plt.savefig('figures/comparison/paired_plots/correspondence_nolines_' + str(j) + '.png')
	fig.clear()
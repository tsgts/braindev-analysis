import numpy as np

data = np.loadtxt("allen_data/dev_human/human_numpy_array.txt")

data = data.reshape(1912,15,10)

cropped = []

for i in data:
	cropped.append(i[[0,1,2,3,5,6,9,14]])

print(np.array(cropped).shape)

cropped = np.array(cropped)

np.savetxt('allen_data/dev_human/human_cropped_numpy_array.txt', cropped.reshape(1912,80))
import numpy as np
import matplotlib.pyplot as plt
import json

with open('allen_data/dev_mouse/raw_dictionary_no_days.txt') as data_file:    
    data = json.load(data_file)
    matrix_array = np.array(list(data.values()),np.float32)
    print(matrix_array.shape)
    print(matrix_array)
    matrix_array = np.reshape(matrix_array,(2012,77))
    np.savetxt('allen_data/dev_mouse/mouse_numpy_array.txt', matrix_array)

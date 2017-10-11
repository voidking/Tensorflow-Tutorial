import tensorflow as tf
import numpy as np

x_data = np.linspace(-1,1,300)

print(x_data)
print(x_data[np.newaxis,:])
print(x_data[:,np.newaxis])
print(np.transpose(x_data))
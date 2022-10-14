import numpy as np
import matplotlib.pyplot as plt
import neurolab as nl

# Load input data
try:
    text = np.loadtxt('Forelesninger\data_simple_nn.txt')
except IOError as e:
    print(e)
    print('Necessary file data_simple_nn.txt is not found in the directory')

# Separate data and labels
data = text[:, 0:2]
labels = text[:, 2:]

# Plot input data
plt.figure()
plt.scatter(data[:,0], data[:,1])
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.title('Input data')
plt.show()

# Define minimum and maximum values and number of values for each dimension
dim1_min, dim1_max = data[:,0].min(), data[:,0].max()
dim2_min, dim2_max = data[:,1].min(), data[:,1].max()
num_output = labels.shape[1]

# Define a multilayer neural network with 2 hidden layers
dim1 = [dim1_min, dim1_max]
dim2 = [dim2_min, dim2_max]
nn = nl.net.newp([dim1, dim2],num_output)

# Train the neural network
error_progress = nn.train(data, labels, epochs=100, show=20,lr=0.03)

# Plot the training progress
plt.figure()
plt.plot(error_progress)
plt.xlabel('Number of epochs')
plt.ylabel('Training error')
plt.title('Training error progress')
plt.grid()
plt.show()

# Test the neural network
print('Testing on unknown data:')
data_test = [[0.4, 4.3], [4.4, 0.6], [4.7,8.1]]
for item in data_test:
    print(item, '-->', nn.sim([item])[0])
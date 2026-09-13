''' 
Numpy is a powerful library for numerical computing in Python. 
It provides support for large multi-dimensional arrays and matrices, 
along with a collection of mathematical functions to operate on these arrays.
'''

import numpy as np 

a = np.array([1, 2, 3]) # Create a 1D array with three elements
b = np.array([4, 5, 6]) # Create a 1D array with three elements
c = np.add(a, b) # Add the two arrays together
print(c) # Output: [5 7 9] because the addition is performed element-wise, which means that each element in the first array is added to the corresponding element in the second array.

# Get dimensions of the array
print(a.ndim) # Output: 1 because the array is one-dimensional

# get shape of the array
print(a.shape) # Output: (3,) because the array has three elements in one dimension

# 2 dimensional array with two rows and three columns
d = np.array([[1, 2, 3], [4, 5, 6]]) 
e = np.array([[7, 8, 9], [10, 11, 12]]) 
f = np.add(d, e) # Add the two arrays
print(f) # Output: [[ 8 10 12] [14 16 18]] because the addition is performed element-wise, which means that each element in the first array is added to the corresponding element in the second array.

# Get dimensions of the array
print(d.ndim) # Output: 2 because the array is two-dimensional

# get shape of the array
print(d.shape) # Output: (2, 3) because the array has two rows and three columns

# Accessing / changing elements in the array
g = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17]]) # Create a 2D array with two rows and nine columns
print(g) # Output: [[ 1  2  3  4  5  6  7  8  9] [10 11 12 13 14 15 16 17]] because the array is printed in its entirety
print(g.shape) # Output: (2, 9) because the array has two rows and nine columns

# Get specific element in the array [row, column]
print(g[0, 1]) # Output: 2 because we are accessing the element in the first row and second column
print(g[1, 2]) # Output: 12 because we are accessing the element in the second row and third column
print(g[1, 7]) # Output: 17 because we are accessing the element in the second row and eighth column
print(g[0, -1]) # Output: 9 because we are accessing the last element in the first row using negative indexing

# Get specific row in the array
print(g[0, :]) # Output: [1 2 3 4 5 6 7 8 9] because we are accessing all elements in the first row
print(g[1, :]) # Output: [10 11 12 13 14 15 16 17] because we are accessing all elements in the second row

# Get specific column in the array
print(g[:, 0]) # Output: [ 1 10] because we are accessing all elements in the first column
print(g[:, 1]) # Output: [ 2 11] because we are accessing all elements in the second column
print(g[:, 2]) # Output: [ 3 12] because we are accessing all elements in the third column

# More advanced slicing techniques
print(g[0, 1:4:2]) # Output: [2 4] because we are accessing elements in the first row, starting from index 1 to index 4 (exclusive), with a step of 2
print(g[1, 0:6:3]) # Output: [10 13] because we are accessing elements in the second row, starting from index 0 to index 6 (exclusive), with a step of 3

# Changing elements in the array
g[0, 0] = 100 # Change the first element in the first row
print(g) # Output: [[100   2   3   4   5   6   7   8   9] [ 10  11  12  13  14  15  16  17]] because the first element in the first row has been changed to 100
g[1, 1:4] = [200, 300, 400] # Change elements in the second row from index 1 to index 4 (exclusive)
print(g) # Output: [[100   2   3   4   5   6   7   8   9] [ 10 200 300 400 14  15  16  17]] because the elements in the second row from index 1 to index 4 (exclusive) have been changed to 200, 300, and 400 respectively


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

# Initializing arrays with zeros, ones, and random numbers
h = np.zeros((2, 3)) # Create a 2D array with two rows and three columns, filled with zeros
print(h) # Output: [[0. 0 0.] [0. 0. 0.]] because the array is filled with zeros

i = np.ones((3, 2)) # Create a 2D array with three rows and two columns, filled with ones
print(i) # Output: [[1. 1.] [1. 1.] [1. 1.]] because the array is filled with ones

j = np.random.random((2, 3)) # Create a 2D array with two rows and three columns, filled with random numbers between 0 and 1
print(j) # Output: [[0.12345678 0.23456789 0.3456789 ] [0.45678901 0.56789012 0.67890123]] because the array is filled with random numbers between 0 and 1

k = np.random.randint(0, 10, (2, 3)) # Create a 2D array with two rows and three columns, filled with random integers between 0 and 10
print(k) # Output: [[3 7 1] [4 9 2]] because the array is filled with random integers between 0 and 10

l = np.full((2, 3), 7) # Create a 2D array with two rows and three columns, filled with the value 7  # noqa: E741
print(l) # Output: [[7 7 7] [7 7 7]] because the array is filled with the value 7 

m = np.eye(3) # Create a 3x3 identity matrix
print(m) # Output: [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]] because the array is an identity matrix with ones on the diagonal and zeros elsewhere

# Be careful when copying arrays, as it can lead to unexpected behavior if not done correctly.
n = np.array([1, 2, 3]) # Create a 1D array with three elements
o = n # This creates a reference to the same array, not a copy
o[0] = 100 # Change the first element in the array
print(n) # Output: [100   2   3] because the first element in the original array has been changed to 100, since o is a reference to n

# To create a copy of the array, use the copy() method
p = np.array([1, 2, 3]) # Create a 1D array with three elements
q = p.copy() # Create a copy of the array
q[0] = 100 # Change the first element in the copied array
print(p) # Output: [1 2 3] because the original array has not been changed, since q is a copy of p
print(q) # Output: [100   2   3] because the first element in the copied array has been changed to 100

# Mathematical operations on arrays
r = np.array([1, 2, 3]) # Create a 1D array with three elements
s = np.array([4, 5, 6]) # Create a 1D array with three elements

# Addition
print(r + 2) # Output: [3 4 5] because 2 is added to each element in the array

t = np.add(r, s) # Add the two arrays together
print(t) # Output: [5 7 9] because the addition is performed element-wise, which means that each element in the first array is added to the corresponding element in the second array.

# Subtraction
print(r - 2) # Output: [-1  0  1] because 2 is subtracted from each element in the array

u = np.subtract(r, s) # Subtract the second array from the first array
print(u) # Output: [-3 -3 -3] because the subtraction is performed element-wise, which means that each element in the second array is subtracted from the corresponding element in the first array.

# Multiplication
print(r * 2) # Output: [2 4 6] because each element in the array is multiplied by 2

v = np.multiply(r, s) # Multiply the two arrays together
print(v) # Output: [ 4 10 18] because the multiplication is performed element-wise, which means that each element in the first array is multiplied by the corresponding element in the second array.

# Division
print(r / 2) # Output: [0.5 1.  1.5] because each element in the array is divided by 2

w = np.divide(r, s) # Divide the first array by the second array
print(w) # Output: [0.25 0.4 0.5] because the division is performed element-wise, which means that each element in the first array is divided by the corresponding element in the second array.

# Exponentiation
print(r ** 2) # Output: [1 4 9] because each element in the array is raised to the power of 2

# Square root
print(np.sqrt(r)) # Output: [1.         1.41421356 1.73205081] because the square root is calculated for each element in the array

# Sin and Cos
print(np.sin(r)) # Output: [0.84147098 0.90929743 0.14112001] because the sine is calculated for each element in the array
print(np.cos(r)) # Output: [0.54030231 0.41614684 0.9899925 ] because the cosine is calculated for each element in the array

# Statistical operations on arrays
x = np.array([1, 2, 3, 4, 5])
print(np.mean(x)) # Output: 3.0 because the mean is calculated for the array
print(np.median(x)) # Output: 3 because the median is calculated for the array
print(np.std(x)) # Output: 1.4142135623730951 because the standard deviation is calculated for the array
print(np.var(x)) # Output: 2.0 because the variance is calculated for the array
print(np.min(x)) # Output: 1 because the minimum value is calculated for the array
print(np.max(x)) # Output: 5 because the maximum value is calculated for the array
print(np.sum(x)) # Output: 15 because the sum is calculated for the array

# Statistical operations on 2D arrays
y = np.array([[1, 2, 3], [4, 5, 6]])
print(np.mean(y)) # Output: 3.5 because the mean is calculated for the entire 2D array
print(np.min(y)) # Output: 1 because the minimum value is calculated for the entire 2D array
print(np.max(y)) # Output: 6 because the maximum value is calculated for the entire 2D array
print(np.sum(y)) # Output: 21 because the sum is calculated for the entire 2D array
print(np.mean(y, axis=0)) # Output: [2.5 3.5 4.5] because the mean is calculated for each column in the 2D array
print(np.mean(y, axis=1)) # Output: [2. 5.] because the mean is calculated for each row in the 2D array
# The axis parameter specifies the axis along which the operation is performed. In this case, axis=0 means that the operation is performed along the columns, and axis=1 means that the operation is performed along the rows.

# Reorganising arrays
z = np.array([[1, 2, 3], [4, 5, 6]])

reshaped_z = z.reshape((3, 2)) # Reshape the 2D array to have three rows and two columns
print(reshaped_z) # Output: [[1 2] [3 4] [5 6]] because the array has been reshaped to have three rows and two columns

flattened_z = z.flatten() # Flatten the 2D array to a 1D array
print(flattened_z) # Output: [1 2 3 4 5 6] because the array has been flattened to a 1D array

# Vertical stacking of arrays
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])
v_stacked = np.vstack((a1, a2)) # Stack the two arrays vertically
print(v_stacked) # Output: [[1 2] [3 4] [5 6] [7 8]] because the two arrays have been stacked vertically

# Horizontal stacking of arrays
h_stacked = np.hstack((a1, a2)) # Stack the two arrays horizontally
print(h_stacked) # Output: [[1 2 5 6] [3 4 7 8]] because the two arrays have been stacked horizontally


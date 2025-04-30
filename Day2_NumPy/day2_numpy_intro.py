import numpy as np

# Create a 1D array
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

print("1D Array:", a)
print("2D Array:\n", b)

# 2. Array Operations
print("Array sum:", np.sum(a))
print("Array mean:", np.mean(a))
print("Element-wise addition:", a + 2)

# 3. Array Shape and Reshape
print("Shape of b:", b.shape)
b_reshaped = b.reshape(4, 1)
print("Reshaped:\n", b_reshaped)

# 4. Random Numbers
rand_arr = np.random.rand(3, 2)
print("Random Array:\n", rand_arr)

# 5. Matrix Multiplication
x = np.array([[1, 2], [3, 4]])
y = np.array([[2, 0], [1, 2]])
print("Matrix product:\n", np.dot(x, y))

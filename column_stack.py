import numpy as np

# Two separate 1D arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stack them as columns
result = np.column_stack((a, b))

print(result)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]


import numpy as np

matrix_a = np.array([[1, 2], 
                     [3, 4]])
matrix_b = np.array([[5], 
                     [6]])

result = np.column_stack((matrix_a, matrix_b))

print(result)
# Output:
# [[1 2 5]
#  [3 4 6]]

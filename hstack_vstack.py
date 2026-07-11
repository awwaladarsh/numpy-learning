import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.hstack((a, b))

print(result)
# Output: [1 2 3 4 5 6]


import numpy as np

matrix_a = np.array([[1, 2], 
                     [3, 4]])

matrix_b = np.array([[5], 
                     [6]])

result = np.hstack((matrix_a, matrix_b))

print(result)
# Output:
# [[1 2 5]
#  [3 4 6]]


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.vstack((a, b))

print(result)
# Output:
# [[1 2 3]
#  [4 5 6]]


import numpy as np

matrix_a = np.array([[1, 2], 
                     [3, 4]])

matrix_b = np.array([[5, 6]])

result = np.vstack((matrix_a, matrix_b))

print(result)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

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

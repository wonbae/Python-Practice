import numpy as np

x = np.array([[1, 1], [2, 1]])
res = np.array([15, 25])

# print(np.sum(x, axis=0))
y = abs(x[0] - x[1])
z = abs(res[0] - res[1])

p = np.linalg.inv(x)

a = p * res

# print(a)
# print(np.sum(a, axis=0)
print(np.sum(a) )
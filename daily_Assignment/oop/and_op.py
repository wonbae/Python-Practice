import numpy as np


def f(para):
    para = para.flatten()
    tmp = 0
    for val in para:
        if val < tmp:
            return 0
        else:
            return val


W = np.array([1, 1])
b = -1

x1 = np.array([0, 0])
x2 = np.array([0, 1])
x3 = np.array([1, 0])
x4 = np.array([1, 1])

print(f(W.dot(x1) + b))
print(f(W.dot(x2) + b))
print(f(W.dot(x3) + b))
print(f(W.dot(x4) + b))

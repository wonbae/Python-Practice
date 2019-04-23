# import numpy as np
#
# x = np.array([[1,2], [3,4]], dtype=np.float64)
# y = np.array([[1,2], [3,4]], dtype=np.float64)
#
# print(x + y)
# print(np.add(x,y))
# print('-------')
#
# print(x - y)
# print(np.subtract(x,y))
# print('-------')
#
#
# print(x * y)
# print(np.multiply(x, y))
# print('-------')
#
#
# print(x / y)
# print(np.divide(x, y))
# print('-------')
#
# print(np.sqrt(x))


# 2.Dot Product
import numpy as np

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

v = np.array([9, 10])
w = np.array([11, 12])

print(v.dot(w))
print(np.dot(v, w))

#매트릭스 / 벡터 곱
print(x.dot(v))
print(np.dot(x, v))


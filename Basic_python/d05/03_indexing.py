# import numpy as np
# # 1)
# # 2차원 배열(3x2) 생성
# # [[ 1 2]
# # [ 3 4]
# # [ 5 6]]
# a = np.array([[1, 2], [3, 4], [5, 6]])
# # [1 4 5] 1차원 행렬(3,)을 얻는 두 가지 방법
# print(a[[0, 1, 2], [0, 1, 0]])  #앞에꺼는 행, 뒤에껀 열
# print(np.array([a[0, 0], a[1, 1], a[2, 0]]))
# # [2 2] 1차원 행렬(2,)을 얻는 두 가지 방법
# print(a[[0, 0], [1, 1]])
# print(np.array([a[0, 1], a[0, 1]]))


# 2)
import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)

b = np.array([0,2,0,1])
print(a[np.arange(4)])
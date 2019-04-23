import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
y = np.empty_like(x)

# 1. for 사용
# for i in range(4):
#     y[i, :] = x[i, :] + v

# 2. tile 사용
# xx = np.tile(v, (4,1)) #각 행에 대해서 반복

# 3. 그냥 브로드캐스팅 사용
y = x + v

print(y)
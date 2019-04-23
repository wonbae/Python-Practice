import numpy as np

a = np.zeros((2,2))
print(a, end='\n\n')

b = np.ones((1,2))
print(b, end='\n\n')

c = np.full((2,2), 7)
print(c, end='\n\n')

d = np.eye(2)
print(d, end='\n\n')

e = np.random.random((2,2))
print(e)
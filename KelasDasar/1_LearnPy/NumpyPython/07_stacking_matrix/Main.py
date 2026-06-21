import numpy as np


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a)
print(b)

aMat = np.zeros((2, 3))
bMat = np.zeros((2, 3))

print(aMat)
print(bMat)

# stacking matrix, menumpuk matrix

c = np.hstack((a, b))
d = np.vstack((a, b))

print(c)
print(d)

cMat = np.hstack((aMat, bMat))
dMat = np.vstack((aMat, bMat))

print(cMat)
print(dMat)
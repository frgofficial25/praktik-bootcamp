import numpy as np

a = np.array([
            (1, 2, 3),
            (4, 5, 6)
            ])

print('matrix a dengan ukuran:', a.shape)
print(a)

# transpose matrix
print('transpose dari matrix a:')
print(a.transpose())
print(np.transpose(a))
print(a.T)
print('matrix a transpose dengan ukuran:', a.T.shape)

# flatten array, vector baris
print('flatten matrix a:')
print(a.ravel())
print(np.ravel(a))
print('matrix a flatten dengan ukuran:', a.ravel().shape)

# reshape matrix
print('reshape matrix a:')
print(a.reshape(3, 2))
print('matrix a reshape dengan ukuran:', a.reshape(3, 2).shape)

# resize matrix
print('resize matrix a:')
a.resize(3, 2)
print(a)
print('matrix a dengan ukuran:', a.shape)
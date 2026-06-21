import numpy as np

# membuat vector
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.5, 2.5, 5, 6, 7])

print(a)
print(b)

# membuat vector dengan range
c = np.arange(1, 10, 2)

print(c)

# membuat linspace
d = np.linspace(1, 10, 4)

print(d)

# array multidimensi / matrix
e = np.array([(1, 2, 3), (4, 5, 6)])

print(e)

# matrix dengan nilai nol
f = np.zeros((5, 5))

print(f)

# matrix dengan nilai satu
g = np.ones((5, 5))

print(g)

# matrix identitas
h1 = np.identity(5)
h2 = np.eye(5)

print(h1)
print(h2)
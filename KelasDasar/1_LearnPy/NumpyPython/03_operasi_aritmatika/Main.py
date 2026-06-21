import numpy as np

# list python
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

# array numpy
anp = np.array([1, 2, 3, 4, 5])
bnp = np.array([6, 7, 8, 9, 10])

# ELEMENTWISE operation
#penjumlahan
hasil = anp + bnp
print(hasil)

# pengurangan
hasil = anp - bnp
print(hasil)

# perkalian
hasil = anp * bnp
print(hasil)

# pembagian
hasil = anp / bnp
print(hasil)

# kuadrat
hasil = anp**2
print(hasil)

# multidimensi array numpy

c = np.array([(1, 2, 3), (4, 5, 6)])
d = np.array([(7, 8, 9), (-1, -2, -3)])

hasil = c + d
print(hasil)
hasil = c * d
print(hasil)
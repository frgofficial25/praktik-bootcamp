import numpy as np

# membuat matrix dengan tipe data tertentu
a = np.array([(1, 2, 3), (4, 5, 6)], dtype=float)

print(a)

# membuat array baru menggunakan function

def kuadrat(baris, kolom) :
    return kolom**2

def jumlah(baris, kolom) :
    return (kolom + baris)

b = np.fromfunction(kuadrat, (1, 10), dtype=int)
c = np.fromfunction(jumlah, (4, 4), dtype=float)

print(b)
print(c)

# membuat array atau matrix dengan menggunakan iterable

iterable = (x*2 for x in range(5))

d = np.fromiter(iterable, dtype=int)

print(d)

# multitype array

dtipe = [('nama', 'S255'), ('tinggi', int)]

data = [
    ('ucup', 150),
    ('otong', 160),
    ('mario', 180)
]

e = np.array(data, dtype=dtipe)

print(e)
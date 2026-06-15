import numpy as np

# Perbedaan List Python dan Array NumPy
list_a = [1, 2, 3, 4]
vector_a = np.array([1, 2, 3, 4])

print(f"list_a   = {list_a}")
# print(list_a**2) # Ini akan ERROR

print(f"vector_a = {vector_a}")
print(f"vector_a pangkat 2 = {vector_a**2}")
print(f"vector_a kali 5    = {vector_a*5}")

# Membuat Matriks 2D
matrix_b = np.array([(1, 2), (3, 4)])
print(f"\nmatrix_b : \n{matrix_b}")
print(f"matrix_b pangkat 2 : \n{matrix_b**2}")

# Membuat Matriks Nol (Zeros)
zeros_c = np.zeros((2, 2))
print(f"\nzeros_c : \n{zeros_c}")

# Membuat Matriks Satu (Ones)
ones_d = np.ones((2, 2))
print(f"\nones_d : \n{ones_d}")

# Operasi antar Matriks
jumlah = matrix_b + matrix_b**2 + ones_d
print(f"\nHasil penjumlahan matriks: \n{jumlah}")
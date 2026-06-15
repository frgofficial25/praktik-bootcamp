# List
# Menggunakan kurung siku []
data_list = [1, 2, 10, 2, 3]
print(f"data list = {data_list}")

# Tuples
# Menggunakan kurung biasa ()
data_tuples = (7, 8, 9, 10)
print(f"data tuples = {data_tuples}")

# Mengakses data tuples
print(f"data tuples index ke-1 = {data_tuples[1]}")

# Tuples tidak bisa dirubah isinya (assignment tidak didukung)
# data_tuples[1] = "Ucup" <-- Ini akan menghasilkan ERROR
# data_tuples.append(1)  <-- Ini juga akan menghasilkan ERROR

# Sets (Himpunan)
# Menggunakan kurung kurawal {}
data_sets = {10, 1, 4, 12, 4, 3}
print(f"data sets = {data_sets}")

# Sets tidak memiliki indeks
# print(data_sets[0]) <-- Ini akan menghasilkan ERROR karena tidak ada urutan tetap
# Operasi pada List

data_angka = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]
print(f"data angka = \n{data_angka}")

# 1. Count data (menghitung jumlah munculnya data)
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# 2. Ambil posisi data (index)
data = ["Ucup", "Otong", "Dudung", "Ujang"]
print(f"data = {data}")

index_dudung = data.index("Dudung")
index_ujang = data.index("Ujang")
print(f"index si Dudung = {index_dudung}")
print(f"index si Ujang = {index_ujang}")

# 3. Mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka setelah sort = \n{data_angka}")

print(f"data string sebelum sort = {data}")
data.sort()
print(f"data string setelah sort = {data}")

# 4. Membalik urutan list (reverse)
data_angka.reverse()
data.reverse()
print(f"data angka setelah reverse = \n{data_angka}")
print(f"data string setelah reverse = {data}")
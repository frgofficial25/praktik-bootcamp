# Operasi Manipulasi List

# Index  0 ( -3 )  1 ( -2 )  2 ( -1 )
data = ["Ucup", "Otong", "Dudung"]

# 1. Mengambil data dari list
data_0 = data[0]
print(f"data pertama (indeks 0): {data_0}")

data_terakhir = data[-1]
print(f"data terakhir: {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup: {data_ucup}")

# 2. Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data: {panjang_data}")

## Manipulasi Data List

# 3. Menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah: \n{data}")

data.insert(1, "Asep")
print(f"data sesudah ditambah (insert): \n{data}")

# 4. Menambah di akhir list
data.append("Jejeng")
print(f"data sesudah ditambah (append): \n{data}")

# 5. Menambahkan list dengan list (gabung)
data_baru = ["Yujeng", "Usep", "Dadang"]
data.extend(data_baru)
print(f"data gabungan: \n{data}")

# 6. Merubah data
# kita ubah indeks 2 (Otong) menjadi Michael
data[2] = "Michael"
print(f"data rubah: \n{data}")

# 7. Meremove data
data.remove("Yujeng")
print(f"data remove (Yujeng): \n{data}")
# data.remove("usep") # akan error karena huruf kecil-besar berpengaruh

# 8. Meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir yang dihapus: {data_akhir}")
print(f"data hasil pop: \n{data}")
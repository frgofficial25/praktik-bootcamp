# Nested List / List Bersarang

data_0 = [1, 2]
data_1 = [3, 4, 5]

data_list_biasa = [1, 2, 3, 4]
print(f"list biasa = {data_list_biasa}")

# Membuat List 2 Dimensi (Nested List)
list_2D = [data_0, data_1, 6, 7]
print(f"list 2D = {list_2D}")

# Contoh penggunaan praktis: Data Peserta
peserta_0 = ["Ucup", 25, "Laki-laki"]
peserta_1 = ["Otong", 10, "Laki-laki"]
peserta_2 = ["Dedeh", 50, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = \n{list_peserta}")

# Menampilkan data menggunakan looping
for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")

# Masalah dengan reference pada nested list
list_copy = list_peserta.copy()
print(f"list copy = \n{list_copy}")

# Kita coba ubah salah satu data di dalam nested list
peserta_0[0] = "Michael"
print(f"peserta asli = \n{list_peserta}")
print(f"peserta copy = \n{list_copy}") # Ikut berubah menjadi Michael!
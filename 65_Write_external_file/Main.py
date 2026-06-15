# Belajar Menulis File Eksternal

# 1. Mode Write (w) -> Menghapus isi lama, ganti baru
with open("C:\\BasicPython\\65_Write_external_file\\data_1.txt", mode="w", encoding="utf-8") as file :
    file.write("John Si Joni")

with open("C:\\BasicPython\\65_Write_external_file\\data_1.txt", mode="w", encoding="utf-8") as file :
    file.write("Ucup Surucup") # "John Si Joni" akan terhapus

#2 Mode Append (a) -> Menambah di akhir
with open("C:\\BasicPython\\65_Write_external_file\\data_2.txt", mode="w", encoding="utf-8") as file :
    file.write("Ucup Surucup\n")

with open("C:\\BasicPython\\65_Write_external_file\\data_2.txt", mode="a", encoding="utf-8") as file :
    file.write("Otong Surotong\n")
    file.write("Tambah lagi dengan append\n")

# 3 Mode r+ (Read and Write)
# Membuat file awal dulu
with open("C:\\BasicPython\\65_Write_external_file\\data_3.txt", mode="w", encoding="utf-8") as file :
    file.write("baris ke-1\n")
    file.write("baris ke-2\n")
    file.write("baris ke-3\n")

with open("C:\\BasicPython\\65_Write_external_file\\data_3.txt", mode="r+", encoding="utf-8") as file :
    file.write("Otong") # Akan menimpa "baris" menjadi "Otong"

with open("C:\\BasicPython\\65_Write_external_file\\data_3.txt", mode="r+", encoding="utf-8") as file :
    data = file.read()
    print(data)
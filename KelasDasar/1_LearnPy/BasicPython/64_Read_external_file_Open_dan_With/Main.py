## Membaca file eksternal - Open dan With

# 1. Cara Pertama: Menggunakan open()
print(3*"=", " Membaca file txt dengan open ", 3*"=")
file = open("data.txt", mode="r")

# Cek apakah file bisa dibaca atau ditulis
print(f"Status read  : {file.readable()}")
print(f"Status write : {file.writable()}")

# Membaca seluruh file
# print(file.read())

# Membaca per baris
print(file.readline(), end="") # Baris 1
print(file.readline(), end="") # Baris 2

# Membaca semua baris sebagai list
# print(file.readlines())

# Mengecek apakah file sudah ditutup
print(f"Apakah file sudah diclose : {file.closed}")
file.close()
print(f"Apakah file sudah diclose : {file.closed}")


# 2. Cara Kedua: Menggunakan with (Lebih Direkomendasikan)
print("\n" + 3*"=", " Membaca file txt dengan with ", 3*"=")

with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"Apakah file sudah diclose di dalam with : {file.closed}")

print(f"Apakah file sudah diclose di luar with : {file.closed}")
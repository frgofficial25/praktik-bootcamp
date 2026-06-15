# Contoh sederhana untuk menangkap Exception
input_user = int(input("masukkan angka: "))
hasil = 0

try:
    hasil = 10 / input_user
except:
    print("input tidak boleh 0")

print(f"hasil = {hasil}")

# Contoh di aplikasi menggunakan loop
while True:
    angka = int(input("masukkan angka pembagi: "))
    try:
        hasil = 10 / angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan (y/n)? ")
        if is_done == "n":
            break
    except:
        print("pembagi nol, silahkan masukkan input lagi")

print("akhir dari program 1")

# Contoh aplikasi membuka file
try:
    with open("data.txt", "r") as file:
        print(file.read())
except:
    print("file data tidak ditemukan, membuat file baru")
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("file baru")

print("akhir dari program 2")
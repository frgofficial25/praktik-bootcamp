import os

# Fungsi untuk menampilkan header
def header():
    os.system("cls") # Gunakan 'cls' untuk Windows
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

# Fungsi untuk mengambil input user
def input_user():
    lebar = int(input("Masukkan nilai lebar: "))
    panjang = int(input("Masukkan nilai panjang: "))
    return lebar, panjang

# Fungsi hitung luas
def hitung_luas(lebar, panjang):
    return lebar * panjang

# Fungsi hitung keliling
def hitung_keliling(lebar, panjang):
    return 2 * (lebar + panjang)

# Fungsi untuk menampilkan hasil
def display(message, value):
    print(f"Hasil perhitungan {message} = {value}")

# Program Utama (Main Program)
while True:
    header()
    
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    display("luas", LUAS)
    display("keliling", KELILING)

    print("\n")
    is_continue = input("Apakah lanjut (y/n)? ")
    if is_continue == "n":
        break

print("Program selesai, terima kasih!")
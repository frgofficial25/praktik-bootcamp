""" *args pada Fungsi """

# 1. Cara Standar (Posisional)
def fungsi_standar(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi_standar("Ucup", 170, 40)

# 2. Menggunakan List sebagai Input
def fungsi_list(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi_list(["Otong", 100, 120])

# 3. Menggunakan *args (Lebih Simpel dan Dinamis)
def fungsi_args(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi_args("Dudung", 120, 120)

# 4. Studi Kasus: Fungsi Tambah Dinamis
def tambah(*data):
    # data bertipe tuple, bisa di-iterasi
    output = 0
    for angka in data:
        output += angka
    return output

hasil = tambah(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Hasil tambah = {hasil}")

hasil = tambah(10, 5, 15)
print(f"Hasil tambah baru = {hasil}")
import datetime
import os
import string
import random

# Template dictionary mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,1)
}

data_mahasiswa = {}

while True:
    # Membersihkan terminal
    os.system("cls") # Gunakan 'cls' untuk Windows

    print(f"{'SELAMAT DATANG':^40}")
    print(f"{'DATA MAHASISWA':^40}")
    print("-" * 40)

    # Membuat dictionary mahasiswa baru berdasarkan template
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    # Input User
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    tahun_lahir = int(input("Tahun lahir (YYYY): "))
    bulan_lahir = int(input("Bulan lahir (1-12): "))
    tanggal_lahir = int(input("Tanggal lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)

    # Membuat Key Unik (6 karakter acak)
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    # Menampilkan Header Tabel
    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<10} {'SKS':<3} {'Lahir':<10}")
    print("-" * 52)

    # Looping untuk menampilkan semua data di database
    for mhs in data_mahasiswa:
        K = mhs
        NAMA = data_mahasiswa[K]['nama']
        NIM = data_mahasiswa[K]['nim']
        SKS = data_mahasiswa[K]['sks_lulus']
        LAHIR = data_mahasiswa[K]['lahir'].strftime("%x")

        print(f"{K:<6} {NAMA:<17} {NIM:<10} {SKS:<3} {LAHIR:<10}")

    print("\n")
    is_done = input("Mau tambah lagi bos? (y/n): ")
    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih!")
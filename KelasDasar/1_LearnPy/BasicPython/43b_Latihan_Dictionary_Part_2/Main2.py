import datetime
import os

# Template dictionary mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,1)
}

data_mahasiswa = {}
count = 0

while True :

    # Membersihkan terminal (Windows: 'cls', Linux/Mac: 'clear')
    os.system('cls')
    
    print(f"{'SELAMAT DATANG':^40}")
    print(f"{'DATA MAHASISWA':^40}")
    print("-" * 40)

    # Memformat keys
    count += 1
    format_keys = f"MHS{count}"

    # Membuat dictionary mahasiswa baru berdasarkan template
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    # Mengambil input dari user
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))

    tahun_lahir = int(input("Tahun lahir (YYYY): "))
    bulan_lahir = int(input("Bulan lahir (1-12): "))
    tanggal_lahir = int(input("Tanggal lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)

    # Menambahkan dict mahasiswa ke dict data_mahasiswa
    data_mahasiswa.update({format_keys : mahasiswa})

    # Menampilkan hasil input (untuk pengecekan sementara)
    print()
    # Membuat Header Tabel
    print(f"{'KEY':<6} {'Nama':<17} {'NIM':<10} {'SKS':<3} {'Lahir':<10}")
    print("-" * 50)
    
    # Looping untuk menampilkan data
    for items in data_mahasiswa :
        KEY = items
        Nama = data_mahasiswa[items]['nama']
        NIM = data_mahasiswa[items]['nim']
        SKS = data_mahasiswa[items]['sks_lulus']
        Lahir = data_mahasiswa[items]['lahir'].strftime("%x")
        print(f"{KEY:<6} {Nama:<17} {NIM:<10} {SKS:<3} {Lahir:<10}")

    check = input("\napakah ingin melanjutkan (y/n)? ")
    if (check == 'n') :
        print()
        break
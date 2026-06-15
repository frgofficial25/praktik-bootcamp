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

# Membersihkan terminal (Windows: 'cls', Linux/Mac: 'clear')
os.system('cls') 

print(f"{'SELAMAT DATANG':^40}")
print(f"{'DATA MAHASISWA':^40}")
print("-" * 40)

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

# Menampilkan hasil input (untuk pengecekan sementara)
print(f"\n{mahasiswa}")
""" Global dan Local Scope """

# 1. Variabel Global
nama_global = "Otong" # <- Variabel Global

def fungsi1():
    print(f"Fungsi menampilkan {nama_global}")

fungsi1()

# Akses dalam Loop
for i in range(0, 5):
    print(f"Loop ke-{i} - {nama_global}")

# Akses dalam Percabangan
if True:
    print(f"If menampilkan {nama_global}")

# 2. Variabel Lokal Scope
def fungsi2():
    nama_lokal = "Ucup" # <- Variabel Lokal

fungsi2()
# print(nama_lokal) # <- Akan ERROR: name 'nama_lokal' is not defined

# 3. Contoh Penggunaan dan Urutan Pemanggilan
# Pastikan variabel didefinisikan sebelum fungsi dipanggil
nama = "Otong"

def say_otong():
    print(f"Hello {nama}")

say_otong()

# 4. Merubah Variabel Global
angka = 0
name = "Ucup"

def ubah(nilai_baru, nama_baru):
    global angka # <- Memberikan akses ke variabel global 'angka'
    global name  # <- Memberikan akses ke variabel global 'name'
    angka = nilai_baru
    name = nama_baru

print(f"Sebelum: {angka}, {name}")
ubah(10, "Otong")
print(f"Sesudah: {angka}, {name}")

# 5. Perilaku pada For dan If (Bukan Scope Terpisah)
if True:
    angka_dummy = 10
    angka = 20

print(f"Angka dummy: {angka_dummy}") # Bisa diakses
print(f"Angka berubah: {angka}")      # Berubah langsung tanpa keyword global
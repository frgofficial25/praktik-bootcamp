import time

# Cara 1: Menggunakan import ke modul dalam package
import science.matematika

# Cara 2: Menggunakan from untuk mengambil modul
from science import fisika
from science.fisika import gaya as force

# Mengukur waktu eksekusi start
t_start = time.time()

# Penggunaan modul matematika
hasil_tambah = science.matematika.tambah(1, 2, 3, 4, 5)
print(f"Hasil tambah dari package = {hasil_tambah}")

# Penggunaan modul fisika
gaya_result = fisika.gaya(90, 10)
print(f"Gaya adalah = {gaya_result}")

# Penggunaan alias
f = force(90, 10)
print(f"Force alias adalah = {f}")

# Mengukur waktu eksekusi end
t_end = time.time()
print(f"Waktu eksekusi: {t_end - t_start} detik")
""" Membuat Module """

# 1. Cara Standar (Import seluruh modul)
import matematika

hasil_tambah = matematika.tambah(1, 2, 3, 4, 5)
print(f"Hasil tambah: {hasil_tambah}")

hasil_kali = matematika.kali(1, 2, 3, 4, 5)
print(f"Hasil kali: {hasil_kali}")

pangkat_3 = matematika.pangkat(3)
print(f"Hasil pangkat 3 dari 3: {pangkat_3(3)}")


# 2. Menggunakan 'from' (Import fungsi spesifik)
from matematika import tambah, kali
# Sekarang bisa dipanggil langsung tanpa 'matematika.'
print(f"Tambah (from): {tambah(10, 5)}")


# 3. Menggunakan Alias 'as'
from matematika import tambah as add
from matematika import kali as multiply
import matematika as math

print(f"Hasil add: {add(1, 1)}")
print(f"Hasil math.kali: {math.kali(2, 2)}")


# 4. Import Semua (Kurang direkomendasikan)
from matematika import *
print(f"Pangkat direct: {pangkat(2)(10)}")
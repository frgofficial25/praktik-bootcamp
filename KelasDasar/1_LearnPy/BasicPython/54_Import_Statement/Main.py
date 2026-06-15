""" Import Statement """

# 1. Menyambung program dari file eksternal
import program_print
import program_ucup

# 2. Import dengan data (menggunakan namespace)
import variabel
import kucuy

# Mengakses data menggunakan namespace (nama file)
print(variabel.data)
print(kucuy.data)

# 3. Import dengan fungsi
import matematika

hasil = matematika.tambah(4, 5)
print(f"Hasil tambah: {hasil}")
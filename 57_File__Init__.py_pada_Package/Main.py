import science

# Mengakses lewat namespace yang sudah disambung di __init__.py
hasil_tambah = science.matematika.tambah(1, 2, 3, 4, 5)
print(f"Hasil tambah: {hasil_tambah}")

hasil_fisika = science.fisika.gaya(10, 9.8)
print(f"Hasil fisika: {hasil_fisika}")

hasil_kali = science.matematika.kali(1, 2, 3)
print(f"Hasil kali: {hasil_kali}")

pangkat_3 = science.matematika.pangkat(3)
print(f"Hasil pangkat 3 dari 5: {pangkat_3(5)}")
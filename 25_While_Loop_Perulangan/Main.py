# While Loop (Perulangan)

# Struktur dasar:
# while kondisi:
#     aksi ini
#     aksi itu

# Contoh 1: Perulangan sederhana
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1 # Update variabel agar tidak infinite loop
    print(f"angka sekarang -> {angka}")
    print("Otong ganteng maksimal!")

print("cukup \n")

# Contoh 2: Penjelasan alur logic
angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    print("Otong ganteng maksimal!")

# Penjelasan:
# 1. Start angka = 0.
# 2. Cek apakah 0 < 5? True. 
# 3. Masuk loop: angka jadi 1, print pesan.
# 4. Cek lagi apakah 1 < 5? True.
# 5. Terus berulang sampai angka menjadi 5.
# 6. Cek apakah 5 < 5? False.
# 7. Keluar dari loop dan print "cukup".
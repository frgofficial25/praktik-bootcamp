# Definisi Variabel
a = 10
b = 3

print("Nilai a =", a)
print("Nilai b =", b)
print("="*50)

# 1. Operasi Penambahan (+)
hasil = a + b
print(a, "+", b, "=", hasil)

# 2. Operasi Pengurangan (-)
hasil = a - b
print(a, "-", b, "=", hasil)

# 3. Operasi Perkalian (*)
hasil = a * b
print(a, "*", b, "=", hasil)

# 4. Operasi Pembagian (/) -> Hasil selalu float
hasil = a / b
print(a, "/", b, "=", hasil)

# 5. Operasi Eksponen (Pangkat: **)
hasil = a ** b # 10 pangkat 3
print(a, "**", b, "=", hasil)

# 6. Operasi Modulus (Sisa Pembagian: %)
hasil = a % b
print(a, "%", b, "=", hasil) # 10 / 3 = 3 sisa 1

# 7. Operasi Floor Division (Pembagian Dibulatkan ke bawah: //)
hasil = a // b
print(a, "//", b, "=", hasil) # 10 / 3 = 3.33 dibulatkan jadi 3

print("="*50)

# ================================
# PRIORITAS OPERASI ARITMATIKA
# ================================

x = 3
y = 2
z = 4

# Operasi tanpa Tanda Kurung (Prioritas: Eksponen > Kali/Bagi/Modulus/Floor Division > Tambah/Kurang)
hasil = x ** y * z + x / y - y % z // x

# Perhitungan manual:
# 1. Eksponen: x ** y = 3^2 = 9
# 2. Perkalian: 9 * z = 9 * 4 = 36
# 3. Pembagian: x / y = 3 / 2 = 1.5
# 4. Modulus: y % z = 2 % 4 = 2
# 5. Floor Division: 2 // x = 2 // 3 = 0
# 6. Penjumlahan/Pengurangan: 36 + 1.5 - 0 = 37.5

print("X =", x, ", Y =", y, ", Z =", z)
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil) # Output: 37.5

print("\n" + "="*50)

# Operasi dengan Tanda Kurung (Kurung memiliki prioritas tertinggi)
# Contoh sederhana: x + y * z (perkalian didahulukan)
hasil = x + y * z
print(x, "+", y, "*", z, "=", hasil) # Output: 3 + (2*4) = 11

# Contoh dengan Kurung: (x + y) * z (penambahan didahulukan)
hasil = (x + y) * z
print("(", x, "+", y, ")", "*", z, "=", hasil) # Output: (3+2) * 4 = 20
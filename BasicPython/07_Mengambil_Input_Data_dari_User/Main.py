# ==================================
# 1. Mengambil Input Data String
# ==================================

# data akan selalu berupa string
data = input("Masukkan data: ")

# Mencetak data dan tipe datanya
print("data =", data, ", type:", type(data))

# Coba jalankan: masukkan 10, hasilnya akan tetap <class 'str'>


# ==================================
# 2. Mengambil Input Angka (Integer)
# ==================================

print("\n" + "="*50 + "\n")

# Casting input string ke integer
angka_int = int(input("Masukkan angka Integer: ")) 

print("data =", angka_int, ", type:", type(angka_int))


# ==================================
# 3. Mengambil Input Angka (Float)
# ==================================

print("\n" + "="*50 + "\n")

# Casting input string ke float
angka_float = float(input("Masukkan angka Float: "))

print("data =", angka_float, ", type:", type(angka_float))


# ==================================
# 4. Mengambil Input Boolean (Tricky)
# ==================================

print("\n" + "="*50 + "\n")

# Untuk input Boolean, perlu casting ganda: String -> Integer -> Boolean
# Input 0 akan menjadi False, input 1 akan menjadi True.

biner = bool(int(input("Masukkan nilai Biner (0/1): ")))

print("data =", biner, ", type:", type(biner))
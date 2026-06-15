# TIPE DATA DASAR

# 1. Integer (Angka Satuan/Bilangan Bulat)
print("TIPE DATA INTEGER")
data_integer = 1000000 # Boleh angka berapapun asalkan tidak ada koma
print("data:", data_integer, "bertipe:", type(data_integer))
print("-")

# 2. Float (Angka Desimal/Bilangan Pecahan)
print("TIPE DATA FLOAT")
data_float = 1.5 
print("data:", data_float, "bertipe:", type(data_float))
print("-")

# 3. String (Kumpulan Karakter)
print("TIPE DATA STRING")
data_string = "Ucup 10" # Angka di dalam kutip tetap string
print("data:", data_string, "bertipe:", type(data_string))
print("-")

# 4. Boolean (Biner: True/False)
print("TIPE DATA BOOLEAN")
data_bool = True # Nilai: True atau False
print("data:", data_bool, "bertipe:", type(data_bool))
print("=")

# TIPE DATA KHUSUS

# 1. Bilangan Kompleks (Complex Number)
print("TIPE DATA KHUSUS: COMPLEX")
data_complex = complex(5, 6) # Bentuk: 5 + 6j
print("data:", data_complex, "bertipe:", type(data_complex))
print("=")

# 2. Tipe Data dari Bahasa C (ctypes)
print("TIPE DATA DARI BAHASA C")

# Harus melakukan import dari library ctypes
from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)
print("data:", data_c_double, "bertipe:", type(data_c_double))

# Contoh lain dari ctypes: c_char, c_long (tidak ditulis dalam kode, hanya disebut)
# from ctypes import c_char, c_long
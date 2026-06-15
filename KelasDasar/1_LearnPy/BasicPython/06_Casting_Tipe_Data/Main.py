# =====================
# CASTING DARI INTEGER
# =====================

data_integer = 9
print("DATA ASAL:", data_integer, ", type:", type(data_integer))
print("-------------------------------------------------------")

# 1. Casting ke Float
data_float = float(data_integer)
print("casting ke float :", data_float, ", type:", type(data_float))

# 2. Casting ke String
data_string = str(data_integer)
print("casting ke string:", data_string, ", type:", type(data_string))

# 3. Casting ke Boolean
data_bool = bool(data_integer)
print("casting ke boolean:", data_bool, ", type:", type(data_bool))
# Catatan: Akan False jika nilai integer = 0
print("\n" + "="*50 + "\n")


# =====================
# CASTING DARI FLOAT
# =====================

data_float = 9.9
print("DATA ASAL:", data_float, ", type:", type(data_float))
print("-------------------------------------------------------")

# 1. Casting ke Integer
data_integer = int(data_float) # Akan dibulatkan ke bawah (floor)
print("casting ke integer:", data_integer, ", type:", type(data_integer))

# 2. Casting ke String
data_string = str(data_float)
print("casting ke string:", data_string, ", type:", type(data_string))

# 3. Casting ke Boolean
data_bool = bool(data_float)
print("casting ke boolean:", data_bool, ", type:", type(data_bool))
# Catatan: Akan False jika nilai float = 0.0
print("\n" + "="*50 + "\n")


# =====================
# CASTING DARI BOOLEAN
# =====================

data_boolean = True
print("DATA ASAL:", data_boolean, ", type:", type(data_boolean))
print("-------------------------------------------------------")

# 1. Casting ke Integer
data_integer = int(data_boolean) # True=1, False=0
print("casting ke integer:", data_integer, ", type:", type(data_integer))

# 2. Casting ke Float
data_float = float(data_boolean) # True=1.0, False=0.0
print("casting ke float :", data_float, ", type:", type(data_float))

# 3. Casting ke String
data_string = str(data_boolean)
print("casting ke string:", data_string, ", type:", type(data_string))
print("\n" + "="*50 + "\n")


# =====================
# CASTING DARI STRING
# =====================

data_string = "10" # String harus angka agar bisa di-casting ke int/float
# data_string = "Ucup" # Contoh yang menyebabkan error jika dicasting ke int/float

print("DATA ASAL:", data_string, ", type:", type(data_string))
print("-------------------------------------------------------")

# 1. Casting ke Integer
data_integer = int(data_string) # String harus angka
print("casting ke integer:", data_integer, ", type:", type(data_integer))

# 2. Casting ke Float
data_float = float(data_string) # String harus angka
print("casting ke float :", data_float, ", type:", type(data_float))

# 3. Casting ke Boolean
# data_string = "" # Contoh string kosong yang akan menghasilkan False
data_bool = bool(data_string)
print("casting ke boolean:", data_bool, ", type:", type(data_bool))
# Catatan: Akan False jika string kosong ("")
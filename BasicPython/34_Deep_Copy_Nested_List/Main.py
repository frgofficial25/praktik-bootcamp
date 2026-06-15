from copy import deepcopy

data_0 = [1, 2]
data_1 = [3, 4]

data_2D = [data_0, data_1, 10]
data_2D_copy = data_2D.copy()

print(f"data asli = {data_2D}")
print(f"data copy = {data_2D_copy}")

# Mengambil data dari nested list
data = data_2D[0][1]
print(f"data = {data}")

# Address asli vs copy (terlihat berbeda di level luar)
print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")

# Address member list (masih sama!)
print(f"address member ke-0 asli = {hex(id(data_2D[0]))}")
print(f"address member ke-0 copy = {hex(id(data_2D_copy[0]))}")

# Masalah: merubah data di nested list
data_2D[0][1] = 30
print(f"data asli = {data_2D}")
print(f"data copy = {data_2D_copy}") # Ikut berubah!

# --- SOLUSI: DEEP COPY ---
data_2D = [data_0, data_1, 10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"\naddress asli = {hex(id(data_2D))}")
print(f"address deep = {hex(id(data_2D_deepcopy))}")

print(f"address member ke-0 asli = {hex(id(data_2D[0]))}")
print(f"address member ke-0 deep = {hex(id(data_2D_deepcopy[0]))}") # Sekarang BERBEDA

# Merubah data pada list asli
data_2D[0][1] = 99
print(f"\ndata asli = {data_2D}")
print(f"data copy (shallow) = {data_2D_copy}") # Masih terikat ke data lama
print(f"data deep (independent) = {data_2D_deepcopy}") # Tetap aman, tidak berubah
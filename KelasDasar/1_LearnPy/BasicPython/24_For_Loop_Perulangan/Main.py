# Perulangan (loop)

# 1. Menggunakan List
angka2_list = [0, 2, 4, 8, 10] # ini adalah list
print(angka2_list)

for i in angka2_list:
    print(f"i sekarang -> {i}")

print("akhir dari program 1 \n")

# 2. Menggunakan Range
angka2_range = range(5)

for i in angka2_range:
    print(f"i sekarang -> {i}")

print("akhir dari program 2 \n")

angka2_range = range(1, 10)

for i in angka2_range:
    print(f"i sekarang -> {i}")
    # print("saya keren") # aksi ini akan diulang sebanyak range

print("akhir dari program 3 \n")

# 3. Menggunakan String
data_str = "saya ganteng abis"

for huruf in data_str:
    print(huruf)

print("akhir dari program 4 \n")
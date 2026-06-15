# Looping Dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasep",
    "cuy":"ucuy surucuy"
}

# 1. Looping standar (hanya mengambil key)
print("Looping standar:")
for teman in teman_teman:
    print(teman)

# 2. Mengambil iterables kuncinya saja (.keys())
print("\nLooping .keys():")
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key)) # Mengambil value via key

# 3. Mengambil iterables nilainya saja (.values())
print("\nLooping .values():")
values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

# 4. Mengambil item (key & value) sekaligus (.items())
print("\nLooping .items():")
items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item) # Hasilnya berupa tuple (key, value)

# Unpacking menggunakan .items()
print("\nLooping .items() dengan Unpacking:")
for key, value in teman_teman.items():
    print(f"key = {key}, value = {value}")
# --- LIST ---

# Kumpulan data angka
data_angka = [1, 5, 2, 3]
print(f"Data angka: {data_angka}")

# Kumpulan data string
data_string = ["ucup", "otong", "odah"]
print(f"Data string: {data_string}")

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(f"Data boolean: {data_boolean}")

# Kumpulan data campuran
data_campuran = [1, "gorengan", 2, "cireng", "ucup", True]
print(f"Data campuran: {data_campuran}")

## Cara alternatif membuat list
# Menggunakan range
data_range = range(0, 10, 2) # (start, stop, step)
print(f"Data range: {data_range}")
list_dari_range = list(data_range)
print(f"List dari range: {list_dari_range}")

# Membuat list dengan for loop (List Comprehension)
list_pakai_for = [i**2 for i in range(0, 10)]
print(f"List hasil comprehension: {list_pakai_for}")

# Membuat list pakai for dan if
list_pakai_for_if = [i for i in range(0, 10) if i != 5]
print(f"List pakai if (tanpa angka 5): {list_pakai_for_if}")

# Contoh list angka genap
list_genap = [i for i in range(0, 10) if i % 2 == 0]
print(f"List angka genap: {list_genap}")

# Contoh list angka ganjil
list_ganjil = [i for i in range(0, 10) if i % 2 != 0]
print(f"List angka ganjil: {list_ganjil}")
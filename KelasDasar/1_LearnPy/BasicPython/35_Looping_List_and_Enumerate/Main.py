# Looping dari list

# 1. For Loop Biasa
print("For Loop")
kumpulan_angka = [4, 3, 2, 5, 6, 1]
for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["ucup", "otong", "dadang", "diding", "dudung"]
for nama in peserta:
    print(f"nama = {nama}")

# 2. For Loop dan range
print("\nFor Loop dan Range")
kumpulan_angka = [10, 5, 4, 2, 6, 5]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# 3. While Loop
print("\nWhile Loop")
kumpulan_angka = [10, 5, 4, 2, 6, 5]
panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# 4. List Comprehension
print("\nList Comprehension")
data = ["ucup", 1, 2, 3, "otong"]
[print(f"data = {i}") for i in data]

# Contoh lain: membuat list kuadrat
angka = [10, 5, 4, 2, 6, 5]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# 5. Enumerate
print("\nEnumerate")
data_list = ["ucup", 1, 2, 3, "otong"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
    
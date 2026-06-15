""" Lambda dan Anonymous Function """

# 1. Fungsi Biasa vs Lambda
def f_kuadrat(angka):
    return angka**2

print(f"Hasil fungsi biasa: {f_kuadrat(3)}")

# Format Lambda -> nama_variabel = lambda argumen: ekspresi
kuadrat = lambda angka : angka**2
print(f"Hasil lambda kuadrat: {kuadrat(5)}")

# Lambda dengan dua input
pangkat = lambda num, pow : num**pow
print(f"Hasil lambda pangkat: {pangkat(4, 2)}")

# 2. Kegunaan: Sorting List
data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort()
print(f"Sorted standar: {data_list}")

# Sorting berdasarkan panjang nama (len)
data_list.sort(key=lambda nama: len(nama))
print(f"Sorted by len: {data_list}")

# 3. Kegunaan: Filter List
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

data_genap = list(filter(lambda x: x % 2 == 0, data_angka))
data_ganjil = list(filter(lambda x: x % 2 != 0, data_angka))
data_kelipatan_3 = list(filter(lambda x: x % 3 == 0, data_angka))

print(f"Data Genap: {data_genap}")
print(f"Data Ganjil: {data_ganjil}")
print(f"Data Kelipatan 3: {data_kelipatan_3}")

# 4. Anonymous Function (Currying)
def buat_pangkat(n):
    return lambda angka : angka**n

pangkat2 = buat_pangkat(2)
pangkat3 = buat_pangkat(3)

print(f"Pangkat 2 dari 5: {pangkat2(5)}")
print(f"Pangkat 3 dari 3: {pangkat3(3)}")
# Pemanggilan langsung tanpa variabel perantara
print(f"Pangkat bebas (5 pangkat 4): {buat_pangkat(4)(5)}")
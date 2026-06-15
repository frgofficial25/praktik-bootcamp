""" Fungsi dengan kembalian (return value) """

# 1. Fungsi kuadrat sederhana
def kuadrat(input_angka):
    '''fungsi kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat

y = kuadrat(5)
print(f"Hasil kuadrat 5 adalah {y}")

print(f"Hasil kuadrat 6 adalah {kuadrat(6)}")

z = 10 + kuadrat(7)
print(f"10 + 7^2 = {z}")

# 2. Fungsi tambah dengan return
def fungsi_tambah(angka_1, angka_2):
    '''fungsi tambah'''
    return angka_1 + angka_2

a = fungsi_tambah(10, 8)
print(f"Hasil tambah 10 + 8 = {a}")

# 3. Fungsi dengan return banyak (Multi Return)
def operasi_matematika(angka_1, angka_2):
    '''fungsi operasi matematika dasar'''
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah, kurang, kali, bagi

# Unpacking hasil multi return
k, l, m, n = operasi_matematika(9, 5)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali   = {m}")
print(f"Hasil bagi   = {n}")
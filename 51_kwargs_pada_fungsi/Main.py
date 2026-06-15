""" **kwargs pada Fungsi """

# 1. Dasar **kwargs
def fungsi_kwargs(**kwargs):
    # kwargs akan menjadi dictionary
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

# Memanggil dengan keyword
fungsi_kwargs(nama="Ucup", tinggi=183, berat=79)

# 2. Studi Kasus: Kombinasi *args dan **kwargs
def math_operasi(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        print("Operasi Penjumlahan")
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        print("Operasi Perkalian")
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak ada operasi")
    
    return output

# Contoh penggunaan 1: Penjumlahan
hasil_tambah = math_operasi(1, 2, 3, 4, option="tambah")
print(f"Hasil jumlah = {hasil_tambah}")

# Contoh penggunaan 2: Perkalian
hasil_kali = math_operasi(1, 2, 3, 4, option="kali")
print(f"Hasil kali = {hasil_kali}")
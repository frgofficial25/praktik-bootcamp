""" Fungsi dengan argumen (input) """

# 1. Fungsi dengan argumen string
def hello_world(nama):
    '''fungsi hello world menerima input dengan variabel nama'''
    print(f"Selamat datang dunia wahai {nama}")

hello_world("Ucup")
hello_world("Asep")

# 2. Fungsi dengan argumen angka (Matematika)
def tambah(angka_1, angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1, 5)
tambah(1000, 1)

# 3. Fungsi dengan argumen list
def say_hi(list_peserta):
    '''fungsi say hi untuk list'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota_boyband = ["Ucup", "Otong", "Dudung"]

say_hi(anggota_boyband)
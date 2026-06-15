""" Default Argument pada Fungsi """

# 1. Contoh sederhana default argument
def say_hello(nama = "Ganteng"):
    '''fungsi dengan default argument'''
    print(f"Halo {nama}")

say_hello("Ucup") # Output: Halo Ucup
say_hello()        # Output: Halo Ganteng

# 2. Contoh dengan satu input biasa dan satu default
def sapa_dia(nama, pesan = "Apa kabar?"):
    '''fungsi dengan satu input biasa dan satu default'''
    print(f"Hai {nama}, {pesan}")

sapa_dia("Otong", "Selamat pagi")
sapa_dia("Dudung")

# 3. Contoh akses dengan nama argumen (Keyword Arguments)
def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2, 4)) # 16

# Kita bisa balik urutannya dengan menyebutkan nama argumennya
hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil) # 125

# 4. Contoh dengan banyak argumen default
def fungsi(input1=1, input2=2, input3=3, input4=4):
    return input1 + input2 + input3 + input4

print(fungsi()) # 10
print(fungsi(input3=10)) # 1+2+10+4 = 17
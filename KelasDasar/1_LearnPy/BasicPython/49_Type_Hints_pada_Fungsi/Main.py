""" Type Hints pada Fungsi """

# 1. Masalah Tanpa Type Hints
# def fungsi(parameter):
#     hasil = parameter**2
#     print(hasil)

# fungsi(1)      # Jalan
# fungsi("Ucup") # Error saat runtime

# 2. Penggunaan Type Hints
import string

def sepuluh_pangkat(argumen:int) -> int:
    '''fungsi dengan hints'''
    output = 10**argumen
    return output

HASIL = sepuluh_pangkat(2)
print(HASIL)

def display(argumen:str):
    '''fungsi display tanpa return (None)'''
    print(argumen)

display("Ucup")

# Contoh perbandingan dengan bahasa C++ atau Java (sebagai pengetahuan)
# integer kuadrat(integer nilai){
#     return nilai**2;
# }
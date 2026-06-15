from numbers import Number

def tambah(a, b):
    # Membuat exception sendiri jika input bukan angka
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise Exception("input harus angka")
    return a + b

print(tambah(5, 6))

# Menangkap tipe Exception spesifik
angka = 0
try:
    hasil = 10 / angka
except Exception as error_message:
    print(error_message) # Output: division by zero

# Atau menangkap secara spesifik tipenya
try:
    hasil = 10 / angka
except ZeroDivisionError as error_message:
    print(error_message)
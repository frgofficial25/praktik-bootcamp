# file: main_app.py
import fungsi

# __name__ pada file program utama akan menjadi "__main__"
print(f"Nilai __name__ pada Main.py adalah '{__name__}'")

## Contoh penggunaan __main__ sebagai gerbang program

# 1. Deklarasi (Fungsi, Variabel, Kelas)
def fungsi_tambah(a:int, b:int) -> int:
    return a + b

# 2. Fungsi Utama (Gerbang Program)
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1, angka2)
    print(f"Hasil tambah: {hasil}")
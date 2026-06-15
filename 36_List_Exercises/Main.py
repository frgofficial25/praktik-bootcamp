# LATIHAN LIST - PROGRAM DAFTAR BUKU

list_buku = []

while True:
    print("\nMasukkan data buku")
    judul = input("Judul buku\t: ")
    penulis = input("Nama penulis\t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("\n"+"="*10, "DATA BUKU", "="*10)
    for index, buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n"+"="*31)
    is_lanjut = input("Apakah dilanjutkan? (y/n) ")

    if is_lanjut == "n":
        break

print("\nPROGRAM SELESAI, TERIMA KASIH")
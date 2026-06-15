# Control Flow: Continue dan Pass

# --- 1. Contoh Penggunaan PASS ---
print("--- Contoh Pass ---")
angka = 0

while angka < 5:
    angka += 1
    if angka == 3:
        pass # Ini dummy, tidak akan melakukan apa-apa
    print(angka)


# --- 2. Contoh Penggunaan CONTINUE ---
print("\n--- Contoh Continue ---")
angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # Aksi 1

    if angka == 3:
        print("nice!")
        continue # Membuat loop meloncat ke step selanjutnya (ke atas)

    print("whassup!") # Aksi 2 (akan di-skip jika angka == 3)

print("akhir dari program")
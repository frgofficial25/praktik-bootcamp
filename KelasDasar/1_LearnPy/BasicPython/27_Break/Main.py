# Control Flow: Break

# --- Contoh 1: Penggunaan Standar ---
angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("nice!")
        break # Perulangan akan langsung berhenti di sini

    print("whassup!")

print("cukup finish \n")


# --- Contoh 2: Penggunaan dengan Input User ---
data_int = int(input("hitung sampai berapa? "))

angka = 0

while True: # Perulangan tak terbatas
    angka += 1
    print(f"count -> {angka}")

    if angka == data_int:
        print("nice!")
        break # Berhenti saat mencapai angka inputan user

    print("whassup!")

print("cukup finish")
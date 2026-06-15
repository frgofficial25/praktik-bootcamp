# IF dan ELSE Statement

# 1. Mengambil input dari user
nama = input("Siapa nama anda? ")

# 2. Program IF Inline
# if nama == "ucup": print("Kamu Ganteng abis!!!")
# print(f"Terima kasih {nama}")

# 3. Program IF dengan Indentasi (Indentation)
if nama == "ucup":
    print("kamu ganteng abis!")
    print("kamu juga keren banget!")
print(f"Terima kasih {nama}")

# 4. ELSE Statement (Percabangan dua arah)
if nama == "otong":
    print("hai otong, si keren!!!")
else:
    print("Ah kamu bukan otong, kamu gak keren!")

print("akhir dari program")
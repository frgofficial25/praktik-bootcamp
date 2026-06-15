## Operasi dan manipulasi string (Part 2)

# 1. Merubah Case dari String

# Merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# Merubah semua ke lower case
alay = "aKu KeCe AbisZzzZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

# 2. Pengecekan dengan is method

# Contoh untuk pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya boolean
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya boolean
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil boolean
print(judul + " is title = " + str(cek_judul))

# 3. Mengecek komponen startswith() dan endswith()
print("\n" + 20*"=" + "\n")

cek_start = "Sajangnim Oppa".startswith("Sajangnim")
print("start = " + str(cek_start))

cek_end = "Sajangnim Oppa".endswith("Oppa")
print("end = " + str(cek_end))

# 4. Penggabungan dan Pemisahan komponen join() dan split()
print("\n" + 20*"=" + "\n")

pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = " akhirat ".join(pisah)
print(gabung)

print("\n" + 20*"=" + "\n")

# memisahkan kembali
print(gabung.split(' akhirat '))

# 5. Alokasi karakter rjust(), ljust(), center()
print("\n" + 20*"=" + "\n")

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20, ":")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip(":") # menghilangkan tanda :
print("'"+tengah+"'")

kanan = kanan.strip() # menghilangkan spasi
print("'"+kanan+"'")
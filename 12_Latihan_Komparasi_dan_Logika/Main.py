# Latihan Komparasi dan Logika

# 1. Membuat gabungan area rentang dari angka

# +++++3-------10+++++
# Area yang ingin kita buat: 
# Angka kurang dari 3 atau lebih besar dari 10 akan bernilai True

inputUser = float(input("masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10 :"))

# +++++3--------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# --------------10+++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# +++++3-------10+++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan:", isCorrect)


# 2. Membuat irisan area rentang dari angka
# ----3++++++++10----
# Area yang ingin kita buat:
# Angka di antara 3 dan 10 akan bernilai True

print("\n",20*"=","\n")
inputUser = float(input("masukkan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10 :"))

# ----3++++++++++++++
# Memeriksa angka lebih dari 3
isLebihDari = (inputUser > 3)
print("Lebih dari 3 =", isLebihDari)

# +++++++++++++10----
# Memeriksa angka kurang dari 10
isKurangDari = (inputUser < 10)
print("Kurang dari 10 =", isKurangDari)

# ----3++++++++10----
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan:", isCorrect)

# Tugas
# 1 ---0+++5---8+++11---

print("\n",20*"=","\n")
inputUser = float(input("masukkan angka yang bernilai \nlebih dari 0 \ndan \nkurang dari 5\n atau\nlebih dari 8 \ndan \nkurang dari 11 :"))

isLebihDari0 = inputUser > 0
isKurangDari5 = inputUser < 5
isLebihDari8 = inputUser > 8
isKurangDari11 = inputUser < 11
isCorrect = (isLebihDari0 and isKurangDari5) or (isLebihDari8 and isKurangDari11)
print("angka yang anda masukkan:", isCorrect)

# 2 +++0---5+++8---11+++

print("\n",20*"=","\n")
inputUser = float(input("masukkan angka yang bernilai \nkurang dari 0 \natau \nlebih dari 5\n dan\nkurang dari 8 \natau \nlebih dari 11 :"))

isKurangDari0 = inputUser < 0
isLebihDari5 = inputUser > 5
isKurangDari8 = inputUser < 8
isLebihDari11 = inputUser > 11
isCorrect = isKurangDari0 or (isLebihDari5 and isKurangDari8) or isLebihDari11
print("angka yang anda masukkan:", isCorrect)

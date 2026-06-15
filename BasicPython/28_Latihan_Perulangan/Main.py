# Latihan Perulangan Membuat Segitiga
# Kelas Terbuka

sisi = int(input("Masukkan sisi segitiga : "))

# Segitiga Siku - Siku (for 1)
for i in range(sisi) :
    a = i + 1
    print(a*"* ")
print()
# Segitiga Siku - Siku (for 2)
for i in range(sisi) :
    a = i + 1
    for j in range(a) :
        print("* ", end = "")
    print()
print()
# Segitiga Siku - Siku (while)
i = 0
while (i < sisi) :
    i += 1
    print(i*"* ")
print()
# Segitiga Sama Sisi (for)
for i in range(sisi) :
    a = i + 1
    print((sisi - a)*" ", end = "")
    print(a*"* ")
print()
# Segitiga Sama Sisi (while)
i = 0
while (i < sisi) :
    i += 1
    print((sisi - i)*" ", end = "")
    print(i*"* ")
print()
# Segitiga Siku - Siku 2 (for)
for i in range(sisi) :
    a = i * 2 + 1
    print(a*"*")
print()
# Segitiga Sama Sisi 2 (for)
sisi2 = sisi * 2 - 1
for i in range(sisi) :
    a = i * 2 + 1
    print((sisi2 - a)*" ", end = "")
    print(a*"* ")
print()
# Segitiga Sama Sisi 3 (for)
for i in range(sisi) :
    a = i * 2 + 1
    print((sisi - i - 1)*" ", end = "")
    print(a*"*")
print()
# Segitiga Siku - Siku 2 (while)
i = 0
while (i < sisi) :
    a = i * 2 + 1
    print(a*"*")
    i += 1
print()
# Segitiga Sama Sisi 2 (while)
i = 0
sisi2 = sisi * 2 - 1
while (i < sisi) :
    a = i * 2 + 1
    print((sisi2 - a)*" ", end = "")
    print(a*"* ")
    i += 1
print()
# Segitiga Sama Sisi 3 (while)
i = 0
while (i < sisi) :
    a = i * 2 + 1
    print((sisi - i - 1)*" ", end = "")
    print(a*"*")
    i += 1
print()
# Segitiga Siku - Siku Terbalik Kanan (for)
for i in range(sisi) :
    print((sisi - i)*"* ")
print()
# Segitiga Siku - Siku Terbalik Kanan (while)
i = 0
while (i < sisi) :
    print((sisi - i)*"* ")
    i += 1
print()
# Segitiga Siku - Siku Terbalik Kanan 2 (for)
sisi2 = sisi * 2 - 1
for i in range(sisi) :
    a = sisi2 - i * 2
    print(a*"*")
print()
# Segitiga Siku - Siku Terbalik Kanan 2 (while)
i = 0
sisi2 = sisi * 2 - 1
while (i < sisi) :
    a = sisi2 - i * 2
    print(a*"*")
    i += 1
print()

# Segitiga Siku - Siku Kiri (for)
for i in range(sisi) :
    print((sisi - i - 1)*"  ", end = "")
    print((i + 1)*"* ")
print()
# Segitiga Siku - Siku Kiri (while)
i = 0
while (i < sisi) :
    print((sisi - i - 1)*"  ", end = "")
    print((i + 1)*"* ")
    i += 1
print()
# Segitiga Siku - Siku Kiri 2 (for)
sisi2 = sisi * 2 - 1
for i in range(sisi) :
    a = i * 2 + 1
    print((sisi2 - i * 2 - 1)*" ", end = "")
    print(a*"*")
print()
# Segitiga Siku - Siku Terbalik Kiri 2 (while)
i = 0
sisi2 = sisi * 2 - 1
while (i < sisi) :
    a = i * 2 + 1
    print((sisi2 - i * 2 - 1)*" ", end = "")
    print(a*"*")
    i += 1
print()


# Segitiga Siku - Siku Terbalik Kiri (for)
for i in range(sisi) :
    print(i*"  ", end = "")
    print((sisi - i)*"* ")
print()
# Segitiga Siku - Siku Terbalik Kiri (while)
i = 0
while (i < sisi) :
    print(i*"  ", end = "")
    print((sisi - i)*"* ")
    i += 1
print()
# Segitiga Siku - Siku Terbalik Kiri 2 (for)
sisi2 = sisi * 2 - 1
for i in range(sisi) :
    a = sisi2 - i * 2
    print(i*2*" ", end = "")
    print(a*"*")
print()
# Segitiga Siku - Siku Terbalik Kiri 2 (while)
i = 0
sisi2 = sisi * 2 - 1
while (i < sisi) :
    a = sisi2 - i * 2
    print(i*2*" ", end = "")
    print(a*"*")
    i += 1
print()

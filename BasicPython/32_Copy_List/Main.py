## Teknik Menduplikat List

a = ["Ucup", "Otong", "Dudung"]
print(f"data a = {a}")

b = a # Pass by reference
print(f"data b = {b}")

# Kita coba ubah member dari a
a[1] = "Michael"
b.sort()
print(f"data a = {a}")
print(f"data b = {b}")

# Address dari kedua list (a dan b)
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# Menduplikat list dengan copy
print("\nmembuat list c dengan a.copy()")
c = a.copy() # Full duplicate / data baru

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}") # Akan berbeda sendiri

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("\nkita ubah data c[0]")
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}") # Hanya c yang berubah menjadi Dadang

print("\nkita ubah data a[1]")
a[1] = "Otong"

print(f"a = {a}")
print(f"b = {b}") # b ikut berubah karena satu address dengan a
print(f"c = {c}") # c tetap karena data terpisah
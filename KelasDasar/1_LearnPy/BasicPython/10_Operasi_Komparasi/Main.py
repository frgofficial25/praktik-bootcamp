# Operasi Komparasi
# Setiap hasil dari operasi komparasi adalah boolean (True/False)

a = 4
b = 2

# 1. Lebih besar dari (>)
print('========== lebih besar dari (>)')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# 2. Kurang dari (<)
print('========== kurang dari (<)')
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# 3. Lebih besar dari sama dengan (>=)
print('========== lebih besar dari sama dengan (>=)')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# 4. Kurang dari sama dengan (<=)
print('========== kurang dari sama dengan (<=)')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# 5. Sama dengan (==)
print('========== sama dengan (==)')
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

# 6. Tidak sama dengan (!=)
print('========== tidak sama dengan (!=)')
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)

# 'is' sebagai komparasi object identity
print('========== object identity (is)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =', x, ', id =', hex(id(x)))
print('nilai y =', y, ', id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 5
y = 6
print('nilai x =', x, ', id =', hex(id(x)))
print('nilai y =', y, ', id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

# 'is not' sebagai komparasi object identity
print('========== object identity (is not)')
x = 5
y = 5
print('nilai x =', x, ', id =', hex(id(x)))
print('nilai y =', y, ', id =', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

x = 5
y = 6
print('nilai x =', x, ', id =', hex(id(x)))
print('nilai y =', y, ', id =', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)
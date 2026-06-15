# Latihan Perhitungan Sederhana: Konversi Satuan Temperatur

print("\nPROGRAM KONVERSI TEMPERATUR")
print("===========================\n")

# Mengambil data suhu dalam Celcius dari user
# Menggunakan float agar bisa menerima angka desimal
celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah", celcius, "Celcius")

# REAMUR
# Rumus: (4/5) * C
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ", reamur, "Reamur")

# FAHRENHEIT
# Rumus: (9/5) * C + 32
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")

# KELVIN
# Rumus: C + 273
kelvin = celcius + 273
print("suhu dalam kelvin adalah ", kelvin, "Kelvin")

# Tugas

# Fahrenheit ke Kelvin
fahrenheit = float(input('Masukkan suhu dalam fahrenheit : '))
celcius = (5/9) * (fahrenheit - 32)
kelvin = celcius + 273
print("Suhu dalam kelvin adalah:", kelvin)

# Kelvin ke Fahrenheit
kelvin = float(input('Masukkan suhu dalam kelvin : '))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah:", fahrenheit)
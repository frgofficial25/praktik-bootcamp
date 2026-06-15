""" Menggunakan Standard Library """

# 1. Contoh Datetime
import datetime

data_waktu = datetime.datetime.now()
print(f"Data waktu sekarang: {data_waktu}")
print(f"Tahun: {data_waktu.year}")
print(f"Hari (format string): {data_waktu.strftime('%A')}")


# 2. Contoh Collections (Counter)
from collections import Counter

data = ["a", "b", "c", "d", "a", "a", "d", "e"]
# Menghitung jumlah data tanpa manual loop
data_count = Counter(data)

print(f"Data count: {data_count}")
print(f"Jumlah huruf 'a': {data_count['a']}")
print(f"Jumlah huruf 'd': {data_count['d']}")


# 3. Contoh IO (Membaca file)
import io

file = open("file_teks.txt", mode='r')
# Membaca isi file
print(f"Isi file teks: {file.read()}")
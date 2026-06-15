# Copy & Pop Dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasep",
    "cuy":"ucuy surucuy"
}

# 1. Copy Dictionary
print("--- Copy Dictionary ---")
friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# Merubah data di list asli (tidak merubah friends karena pakai .copy())
teman_teman["cup"] = "ucup si ganteng"

print(f"teman-teman (setelah update): {teman_teman}\n")
print(f"friends (tetap): {friends}\n")

# 2. Pop Dictionary (mengambil data berdasarkan key)
print("--- Pop Dictionary ---")
dataAsep = friends.pop("sep")

print(f"data asep = {dataAsep}")
print(f"friends = {friends}\n") # Asep sudah hilang dari dictionary friends

# 3. PopItem Dictionary (mengambil data terakhir)
print("--- PopItem Dictionary ---")
dataTerakhir = friends.popitem()

print(f"data terakhir = {dataTerakhir}")
print(f"friends = {friends}\n") # Cuy sudah hilang karena dia paling terakhir
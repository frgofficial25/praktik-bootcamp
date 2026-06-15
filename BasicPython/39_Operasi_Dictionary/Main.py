# Operasi Dictionary

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung"
}

# 1. Panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# 2. Mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# 3. Mengakses value (read) dengan get
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) # menggunakan default message agar tidak error

# 4. Mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)

# Menambah data (append) secara manual
data_dict["sep"] = "si sepsap"
print(data_dict)

# Mengupdate/Menambah dengan .update()
data_dict.update({"cup":"ucup surucup"}) # update data yang ada
data_dict.update({"faqih":"faqihza keren"}) # otomatis nambah jika tidak ada
print(data_dict)

# 5. Mendelete data pada dictionary
del data_dict["faqih"]
print(data_dict)
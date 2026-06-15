# String width and Alignment

# Data
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# String standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print("\n"+ 5*"=" + " DATA STANDARD " + 5*"=")
print(data_string)

# String Multiline (menggunakan enter / newline \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n" + 5*"=" + " DATA MULTILINE (NEWLINE) " + 5*"=")
print(data_string)

# String Multiline (kutip tiga / triplets)
data_string = f"""nama = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n" + 5*"=" +" DATA MULTILINE (TRIPLETS) " + 5*"=")
print(data_string)

# Mengatur Lebar (Width) dan Aligment
data_nama = "Ucup"
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print("\n" + 5*"=" + " DATA ALIGNMENT " + 5*"=")
print(data_string)

# Contoh jika nama lebih panjang, alignment tetap terjaga
data_nama = "Ucup Surucup"
data_string = f"""
nama   = {data_nama:>20}
umur   = {data_umur:>20}
tinggi = {data_tinggi:>20}
sepatu = {data_nomor_sepatu:>20}
"""
print(data_string)
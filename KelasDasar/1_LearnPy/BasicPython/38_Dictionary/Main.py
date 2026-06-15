# Dictionary (dict) -> associative array
# identifier -> key

# List biasa (menggunakan indeks)
data_list = ['ucup', 'otong', 'dudung']
print(f"data list = {data_list[0]}")

# Dictionary
data_dict = {
    'cp': 'ucup',
    'tg': 'otong',
    'dg': 'dudung',
    'nmbr': 1000,
    'list': data_list,
}

print(f"data dictionary = {data_dict}")

# Mengakses data menggunakan Key
print(f"mengakses key cp = {data_dict['cp']}")
print(f"mengakses key nmbr = {data_dict['nmbr']}")
print(f"mengakses key list = {data_dict['list']}")
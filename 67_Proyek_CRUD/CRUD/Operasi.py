from . import Database
from .Util import random_string
import time
import os

def create_first_data() :
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while True :
        try :
            tahun = int(input("Tahun\t: "))
            if (len(str(tahun)) == 4) :
                break
            else :
                print("tahun harus 4 digit, silahkan masukkan tahun lagi (yyyy)")
        except :
            print("tahun harus angka, silahkan masukkan tahun lagi (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try :
        with open(Database.DB_NAME, mode="w", encoding="utf-8", newline='') as file :
            file.write(data_str)
    except :
        print("Proses Create Awal Gagal")

def delete(no_buku) :
    try :
        with open(Database.DB_NAME, mode="r", newline='') as file :
            counter = 0
            while(True) :
                content = file.readline()
                if len(content) == 0 :
                    break
                elif counter == no_buku - 1 :
                    pass
                else :
                    with open("C:\\BasicPython\\67_Proyek_CRUD\\buffer.txt", mode="a", encoding="utf-8", newline='') as buffer_file :
                        buffer_file.write(content)
                counter +=1
    except :
        print("Gagal menghapus data buku")

    os.replace("C:\\BasicPython\\67_Proyek_CRUD\\buffer.txt", Database.DB_NAME)

def update(no_buku, pk, date_add, penulis, judul, tahun) :
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = date_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    data_length = len(data_str)

    try :
        with(open(Database.DB_NAME, mode="r+", encoding="utf-8", newline='')) as file :
            file.seek(data_length * (no_buku - 1))
            file.write(data_str)
    except :
        print("error dalam update data")     

def read(**kwargs) :
    try :
        with open(Database.DB_NAME, mode="r") as file :
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs :
                index_buku = kwargs["index"] - 1
                if index_buku < 0 or index_buku > jumlah_buku - 1 :
                    return False
                else :
                    return content[index_buku]
            else :
                return content
    except :
        print("Membaca Database Error")
        return False

def create(penulis, judul, tahun) :
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try :
        with open(Database.DB_NAME, mode="a", encoding="utf-8", newline='') as file :
            file.write(data_str)
    except :
        print("Proses Create Gagal")
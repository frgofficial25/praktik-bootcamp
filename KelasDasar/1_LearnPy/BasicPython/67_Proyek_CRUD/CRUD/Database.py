from . import Operasi

DB_NAME = "C:\\BasicPython\\67_Proyek_CRUD\\data.txt"
TEMPLATE = {
    "pk" : "XXXXXX",
    "date_add" : "yyyy-mm-dd",
    "judul" : 255 * " ",
    "penulis" : 255 * " ",
    "tahun" : "yyyy"
}

def init_console() :
    try :
        with open(DB_NAME, mode="r") as file:
            print("Database tersedia, init done!")
    except :
        print("Database tidak ditemukan, silahkan buat database baru!")
        Operasi.create_first_data()
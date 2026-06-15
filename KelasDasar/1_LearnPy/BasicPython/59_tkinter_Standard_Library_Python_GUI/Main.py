import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Inisialisasi Window
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("Sapa Dia")

# Variabel Nama
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Fungsi yang dipanggil oleh tombol
def tombol_klik():
    """Fungsi ini akan dipanggil oleh tombol sapa"""
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteng!"
    showinfo(title="Sapa", message=pesan)

# Frame Input
input_frame = ttk.Frame(window)
# Penempatan: Pack, Grid, Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Komponen-komponen
# 1. Label Nama Depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)

# 2. Entry Nama Depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 3. Label Nama Belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(padx=10, fill="x", expand=True)

# 4. Entry Nama Belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# 5. Tombol
tombol_sapa = ttk.Button(input_frame, text="Sapa!", command=tombol_klik)
tombol_sapa.pack(padx=10, pady=10, fill="x", expand=True)

# Menjalankan aplikasi (Looping terus menerus)
window.mainloop()
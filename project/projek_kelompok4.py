import tkinter as tk
from tkinter import ttk

from datetime import datetime, timedelta

def hitung_tanggal_menstruasi():
    try:
        tanggal_terakhir = datetime.strptime(entry_tanggal_terakhir.get(), "%Y-%m-%d")
        siklus_menstruasi = int(entry_siklus_menstruasi.get())
        panjang_menstruasi = int(entry_panjang_menstruasi.get())

        # Perkiraan tanggal menstruasi berikutnya
        tanggal_menstruasi = tanggal_terakhir + timedelta(days=siklus_menstruasi)

        # Perkiraan tanggal kesuburan pada periode berikutnya (contoh: 14 hari sebelum menstruasi)
        tanggal_kesuburan = tanggal_menstruasi - timedelta(days=14)

        # Perkiraan akhir periode (contoh: tanggal menstruasi + panjang menstruasi)
        tanggal_akhir_periode = tanggal_menstruasi + timedelta(days=panjang_menstruasi)

        #menampilkan halaman loading
        loading_window = tk.Toplevel(window)
        loading_window .title("loading")
        loading_window.geometry(window.geometry())
        
        loading_label = ttk.Label(loading_window, text="Sedang menghitung....", font=("Helvetica", 12))
        loading_label.pack(padx=20, pady=20)
        
        window.after(2000,lambda: halaman_hasil(tanggal_menstruasi, tanggal_kesuburan, tanggal_akhir_periode, loading_window))

    except ValueError:
        halaman_hasil.set("Format tanggal atau siklus harus berupa angka")
 
#halaman selanjutnya
def halaman_hasil(tanggal_menstruasi, tanggal_kesuburan, tanggal_akhir_periode, loading_window):
    
    
    #hentikan loading
    loading_window.destroy()

    # Menampilkan hasil
    window_hasil = tk.Toplevel(window)
    window_hasil.title("Hasil Perhitungan")

    label_hasil_tanggal = ttk.Label(window_hasil, text=f"Tanggal Menstruasi Berikutnya: {tanggal_menstruasi.strftime('%Y-%m-%d')}", font=("Helvetica", 12))
    label_hasil_tanggal.pack(pady=10)

    label_hasil_kesuburan = ttk.Label(window_hasil, text=f"Periode Kesuburan: {tanggal_kesuburan.strftime('%Y-%m-%d')}",font=("Helvetica", 12))
    label_hasil_kesuburan.pack(pady=10)

    label_hasil_akhir_periode = ttk.Label(window_hasil, text=f"Tanggal akhir periode {tanggal_akhir_periode.strftime('%Y-%m-%d')}", font=("Helvetica", 12))
    label_hasil_akhir_periode.pack(pady=10)

    window_hasil.geometry(window.geometry())
    

def tampilkan_halaman_utama():
    halaman_selamat_datang.pack_forget()  # Menyembunyikan halaman selamat datang
    halaman_utama.pack(expand=True, fill="both")


# Membuat window utama
window = tk.Tk()
window.title("Aplikasi Siklus Menstruasi")
window.geometry("400x200")

# Membuat halaman selamat datang
halaman_selamat_datang = ttk.Frame(window)
halaman_selamat_datang.pack(expand=True, fill="both")

label_selamat_datang = ttk.Label(halaman_selamat_datang, text="Selamat datang di Aplikasi Menstruasi\nSilakan masukkan data menstruasi Anda", font=("Helvetica", 12))
label_selamat_datang.pack(pady=20)

button_lanjutkan = ttk.Button(halaman_selamat_datang, text="Lanjutkan", command=tampilkan_halaman_utama)
button_lanjutkan.pack()

#halaman utama
halaman_utama = ttk.Frame(window)

# Membuat label dan entry untuk tanggal terakhir
label_tanggal_terakhir = ttk.Label(halaman_utama, text="Tanggal Terakhir (YYYY-MM-DD):", font=("Helvetica", 12))
label_tanggal_terakhir.grid(row=1, column=0, padx=10, pady=5, sticky="W")

entry_tanggal_terakhir = ttk.Entry(halaman_utama)
entry_tanggal_terakhir.grid(row=1, column=1, padx=10, pady=5)

# Membuat label dan entry untuk siklus menstruasi
label_siklus_menstruasi = ttk.Label(halaman_utama, text="Panjang Siklus Menstruasi (hari):", font=("Helvetica", 12))
label_siklus_menstruasi.grid(row=2, column=0, padx=10, pady=5, sticky="W")

entry_siklus_menstruasi = ttk.Entry(halaman_utama)
entry_siklus_menstruasi.grid(row=2, column=1, padx=10, pady=5)

# Membuat label dan entry untuk panjang menstruasi
label_panjang_menstruasi = ttk.Label(halaman_utama, text="Panjang Menstruasi (hari):", font=("Helvetica", 12))
label_panjang_menstruasi.grid(row=3, column=0, padx=10, pady=5, sticky="W")

entry_panjang_menstruasi = ttk.Entry(halaman_utama)
entry_panjang_menstruasi.grid(row=3, column=1, padx=10, pady=5)

# Membuat tombol untuk menghitung tanggal menstruasi
button_hitung = ttk.Button(halaman_utama, text="Hitung", command=hitung_tanggal_menstruasi)
button_hitung.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
window.mainloop()
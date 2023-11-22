def nilai(a):
    if a < 60:
        return 'gagal'
    elif 60 <= a <= 70:
        return 'baik'
    elif 71 <= a <= 80:
        return 'sangat baik'
    elif 81 <= a <= 100:
        return 'istimewa'
    else:
        return 'Salah memasukan nilai'

#input nilai
b = int(input('nilai sebesar '))

#memanggil fungsi nilai dan cetak hasilnya
hasil = nilai(b)
print('kategorinya', hasil)
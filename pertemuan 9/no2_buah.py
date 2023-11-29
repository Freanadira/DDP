nama_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def list_buah(buah):
    duplikasi = []
    for buah in nama_buah:
        duplikasi.append(buah)
        duplikasi.append(buah)

    return duplikasi

hasil = list_buah(nama_buah)

print('urutan sudah di duplikat jadi', hasil)
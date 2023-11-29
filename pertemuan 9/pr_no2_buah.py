nama_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def list_buah(buah):
    duplikasi = []
    for i in buah:
        duplikasi.append(i)
        duplikasi.append(i)

    return duplikasi

hasil = list_buah(nama_buah)

print('urutan sudah di duplikat jadi', hasil)
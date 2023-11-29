nama_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def list_buah(buah):
    urutan_terbalik = []
    #fungsi len untuk mengidentifikasi dan mengetahui seberapa panjang jumlah item atau anggota pada suatu objek
    for i in range (len(buah) -1,-1,-1):
        urutan_terbalik.append(buah[i])
        #menambahkan elemen ke list

    return urutan_terbalik

#manggil fungsi list buah untuk dapat urutan terbalik
hasil = list_buah(nama_buah)

print('urutan sudah di blik jadi', hasil)
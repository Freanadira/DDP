ket = input('''Pilih perhitungan yang ingin dilakukan
            1. keliling trapesium
            2. luas trapesium
            pilihan = ''')

if ket == 'keliling trapesium':
    atas = int(input('masukan sisi sejajar bagiam atas = ' ))
    bawah = int(input('masukan sisi sejajar bagian bawah (alas) = '))
    kiri = int(input('masukan sisi tidak sejajar sebelah kiri = '))
    kanan = int(input('masukan sisi tidak sejajar sebelah kanan = '))
    keliling = atas + bawah + kiri + kanan
    print('keliling trapesium dengan sisi sejajar', atas,'dan', bawah, 'dan sisi tidak sejajar', kiri,'dan', kanan,  'adalah', int(keliling) )
elif ket == 'luas trapesium':
    atas = int(input('masukan sisi sejajar bagiam atas = ' ))
    bawah = int(input('masukan sisi sejajar bagian bawah (alas) = '))
    tinggi = int(input('masukan tinggi trapesium = '))
    luas = 1/2 * tinggi *(atas + bawah)
    print('keliling trapesium dengan sisi sejajar bagian atas', atas,'sisi sejajar bagian bawah', bawah, 'dengan tinggi trapesium', tinggi, 'adalah', int(luas) )
else:
    print = ('')
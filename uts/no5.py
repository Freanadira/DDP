angka1 = int(input('masukan angka pertama = '))
operator = input('''pilihlah operator yang ingin digunakan
     1. tambah (+)
     2. kurang (-)
     3. bagi (/)
     4. kali (*)
     5. pangkat (**)
    pilihan = ''')
angka2 = int(input('masukan angka kedua = '))

if operator == 'tambah':
    hitungan = angka1 + angka2
elif operator == 'kurang':
    hitungan = angka1 - angka2
elif operator == 'bagi':
    hitungan = angka1 / angka2
elif operator == 'kali':
    hitungan = angka1 * angka2
elif operator == 'pangkat':
    hitungan = angka1 ** angka2
else:
    hitungan = 'tidak bisa menjalankan hitungan'

print('hasil perhitungan', angka1, 'dan', angka2, 'dengan pilihan operator', operator, 'adalah', hitungan)

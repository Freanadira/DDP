hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

def predikatlulus(data):
    #menggunakan list untuk mengambil data dari hasil_akhir
    #yang memiliki nilai lenih dari 65
    lulus = [mahasiswa['nama']
        for mahasiswa in data
        if mahasiswa['nilai'] > 65]
    return lulus

#memanggil fungsi lulus untuk memberikan predikat lulus
#pada nama yang memiliki nilai lebih dari 65
hasil = predikatlulus(hasil_akhir)
print('siswa yang lulus : ', hasil)
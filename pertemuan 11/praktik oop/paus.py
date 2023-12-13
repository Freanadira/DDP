class paus:
    #atribut class
    nama = ''
    warna = ''
    umur = 0

    #constructor
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur

    #method untuk menampilkan data
    def data_paus(self):
        print(f'nama paus: {self.nama}')
        print(f'warna paus: {self.warna}')
        print(f'umur paus: {self.umur} tahun')
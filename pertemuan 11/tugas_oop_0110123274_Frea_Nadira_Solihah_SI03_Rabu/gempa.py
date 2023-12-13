class gempa:
    lokasi = ''
    skala = 0

    #construction
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    
    #method
    def data_gempa(self):
        if self.skala < 2:
            keterangan =  'dampak gempa tidak terasa'
        elif (self.skala >= 2 and self.skala <= 4):
            keterangan = 'dampak gempa bangunan retak-retak'
        elif (self.skala >= 4 and self.skala <= 6):
            keterangan = 'dampak gempa bangunan roboh'
        elif self.skala > 6:
            keterangan = 'dampak gempa bangunan roboh dan berpotensi sunami'
        else:
            keterangan = 'salah memasukan skala'
        print(f'Telah terjadi gempa di {self.lokasi} dengan skala {self.skala} {keterangan}')

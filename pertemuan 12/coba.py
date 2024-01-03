class manusia:
    def __init__(self, fnama, lnama):
        self.fnama = fnama
        self.lnama = lnama

    def cetak(self):
        print("Nama saya", self.fnama, self.lnama)

class Staff(manusia):
    def bekerja(self):
        print("saya pekerja keras")

class Pelajar(manusia):
    def __init__(self, fnama, lnama, prodi, angkatan):
        super().__init__(fnama, lnama)
        self.prodi = prodi
        self.angkatan = angkatan

    def belajar(self):
        print("saya adalah pelajar")

#objek manusia
x = manusia("Nada", "Indah")
x.cetak

#objek staff
y = Staff("Dedi", "Rajat")
y.cetak()
y.bekerja()

#objek pelajar
danu = Pelajar("Danu", "Setiawan", "Sistem Informasi", "STT Nurul Fikri")
danu.cetak()
danu.belajar()
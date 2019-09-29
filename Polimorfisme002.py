class Tanaman(object):
    def __init__ (self, nama, jenis, asal):
        self.nama = nama
        self.jenis = jenis
        self.asal = asal
    def cetakData(self):
        print("Nama Tanaman\t: ", self.nama)
        print("Jenis Tanaman\t: ", self.jenis)
        print("Negara Asal\t: ", self.asal)

class TanamanHias(Tanaman):
    def __init__ (self, nama, jenis, asal, warnabunga):
        super(TanamanHias, self).__init__(nama, jenis, asal)
        self.warnabunga = warnabunga
    def cetakData(self):
        super(TanamanHias, self).cetakData()
        print("Warna Bunga\t: ", self.warnabunga)

class TanamanPangan(Tanaman):
    def __init__(self, nama, jenis, asal, penghasil):
        super(TanamanPangan, self).__init__(nama, jenis, asal)
        self.penghasil= penghasil
    def cetakData(self):
        super(TanamanPangan, self).cetakData()
        print("Negara Penghasi terbesar adalah\t: ", self.penghasil)
def main():
    obj = Tanaman('NORMAL', 'Hias Dan Pangan', 'NORMAL')
    print('KELAS INDUK')
    obj.cetakData()
    del obj

    obj = TanamanHias('Bunga Kamboja', 'Tanaman Hias', 'Kamboja', 'Putih')
    print("\nTANAMAN HIAS============")
    obj.cetakData()
    del obj

    obj = TanamanPangan('Gandum', 'Tanaman Pangan', 'Amerika', 'Uni-Eropa')
    print("\nTANAMAN PANGAN=============")
    obj.cetakData()
    del obj

if __name__ == "__main__":
    main()

class Ogrenci():
    def __init__(self, adi, soyadi, numarasi):
        self.ad = adi
        self.soyad = soyadi
        self.numara = numarasi

    def bilgiler(self):
        print("Adi: {}\nSoyadi: {}\nNumarasi: {}".
              format(self.ad, self.soyad, self.numara))


def yazdir():
    print("Merhaba Dünya")

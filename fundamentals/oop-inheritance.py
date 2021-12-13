class Kullanici:
    def __init__(self, adi, soyadi, numara):
        self.adi = adi
        self.soyadi = soyadi
        self.numara = numara

    def giris(self):
        print("Giriş yapıldı")

    def cikis(self):
        print("Çıkış yapıldı")


class Akademisyen(Kullanici):
    pass


class Personel(Kullanici):
    pass


class Ogrenci(Kullanici):
    pass


class AkademisyenOverrided(Kullanici):

    def __init__(self, adi, soyadi, numara, dogum_tarihi):
        super().__init__(adi, soyadi, numara)
  
    # def __init__(self, adi, soyadi, numara, dogum_tarihi): ##super olmasaydı
        # self.adi = adi
        # self.soyadi = soyadi
        # self.numara = numara
        self.dogum_tarihi = dogum_tarihi


akademisyen = Akademisyen("Mustafa", "Kapucu", "5454")
personel = Personel("Personel Mustafa", "Personel Kapucu", 446)
ogrenci = Ogrenci("Öğrenci Mustafa", "Öğrenci Kapucu", 4646)

print("Akademisyen")
print(akademisyen.adi)
print(akademisyen.soyadi)
print(akademisyen.numara)

print("Personel")
print(personel.adi)
print(personel.soyadi)
print(personel.numara)

print("Öğrenci")
print(ogrenci.adi)
print(ogrenci.soyadi)
print(ogrenci.numara)

overridedAkadenmisyen = AkademisyenOverrided(
    "Mustafa Override", "Kapucu", 24654, 2008)
print(overridedAkadenmisyen.adi, overridedAkadenmisyen.dogum_tarihi)
overridedAkadenmisyen.giris()

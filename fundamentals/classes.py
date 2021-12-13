class Araba:
    # def __init__(self):
    #     print("Yapıcı fonk. çalıştı")

    def __init__(self, marka="Renault", renk="Gri", plaka="34aa45", hiz=90):
        self.marka = marka
        self.renk = renk
        self.plaka = plaka
        self.hiz = hiz

    marka = ""
    renk = ""
    plaka = ""
    hiz = 0

    def hizArttir(self):
        self.hiz += 10
        return self.hiz


# sınıftan nesne türetme

# araba1 = Araba()
# araba1.marka = "Ford"
# araba1.renk = "Siyah"
# araba1.plaka = "34bb45"

# araba2 = Araba()
# araba2.marka = "BMW"
# araba2.renk = "Beyaz"
# araba2.plaka = "35aa45"


# araba1 = Araba("Renault", "Gri", "34aa45", 60)
araba1 = Araba(marka="Peugeout", renk="Gri", hiz=100, plaka="35pp89")
# araba1 = Araba()


print("-----Araba 1-------")
print("Marka: {} \nRenk : {} \nPlaka : {}".format(
    araba1.marka, araba1.renk, araba1.plaka))
araba1.hizArttir()
print("Hız : ", araba1.hiz)

# print("-----Araba 2-------")
# print("Marka: {} \nRenk : {} \nPlaka : {}".format(
#     araba2.marka, araba2.renk, araba2.plaka))
# araba2.hizArttir()
# print("Hız : ", araba2.hiz)

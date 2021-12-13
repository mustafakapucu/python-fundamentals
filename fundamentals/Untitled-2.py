# a = 3
# b = 3.14
# c = "Python"
# d = [1, 2, 3, 4, 5, "Python"]
# e = (1, 2, 3, 4, 5, "Python")
# f = {"Elma": 3, "Armut": 4, "Kiraz": 5}
# g = False

# print(type(d))
# print(type(e))
# print(type(f))

# print(a+b)
# print(b//a)

# print (c*10)
# print ("*"*10)

# a = "Python"
# b = [1, 2, 3, 4, 5, 6, 7]

# print(a[0])
# print(b[2])
# print(len(a))
# print(b[len(b)-1])


# print(a[0:2])
# print(a[2:])
# print(b[0:6:2])
# print(b[::2])

# a = {"Elma": 3, "Armut": 4, "Kiraz": 5}
# print(a["Elma"])
# print(a["Elmaa"])

# 2

# a = int(input("a:"))
# b = int(input("b:"))
# c = float(input("c:"))
# print("Toplam", a+b+c)


# yas = int(input("Yaşınızı giriniz:"))

# if yas < 18:
#     print("Mekana giremezsiniz...")
# elif yas > 60:
#     print("Yallah huzurevine ehtiyar")
# else:
#     print("Hoşgeldiniz")

# a = 3
# b = 4

# if a == 3 and b == 5:
#     print("True")

# i = 0

# while i < 10:
#     print("i:", i)
#     i += 1
#     i *= 3


# i = 0

# while (i < 10):
#     if i == 5:
#         break #continue de var
#     print("i:",i)
#     i += 1

# a = [1,2,3,4,5,6]

# for eleman in a:
#     print(eleman)

# for sayi in range(10, 50, 2):
#     print(sayi)


# def selamla():
#     print("Merhaba")
#     print("Nasılsın?")


# selamla()


# def selamla(isim="İsimsiz"):
#     print("Merhaba ", isim)
#     print("Nasılsın?")

# selamla()
# selamla("Mustafa")


# def toplama(a, b, c):
#     print("Toplam:", a+b+c)


# toplama(1, 2, 3)


# def toplama(a, b, c):
#     return a+b+c


# toplam = toplama(1, 2, 3)
# print(toplam)


# liste = [1, 2, 3, 4, 5, 6]
# a = "araba"

# print(a.startswith("a"))
# a = a.replace("a","o")
# print(a)

# liste.append("Python")
# print(liste)
# liste.pop(1)
# print(liste)


# file = open("dosya.txt","a") #w içeriğin hepsini değiştirir #a ekleme yapar

# file.write("Naber Java")
# file.close()

# file = open("dosya.txt", "r")  # r read modu
# # file.seek(10)#otomatik olarak 10 karakter geçti
# # veri = file.read()
# # # veri = file.read(10) #ilk 10 karakteri okur
# # print(veri)

# for satir in file:
#     print(satir) #satır satır okuma
# file.close()


# class Account:
#     def __init__(self, isim, numara, bakiye):
#         self.isim = isim
#         self.numara = numara
#         self.bakiye = bakiye

#     def hesapBilgileri(self):
#         print("İsim :", self.isim)
#         print("Numara :", self.numara)
#         print("Bakiye :", self.bakiye)

#     def paraCek(self,miktar):
#         if self.bakiye - miktar <0:
#             print("Bakiye yetersiz.")
#         else:
#             self.bakiye-=miktar
#             print("Yeni bakiye : ", self.bakiye)
#     def paraYatir(self, miktar):
#         self.bakiye+=miktar
#         print("Yeni bakiye:",self.bakiye)


# account = Account("Mustafa Kapucu",1131,10000)

# account.hesapBilgileri()
# account.paraCek(10)
# account.paraCek(5000000)
# account.paraYatir(10)



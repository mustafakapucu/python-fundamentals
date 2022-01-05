import os

# result = dir(os)


# result = os.chdir("C:\\") #change dir
# result = os.getcwd()
# os.mkdir("newdir")


# result = os.listdir()
# result = os.listdir("C:\\")
# print(result)

# for dosya in os.listdir('C:\\'):
#     if dosya.endswith(".py"):
#         print(dosya)


# os.system("notepad.exe")   # uygulama çalıştırma 

#os.path dosya işlemleri
result = os.path.exists("files.py")
result = os.path.isdir("files.py")
result = os.path.isfile("files.py")
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")

print(result)




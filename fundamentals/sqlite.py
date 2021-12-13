import sqlite3
from typing import Text

# database_connect = sqlite3.connect("sinif.db")
# auto close için
with sqlite3.connect("sinif.db") as database_connect:

    imlec = database_connect.cursor()

    imlec.execute(
        """CREATE TABLE IF NOT EXISTS ogrenciler(ogr_no INTEGER ,ogr_adi TEXT,ogr_soyadi TEXT,ogr_bolum TEXT)""")
    imlec.execute(
        """INSERT INTO ogrenciler VALUES(12,"Mustafa","KAPUCU","Bilgisayar Mühendisliği") """)
    database_connect.commit()
# database_connect.close() #auto close için


    imlec.execute("""SELECT * FROM ogrenciler""")
    ogrenciler = imlec.fetchall()
    # print(ogrenciler)

    for ogrenci in ogrenciler:
        print(ogrenci)
        print(ogrenci[0])
        print(ogrenci[1])


import random
import os
from sqlite3.dbapi2 import Cursor, Error
import time
import sys
import tkinter 
import sqlite3
from tkinter import messagebox
import datetime

# simdiki tarihi bulma --> datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def kayitac() :
    olustur = sqlite3.connect("Kayit.db")
    baglanti = olustur.cursor()
    baglanti.execute("""CREATE TABLE IF NOT EXISTS"Sinema" (
	"SıraNo"	INTEGER UNIQUE,
	"Bilet No"	INTEGER NOT NULL,
	"isim"	TEXT NOT NULL,
	"Soyisim"	TEXT NOT NULL,
	"Film Adi"	TEXT NOT NULL,
	"Salon No"	TEXT NOT NULL,
	"Koltuk No"	TEXT NOT NULL,
    "Kayit Tarihi" TEXT,
	PRIMARY KEY("SıraNo" AUTOINCREMENT));""")
    olustur.commit()
    olustur.close() 

#-------------KAYIT PANOSU ----------------------
def biletkontrol () :
    Bilet_No = random.randint(1000000000, 9999999999)
    olustur = sqlite3.connect("Kayit.db")
    baglanti = olustur.cursor()
    tamami = baglanti.execute("SELECT 'Bilet No' from Sinema")
    olustur.commit()
    if Bilet_No not in tamami.fetchall():
        return Bilet_No

def koltukkayit (filmadi ,salonadi, koltuk) :
    salonadi = salonadi.upper()
    koltuk = koltuk.upper()

    pano = tkinter.Tk()
    pano.title("Kayit Panosu")
    pano.geometry("400x400+400+300")

    tkinter.Label(pano, text="Film Adı    ---------", fg="white").place(x=50 , y=20)        #film adi label
    tkinter.Label(pano, text=filmadi, fg="white").place(x=175 , y=20)                       #film adi 
    tkinter.Label(pano, text="Salon No    ---------", fg="white").place(x=50 , y=50)        #salon adi label
    tkinter.Label(pano, text=salonadi, fg="white").place(x=175 , y=50)                      #salon adi
    tkinter.Label(pano, text="Koltuk No   ---------", fg="white").place(x=50 , y=80)        #koltuk numarası label
    tkinter.Label(pano, text=koltuk, fg="white").place(x=175, y=80)                         #koltuk numarası

    tkinter.Label(pano, text="Bilet No    ---------").place(x=50 , y=110) 
    Bilet_No = biletkontrol()                                                        #bilet no label
    tkinter.Label(pano, text=Bilet_No).place(x=175, y=110)                            #bilet no (Benzersiz bilet numarası secilecek)
    
    tkinter.Label(pano, text="İsim        ---------", fg="white").place(x=50,y=150)    
    isim= tkinter.Entry(pano, bg="white", fg="black")
    isim.place(x=175, y=150)

    tkinter.Label(pano, text="Soyisim     ---------", fg="white").place(x=50,y=200)
    soyisim = tkinter.Entry(pano, bg="white", fg="black")
    soyisim.place(x=175,y=200)

    def musterikayit (filmadi ,salonadi, koltuk,BiletNo,isim,soyisim):
        ekle = "INSERT INTO Sinema ('Bilet No','isim','Soyisim','Film Adi','Salon No','Koltuk No','Kayit Tarihi') VALUES ('{}','{}','{}','{}','{}','{}','{}')"
        zaman = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        olustur = sqlite3.connect("Kayit.db")
        baglan = olustur.cursor()
        baglan.execute(ekle.format(BiletNo, isim.upper(), soyisim.upper(), filmadi, salonadi, koltuk, zaman))
        try :
            olustur.commit()
            olustur.close()
            pano.destroy()
            messagebox.showinfo("Kayit Basarili","{} Kayit Edilmiştir".format(BiletNo))
        except :
            pano.destroy()
            messagebox.showinfo("HATA","Veritabani Kayit Hatasi!")

    TTT=tkinter.Button(pano , text="Kaydet" , command=lambda:musterikayit(filmadi ,salonadi, koltuk, Bilet_No, isim.get(), soyisim.get()))
    TTT.place(x=175,y=250)
    pano.mainloop()



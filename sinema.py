#!/usr/bin/python3


import sqlite3
import tkinter
import os
import time
import sys
from tkinter import font
from tkinter import messagebox
from  koltuklar import koltuksec
from Veritabani import kayitac




#------SQL VERİTABANI OLUSTURULUCAK-------------
kayitac()

#--------FİLM BUTONU SONRASI , SALON PANOSU BURADA ACİLİYOR------------

def salonacmak(filmadi) :
    salon= tkinter.Tk()
    salon.title("SALON")
    salon.geometry("600x200+300+300")
    tkinter.Label(salon , text=(filmadi+" Film Salonu ")).place(x=150 , y=10)

    tkinter.Button(salon , text="Salon 1" ,command=lambda : koltuksec (filmadi, "SALON 1"), width=15 , height=4 ).place(x=10, y=50)
    tkinter.Label(salon , text="Toplam Koltuk : 25").place(x=25,y=145)
    kalankoltuk = tkinter.Label(salon , text="Boş Koltuk : ")
    kalankoltuk.place(x=25,y=175)

    tkinter.Button(salon , text="Salon 2" ,command=lambda : koltuksec (filmadi, "SALON 2") , width=15 , height=4 ).place(x=220, y=50)
    tkinter.Label(salon , text="Toplam Koltuk : 25").place(x=235,y=145)
    kalankoltuk = tkinter.Label(salon , text="Boş Koltuk : ")
    kalankoltuk.place(x=235,y=175)

    tkinter.Button(salon , text="Salon 3" ,command=lambda :koltuksec (filmadi, "SALON 3") , width=15 , height=4 ).place(x=430, y=50)
    tkinter.Label(salon , text="Toplam Koltuk : 25").place(x=445,y=145)
    kalankoltuk = tkinter.Label(salon , text="Boş Koltuk : ")
    kalankoltuk.place(x=445,y=175)
    salon.mainloop()


#----------CİKİS İSLEMLERİ -------------

def cikisislemleri () :    
    pen.destroy()
    try :
        pen.destroy()
        yeni.destroy()
    except :
        sys.exit()


#-----------FİLM EKLEME YERİ ------------------------

def filmayar () : 
    ayarbuton["state"] = "disabled"
    yeni = tkinter.Tk()
    yeni.title("Film Ayarlari")
    yeni.geometry("400x200+200+200")

    tkinter.Label(yeni, text="Film1 Adı Giriniz --> ").place(x=10,y=10)
    film1giris = tkinter.Entry(yeni , bg="white", fg="black")
    film1giris.place(x=150 , y=10)

    tkinter.Label(yeni, text="Film2 Adı Giriniz --> ").place(x=10,y=35)
    film2giris = tkinter.Entry(yeni , bg="white", fg="black")
    film2giris.place(x=150 , y=35)
    
    tkinter.Label(yeni, text="Film3 Adı Giriniz --> ").place(x=10,y=60)
    film3giris = tkinter.Entry(yeni , bg="white", fg="black")
    film3giris.place(x=150 , y=60)
    
    tkinter.Label(yeni, text="Film4 Adı Giriniz --> ").place(x=10,y=85)
    film4giris = tkinter.Entry(yeni , bg="white", fg="black")
    film4giris.place(x=150 , y=85)
    
    tkinter.Label(yeni, text="Film5 Adı Giriniz --> ").place(x=10,y=110)
    film5giris = tkinter.Entry(yeni , bg="white", fg="black")
    film5giris.place(x=150 , y=110)
    def filmkayit() :
        global film1 , film2, film3, film4, film5
        film1isim = str(film1giris.get().upper())
        film2isim = str(film2giris.get().upper())
        film3isim = str(film3giris.get().upper())
        film4isim = str(film4giris.get().upper())
        film5isim = str(film5giris.get().upper())
        film1.configure(state="normal", text=film1isim)
        film2.configure(state="normal", text=film2isim)
        film3.configure(state="normal", text=film3isim)
        film4.configure(state="normal", text=film4isim)
        film5.configure(state="normal", text=film5isim)
        yeni.destroy()
        ayarbuton["state"] = "normal"

    filmkayit = tkinter.Button(yeni , text="Kaydet", command=filmkayit )
    filmkayit.place(x=150, y=150)
    yeni.mainloop()

# ---------- ARAMA PANOSU -----------    

def AramaIslemi() :
    aramapanosu = tkinter.Tk()
    aramapanosu.geometry("400x400+200+200")
    aramapanosu.title("Arama Panosu")

    tkinter.Label(aramapanosu, text="Bilet Numarası ", font=("Ariel",18)).place(x=100,y=40)
    biletnumarasi = tkinter.Entry(aramapanosu, bg="white", fg="black")
    biletnumarasi.place(x=110,y=90)

    def KayitSil (bilet) :
        kayit_sil = 'DELETE FROM Sinema WHERE "Bilet No" = "{}" '
        olustur = sqlite3.connect("Kayit.db")
        imlec = olustur.cursor()
        imlec.execute(kayit_sil.format(bilet))
        
        try :
            olustur.commit()
            messagebox.showinfo("Veri Silindi" , "{} numarali veri silindi".format(bilet))
            olustur.close()
            aramapanosu.destroy()
        except :
            olustur.close()
            messagebox.showerror("HATA","VeriTabani Baglanti Hatasi")
            print(kayit_sil.format(bilet))
    
    def BiletNoArama (bilet) :
        mesaj = """\nBilet No ----- {}\nİsim     ----- {}\nSoyisim  ----- {}\nFilm Adi ----- {}\nSalon No ----- {}\nKoltuk No----- {}\nKayit Tarih -- {}\n"""
        arama_metni = 'SELECT "Bilet No","isim","Soyisim","Film Adi","Salon No","Koltuk No","Kayit Tarihi" FROM Sinema WHERE "Bilet No" = "{}" '
        olustur = sqlite3.connect("Kayit.db")
        baglan = olustur.cursor()
        aranan = baglan.execute(arama_metni.format(bilet))
        olustur.commit()
        liste = aranan.fetchall()

        try :
            tamam = list(liste[0])
            Sonuc["text"] = mesaj.format(tamam[0], tamam[1], tamam[2], tamam[3], tamam[4], tamam[5], tamam[6])
            Duzenle["state"] = "normal"
        except IndexError:
            Sonuc["text"] = "Bulunamadi"

    tkinter.Button(aramapanosu , text="Bilet No Ara", command= lambda : BiletNoArama(biletnumarasi.get()),  width=10, height=2).place(x=150,y=140)

    Sonuc = tkinter.Label(aramapanosu, text="")
    Sonuc.place(x=60, y=200)

    Duzenle = tkinter.Button(aramapanosu, text="KayitSil", command=lambda : KayitSil(biletnumarasi.get()), state="disabled")
    Duzenle.place(x=150, y=350)

    aramapanosu.mainloop()



#----------ANA MENÜ --------------

pen = tkinter.Tk()
pen.title("Cinema Salonu")
pen.geometry("420x600+100+100")

filmayari = tkinter.Frame(pen, width=380 , height=100 ,bg="yellow")
filmayari.place(x=20, y=10)

ayarbuton = tkinter.Button(filmayari, text="Film Ekle" , command=filmayar, width = 10,height=2)
ayarbuton.place(x=45,y=25)

arama = tkinter.Button(filmayari , text="Arama",width=10 , height=2, command=AramaIslemi)
arama.place(x=220, y=25)

#-------------FİLM BUTONLARI---------------------------------------------
filmsolkenar = 40

filmsecenekler = tkinter.Frame(pen , width=400 , height=320, bg="green")
filmsecenekler.place(x=10,y=120)

film1 = tkinter.Button(filmsecenekler, command=lambda : salonacmak (film1["text"]), text="Film1",width=30 , height=2 , bg="black" , fg="white", state="disabled")
film1.place(x=filmsolkenar+10,y=10)

film2 = tkinter.Button(filmsecenekler, command=lambda : salonacmak (film2["text"]), text="Film2",width=30 , height=2 , bg="black" , fg="white", state="disabled")
film2.place(x=filmsolkenar+10,y=70)

film3 = tkinter.Button(filmsecenekler, command=lambda : salonacmak (film3["text"]),  text="Film3",width=30 , height=2 , bg="black" , fg="white", state="disabled")
film3.place(x=filmsolkenar+10,y=130)

film4 = tkinter.Button(filmsecenekler,  command=lambda : salonacmak (film4["text"]), text="Film4",width=30 , height=2 , bg="black" , fg="white", state="disabled")
film4.place(x=filmsolkenar+10,y=190)

film5 = tkinter.Button(filmsecenekler, command=lambda : salonacmak (film5["text"]),  text="Film5",width=30 , height=2 , bg="black" , fg="white", state="disabled")
film5.place(x=filmsolkenar+10,y=250)

#---------------------------------------------

cikis = tkinter.Frame(pen, width=400 , height=130 , bg ="red" )
cikis.place(x=10 , y=450)

tkinter.Button(cikis, text="Cikis" , command = cikisislemleri , width=15 , height=2, bg="black", fg="white", font=("Ariel" , 20)).place(x=50,y=25)

pen.mainloop()
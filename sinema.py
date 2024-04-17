import os
import time
import sys
import tkinter as TK
import sqlite3 as sql 
import random
import datetime
from tkinter import messagebox
from sqlite3.dbapi2 import Cursor, Error

global koltukSec

def CreateDatabase():
	conn = sql.connect("Sinema.sql")
	conn.cursor()
	conn.execute("""CREATE TABLE IF NOT EXISTS "Sinema" (
		"SıraNo"	INTEGER UNIQUE,
		"BiletNo"	INTEGER NOT NULL,
		"isim"	TEXT NOT NULL,
		"Soyisim"	TEXT NOT NULL,
		"FilmAdi"	TEXT NOT NULL,
		"KoltukNo"	TEXT NOT NULL,
		"KayitTarihi" TEXT,
		PRIMARY KEY("SıraNo" AUTOINCREMENT));""")
	conn.commit()
	conn.close() 

def veriTabaniKayit (bilet_no, isim , soyisim ,filmadi, koltukno) :
	zaman = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	ekle = "INSERT INTO Sinema ('BiletNo','isim','Soyisim','FilmAdi','KoltukNo','KayitTarihi') VALUES ('{}','{}','{}','{}','{}','{}')"
	olustur = sql.connect("Sinema.sql")
	baglan = olustur.cursor()
	baglan.execute(ekle.format(bilet_no, isim , soyisim ,filmadi, koltukno, zaman))
	try :
		olustur.commit()
		olustur.close()
		messagebox.showinfo("Kayit Basarili","{} Kayit Edilmiştir".format(bilet_no))
		koltukSec(filmadi ) 
		panel.destroy()
	except :
		messagebox.showinfo("HATA","Veritabani Kayit Hatasi!")
	
def biletkontrol () :
	for ata in range(10):
		Bilet_No = random.randint(1000000000, 9999999999)
		olustur = sql.connect("Sinema.sql")
		baglanti = olustur.cursor()
		tamami = baglanti.execute("SELECT 'BiletNo' FROM Sinema")
		olustur.commit()
		if Bilet_No not in tamami.fetchall():
			olustur.close()
			return Bilet_No

def koltukkayit(filmadi, koltukno) :
	global panel

	panel = TK.Tk()
	panel.title("Panel")
	panel.geometry("500x500+500+200")
	
	TK.Label(panel, text="Film Adi").grid(row=0, column=0, padx=50, pady=10)
	TK.Label(panel, text=filmadi).grid(row=0, column=1, padx=50, pady=10)     
	TK.Label(panel, text="Koltuk No").grid(row=1, column=0, padx=50, pady=10)
	TK.Label(panel, text=koltukno).grid(row=1, column=1, padx=50, pady=10)                    
	TK.Label(panel, text="Bilet No").grid(row=3, column=0, padx=50, pady=10) 
	bilet_no = biletkontrol()                                                    
	
	TK.Label(panel, text=bilet_no).grid(row=3, column=1, padx=50, pady=10)                      
	TK.Label(panel, text="İsim").grid(row=4, column=0, padx=50, pady=10)    
	
	isim= TK.Entry(panel,)
	isim.grid(row=4, column=1, padx=50, pady=10)

	TK.Label(panel, text="Soyisim").grid(row=5, column=0, padx=50, pady=10)
	soyisim = TK.Entry(panel, fg="black")
	soyisim.grid(row=5, column=1, padx=50, pady=10)

	TK.Button(panel, text="Kaydet", command=lambda: veriTabaniKayit(bilet_no, isim.get().upper() , soyisim.get().upper(),filmadi, koltukno ) ).grid(row=7, column=1, padx=5, pady=15)


	panel.mainloop()
	
def listele (filmadi) :
	sorgula = "SELECT * FROM Sinema WHERE FilmAdi='{}'"
	sor = sql.connect("Sinema.sql")
	baglan = sor.cursor()
	baglan.execute(sorgula.format(filmadi))
	veriler = baglan.fetchall()
	baglan.close()
	listelePanel = TK.Tk()
	listelePanel.geometry("700x350+100+200")
	listelePanel.title("Sinema Müşteri Listesi")
	
	baslik = TK.Frame(listelePanel, width=700 ,height=50, bg="skyblue")
	baslik.place(x=0, y=0)
	TK.Label(baslik, text="Bilet Numarasi" ,bg = "skyblue").place(x=30, y=18)
	TK.Label(baslik, text="İsim" ,bg = "skyblue").place(x=150, y=18)
	TK.Label(baslik, text="Soyisim" ,bg = "skyblue").place(x=210, y=18)
	TK.Label(baslik, text="Film Adi" ,bg = "skyblue").place(x=290, y=18)
	TK.Label(baslik, text="Koltuk No" ,bg = "skyblue").place(x=380, y=18)
	TK.Label(baslik, text="Kayit Tarihi" ,bg = "skyblue").place(x=500, y=18)

	sayi = int(60)
	for ata in veriler :
		TK.Label(listelePanel, text=ata[1]).place(x=35, y=sayi)
		TK.Label(listelePanel, text=ata[2]).place(x=150, y=sayi)
		TK.Label(listelePanel, text=ata[3]).place(x=225, y=sayi)
		TK.Label(listelePanel, text=ata[4]).place(x=300, y=sayi)
		TK.Label(listelePanel, text=ata[5]).place(x=375, y=sayi)
		TK.Label(listelePanel, text=ata[6]).place(x=500, y=sayi)
		sayi+=30


	TK.Button(listelePanel, command= lambda : listelePanel.destroy(), bg="red", width=6, height=2 ,text="Kapat").pack(side="bottom", pady=15)
	listelePanel.mainloop()

def koltukKontrol (filmadi) :
	sorgula = "SELECT KoltukNo FROM Sinema WHERE FilmAdi='{}'"
	sor = sql.connect("Sinema.sql")
	baglan = sor.cursor()
	baglan.execute(sorgula.format(filmadi))
	veriler = baglan.fetchall()
	koltukliste = []
	for ata in veriler :
		koltukliste.append(ata[0])
	baglan.close()

	return koltukliste
		
def veriguncelle ():
	yenisim = isimgun.get().upper()
	yenisoysim = soyisimgun.get().upper()
	gunconn = sql.connect("Sinema.sql")
	gunconn.cursor()
	gunconn.execute("UPDATE Sinema SET isim='{}', soyisim='{}' WHERE BiletNo='{}'".format(yenisim, yenisoysim, biletNumarasi))
	gunconn.commit()
	gunconn.close()
	musteriPanel.destroy()

def verisil (secilenFilm) :
	gunconn = sql.connect("Sinema.sql")
	gunconn.cursor()
	gunconn.execute("DELETE FROM Sinema  WHERE BiletNo='{}'".format( biletNumarasi))
	gunconn.commit()
	gunconn.close()
	musteriPanel.destroy()
	koltukSec(secilenFilm ) 

def guncelle (filmadi, koltukno) :
	global isimgun, soyisimgun, biletNumarasi , musteriPanel
	musteri = []
	gun = sql.connect("Sinema.sql")
	guncursor = gun.cursor()
	soru = "SELECT * FROM Sinema WHERE FilmAdi='{}' and KoltukNo='{}'"
	guncursor.execute(soru.format(filmadi, koltukno))
	musteriler = guncursor.fetchall()

	for ata in musteriler[0] :
		musteri.append(ata)
	guncursor.close()
	biletNumarasi = musteri[1]
	musteriPanel = TK.Tk()
	musteriPanel.geometry("400x400+300+300")
	musteriPanel.title("Musteri Bilgileri Güncelleme")
	TK.Label(musteriPanel, text="Bilet Numarası").grid(row=0, column=0, padx=10, pady=10)
	TK.Label(musteriPanel, text="İsim").grid(row=1, column=0, padx=10, pady=10)
	TK.Label(musteriPanel, text="Soyisim").grid(row=2, column=0, padx=10, pady=10)
	TK.Label(musteriPanel, text="Film Adı").grid(row=3, column=0, padx=10, pady=10)
	TK.Label(musteriPanel, text="Koltuk Numarası").grid(row=4, column=0, padx=10, pady=10)
	TK.Label(musteriPanel, text="Kayit Tarihi").grid(row=5, column=0, padx=10, pady=10)
	
	TK.Label(musteriPanel, text=musteri[1]).grid(row=0, column=1, padx=10, pady=10)
	isimgun = TK.Entry(musteriPanel)
	isimgun.insert(0, '{}'.format(musteri[2]))
	isimgun.grid(row=1, column=1, padx=10, pady=10)
	
	soyisimgun= TK.Entry(musteriPanel)
	soyisimgun.insert(0, '{}'.format(musteri[3]))
	soyisimgun.grid(row=2, column=1, padx=10, pady=10)
	TK.Label(musteriPanel, text=musteri[4]).grid(row=3, column=1, padx=10, pady=10)
	TK.Label(musteriPanel, text=musteri[5]).grid(row=4, column=1, padx=10, pady=10)
	TK.Label(musteriPanel, text=musteri[6]).grid(row=5, column=1, padx=10, pady=10)

	TK.Button (musteriPanel, text="Guncelle" ,command=veriguncelle , bg="green" , height=2, width=7).grid(row=7, column=0, padx=10, pady=10)
	TK.Button (musteriPanel, text="Sil" ,command= lambda : verisil (musteri[4]) , bg="red" , height=2, width=7).grid(row=7, column=1, padx=10, pady=10)

	musteriPanel.mainloop()

def koltukSec(filmadi ) :
	
	global koltuk1,koltuk2,koltuk3,koltuk4,koltuk5,koltuk6,koltuk7,koltuk8,koltuk9,koltuk10,koltuk11,koltuk12,koltuk13,koltuk14,koltuk15,koltuk16,koltuk17,koltuk18,koltuk19,koltuk20
	koltukliste = koltukKontrol(filmadi)
	
	perde = TK.Frame(menu, width=460, height=100, bg="red").place(x=225,y=10)
	TK.Label(perde, text="Burasi Sahne").place(x=350, y=50)	
	
	koltuk1 = TK.Button(menu, command=lambda : koltukkayit(filmadi,  "Koltuk1"), text="1" ,width=5, height=3, bg="green")
	koltuk1.place(x=225,y=125)
	
	koltuk2 = TK.Button(menu, command=lambda : koltukkayit(filmadi,  "Koltuk2"), text="2" ,width=5, height=3, bg="green")
	koltuk2.place(x=325,y=125)

	koltuk3 = TK.Button(menu,command=lambda : koltukkayit(filmadi,  "Koltuk3"), text="3" ,width=5, height=3, bg="green")
	koltuk3.place(x=425,y=125)

	koltuk4 = TK.Button(menu, command=lambda : koltukkayit(filmadi,  "Koltuk4"),text="4" ,width=5, height=3, bg="green")
	koltuk4.place(x=525,y=125)

	koltuk5 = TK.Button(menu,command=lambda : koltukkayit(filmadi,  "Koltuk5"), text="5" ,width=5, height=3, bg="green")
	koltuk5.place(x=625,y=125)

	koltuk6 = TK.Button(menu, command=lambda : koltukkayit(filmadi,  "Koltuk6"), text="6" ,width=5, height=3, bg="green")
	koltuk6.place(x=225,y=225)

	koltuk7 = TK.Button(menu, command=lambda : koltukkayit(filmadi,  "Koltuk7"), text="7" ,width=5, height=3, bg="green")
	koltuk7.place(x=325,y=225)

	koltuk8 = TK.Button(menu,command=lambda : koltukkayit(filmadi,  "Koltuk8"), text="8" ,width=5, height=3, bg="green")
	koltuk8.place(x=425,y=225)

	koltuk9 = TK.Button(menu, command=lambda : koltukkayit(filmadi,  "Koltuk9"),text="9" ,width=5, height=3, bg="green")
	koltuk9.place(x=525,y=225)

	koltuk10 = TK.Button(menu,command=lambda : koltukkayit(filmadi,  "Koltuk10"), text="10" ,width=5, height=3, bg="green")
	koltuk10.place(x=625,y=225)

	koltuk11 = TK.Button(menu, command=lambda : koltukkayit(filmadi,  "Koltuk11"), text="11" ,width=5, height=3, bg="green")
	koltuk11.place(x=225,y=325)

	koltuk12 = TK.Button(menu, command=lambda : koltukkayit(filmadi,  "Koltuk12"), text="12" ,width=5, height=3, bg="green")
	koltuk12.place(x=325,y=325)

	koltuk13 = TK.Button(menu,command=lambda : koltukkayit(filmadi,  "Koltuk13"), text="13" ,width=5, height=3, bg="green")
	koltuk13.place(x=425,y=325)

	koltuk14 = TK.Button(menu, command=lambda : koltukkayit(filmadi,  "Koltuk14"),text="14" ,width=5, height=3, bg="green")
	koltuk14.place(x=525,y=325)

	koltuk15 = TK.Button(menu,command=lambda : koltukkayit(filmadi,  "Koltuk15"), text="15" ,width=5, height=3, bg="green")
	koltuk15.place(x=625,y=325)

	koltuk16 = TK.Button(menu, command=lambda : koltukkayit(filmadi,  "Koltuk16"), text="16" ,width=5, height=3, bg="green")
	koltuk16.place(x=225,y=425)

	koltuk17 = TK.Button(menu, command=lambda : koltukkayit(filmadi,  "Koltuk17"), text="17" ,width=5, height=3, bg="green")
	koltuk17.place(x=325,y=425)

	koltuk18 = TK.Button(menu,command=lambda : koltukkayit(filmadi,  "Koltuk18"), text="18" ,width=5, height=3, bg="green")
	koltuk18.place(x=425,y=425)

	koltuk19 = TK.Button(menu, command=lambda : koltukkayit(filmadi,  "Koltuk19"),text="19" ,width=5, height=3, bg="green")
	koltuk19.place(x=525,y=425)

	koltuk20 = TK.Button(menu,command=lambda : koltukkayit(filmadi,  "Koltuk20"), text="20" ,width=5, height=3, bg="green")
	koltuk20.place(x=625,y=425)
	
	TK.Button(menu,text="Listele" ,command=lambda : listele(filmadi), bg="green", fg="black", width=5, height=2).place(x=400,y=600)

	if "Koltuk1" in koltukliste :
		koltuk1.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk1"), text="Güncelle")
	if "Koltuk2" in koltukliste :
		koltuk2.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk2"), text="Güncelle")
	if "Koltuk3" in koltukliste :
		koltuk3.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk3"), text="Güncelle")
	if "Koltuk4" in koltukliste :
		koltuk4.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk4"), text="Güncelle")
	if "Koltuk5" in koltukliste :
		koltuk5.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk5"), text="Güncelle")
	if "Koltuk6" in koltukliste :
		koltuk6.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk6"), text="Güncelle")
	if "Koltuk7" in koltukliste :
		koltuk7.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk7"), text="Güncelle")
	if "Koltuk8" in koltukliste :
		koltuk8.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk8"), text="Güncelle")
	if "Koltuk9" in koltukliste :
		koltuk9.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk9"), text="Güncelle")
	if "Koltuk10" in koltukliste :
		koltuk10.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk10"), text="Güncelle")
	if "Koltuk11" in koltukliste :
		koltuk11.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk11"), text="Güncelle")
	if "Koltuk12" in koltukliste :
		koltuk12.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk12"), text="Güncelle")
	if "Koltuk13" in koltukliste :
		koltuk13.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk13"), text="Güncelle")
	if "Koltuk14" in koltukliste :
		koltuk14.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk14"), text="Güncelle")
	if "Koltuk15" in koltukliste :
		koltuk15.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk15"), text="Güncelle")
	if "Koltuk16" in koltukliste :
		koltuk16.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk16"), text="Güncelle")
	if "Koltuk17" in koltukliste :
		koltuk17.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk17"), text="Güncelle")
	if "Koltuk18" in koltukliste :
		koltuk18.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk18"), text="Güncelle")
	if "Koltuk19" in koltukliste :
		koltuk19.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk19"), text="Güncelle")
	if "Koltuk20" in koltukliste :
		koltuk20.configure(bg="red" , command=lambda : guncelle (filmadi, "Koltuk20"), text="Güncelle")
	
def filmKaydetDef(filmler):
	try :
		if (bool(filmler[0])) :
			film1Button = TK.Button(menu, text=filmler[0] , fg="black", bg="green", width=16 , command=lambda : koltukSec(filmler[0]))
			film1Button.place(x=25, y=100)
		if (bool(filmler[1])) :
			film2Button = TK.Button(menu, text=filmler[1] , fg="black", bg="green", width=16 , command=lambda : koltukSec(filmler[1]))
			film2Button.place(x=25, y=135)
		if (bool(filmler[2])) :
			film3Button = TK.Button(menu, text=filmler[2] , fg="black", bg="green", width=16 , command=lambda : koltukSec(filmler[2]))
			film3Button.place(x=25, y=160)
		if (bool(filmler[3])) :
			film4Button = TK.Button(menu, text=filmler[3] , fg="black", bg="green", width=16, command=lambda : koltukSec(filmler[3]) )
			film4Button.place(x=25, y=185)
		if (bool(filmler[4])) :
			film5Button = TK.Button(menu, text=filmler[4] , fg="black", bg="green", width=16 , command=lambda : koltukSec(filmler[4]))
			film5Button.place(x=25, y=210)
		if (bool(filmler[5])) :
			film6Button = TK.Button(menu, text=filmler[5] , fg="black", bg="green", width=16 , command=lambda : koltukSec(filmler[5]))
			film6Button.place(x=25, y=235)
	except  :
		pass
	filmEklePanel.destroy()
	
def kayitkontrol () :
	
	
	filmler = []
	film1isim = str(film1.get().upper())
	film2isim = str(film2.get().upper())
	film3isim = str(film3.get().upper())
	film4isim = str(film4.get().upper())
	film5isim = str(film5.get().upper())
	film6isim = str(film6.get().upper())

	if (bool(film1isim)) :
		filmler.append(film1isim )
	if (bool(film2isim)) :
		filmler.append(film2isim)
	if (bool(film3isim)) :
		filmler.append(film3isim)
	if (bool(film4isim)) :
		filmler.append(film4isim)
	if (bool(film5isim)) :
		filmler.append(film5isim)
	if (bool(film6isim)) :
		filmler.append(film6isim)

	if (bool(filmler)):
		filmEkle.configure(state="disabled")

	filmKaydetDef(filmler)

def filmEklemeDef ():
	global filmEklePanel
	global film1, film2, film3, film4, film5, film6

	filmEklePanel= TK.Tk()
	filmEklePanel.geometry("350x300+300+100")
	filmEklePanel.title("Film Ekleme Paneli")
	TK.Label(filmEklePanel, text="Film Ekle -> ").place(x=25, y=25)
	film1 = TK.Entry(filmEklePanel ,bg="white", fg="black" )
	film1.place(x=150, y=25)
	TK.Label(filmEklePanel, text="Film Ekle -> ").place(x=25, y=50)
	film2 = TK.Entry(filmEklePanel ,bg="white", fg="black" )
	film2.place(x=150, y=50)
	TK.Label(filmEklePanel, text="Film Ekle -> ").place(x=25, y=75)
	film3 = TK.Entry(filmEklePanel ,bg="white", fg="black" )
	film3.place(x=150, y=75)
	TK.Label(filmEklePanel, text="Film Ekle -> ").place(x=25, y=100)
	film4 = TK.Entry(filmEklePanel ,bg="white", fg="black" )
	film4.place(x=150, y=100)
	TK.Label(filmEklePanel, text="Film Ekle -> ").place(x=25, y=125)
	film5 = TK.Entry(filmEklePanel ,bg="white", fg="black" )
	film5.place(x=150, y=125)
	TK.Label(filmEklePanel, text="Film Ekle -> ").place(x=25, y=150)
	film6 = TK.Entry(filmEklePanel ,bg="white", fg="black" )
	film6.place(x=150, y=150)
	
	TK.Button(filmEklePanel, text="Kaydet" , command= kayitkontrol , fg="black").place(x=100, y=200)
	filmEklePanel.mainloop()

def temizle ():
	evet = messagebox.askokcancel(title="Dikkat!!" , message="Veritabanı Tamamen Silinecektir.\n Onaylıyor musunuz ?")
	if evet :
		os.remove("Sinema.sql")
		menu.destroy()
		os.system("python3 Menu.py")
	else :
		pass

def menuDef(filmler):
	global menu, solFrame , filmEkle
	CreateDatabase()
	menu = TK.Tk()
	menu.geometry("700x700+100+100")
	menu.title("SİNEMA TABLOSU")

	solFrame = TK.Frame(menu, height=700, width=200, bg="yellow")
	solFrame.place(x=0,y=0)

	if(bool(filmler)) :
		filmEkle = TK.Button(solFrame, text="Film Ekle" , fg="black", width=15, command=filmEklemeDef, state="disabled")
		filmEkle.place(x=25,y=25)
		try :
			if (bool(filmler[0])) :
				film1Button = TK.Button(solFrame, text=filmler[0] , fg="black", bg="green", width=16 , command=lambda : koltukSec(filmler[0]))
				film1Button.place(x=25, y=100)
			if (bool(filmler[1])) :
				film2Button = TK.Button(solFrame, text=filmler[1] , fg="black", bg="green", width=16 , command=lambda : koltukSec(filmler[1]))
				film2Button.place(x=25, y=125)
			if (bool(filmler[2])) :
				film3Button = TK.Button(solFrame, text=filmler[2] , fg="black", bg="green", width=16 , command=lambda : koltukSec(filmler[2]))
				film3Button.place(x=25, y=150)
			if (bool(filmler[3])) :
				film4Button = TK.Button(solFrame, text=filmler[3] , fg="black", bg="green", width=16, command=lambda : koltukSec(filmler[3]) )
				film4Button.place(x=25, y=175)
			if (bool(filmler[4])) :
				film5Button = TK.Button(solFrame, text=filmler[4] , fg="black", bg="green", width=16 , command=lambda : koltukSec(filmler[4]))
				film5Button.place(x=25, y=200)
			if (bool(filmler[5])) :
				film6Button = TK.Button(solFrame, text=filmler[5] , fg="black", bg="green", width=16 , command=lambda : koltukSec(filmler[5]))
				film6Button.place(x=25, y=225)
		except  :
			pass
	else :
		filmEkle = TK.Button(solFrame, text="Film Ekle" , fg="black", width=15, command=filmEklemeDef)
		filmEkle.place(x=25,y=25)

	cikis = TK.Button(menu, text="Cikis",command= lambda : menu.destroy() , width=15, height=2, bg="red").place(x=25, y=600) 
	cikis = TK.Button(solFrame, text="Temizle",command= temizle , width=15, height=2, bg="pink").place(x=25, y=525) 
	menu.mainloop()

def basla () :
	global filmler
	filmler = []
	if "Sinema.sql" in os.listdir(".") :
		bag = sql.connect("Sinema.sql")
		baglan = bag.cursor()
		baglan.execute("SELECT FilmAdi  FROM Sinema GROUP BY FilmAdi")
		sinemaListe = baglan.fetchall()
		
		if bool(sinemaListe) :
			for ata in sinemaListe:
				filmler.append(ata[0])
			menuDef (filmler)
		else :
			menuDef(filmler)
	else :
		menuDef(filmler)
basla()

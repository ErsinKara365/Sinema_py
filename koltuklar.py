import tkinter
from Veritabani import koltukkayit
import sqlite3
import threading


#-----------------------OTURMA POZİSYONU MENUSU-------------------------------

def koltuksec (filmadi , salonadi) :
	koltuklar = ['KOLTUK 1', 'KOLTUK 2', 'KOLTUK 3', 'KOLTUK 4', 'KOLTUK 5', 'KOLTUK 6', 'KOLTUK 7', 'KOLTUK 8', 'KOLTUK 9', 'KOLTUK 10', 'KOLTUK 11', 'KOLTUK 12', 'KOLTUK 13', 'KOLTUK 14']

	#---BOS DOLU KOLTUK TARAMASI-------------
	baglan = sqlite3.connect("Kayit.db")
	imlec = baglan.cursor()
	koltukbul = 'select "Koltuk No" from Sinema where "Film Adi" = "{}" and "Salon No" = "{}"'
	liste = imlec.execute(koltukbul.format(filmadi, salonadi))
	baglan.commit()
	tablo = liste.fetchall()
	tamam = list(tablo)

	koltuklar = tkinter.Tk()
	koltuklar.title("Oturma Pozisyonu")
	koltuklar.geometry("500x500+400+100")

	perde = tkinter.Frame(koltuklar, width=480, height=100, bg="red").place(x=10,y=10)

	koltuk1 = tkinter.Button(koltuklar, command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 1"), text="1" ,width=5, height=3, bg="green")
	koltuk1.place(x=10,y=150)

	koltuk2 = tkinter.Button(koltuklar, command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 2"), text="2" ,width=5, height=3, bg="green")
	koltuk2.place(x=100,y=150)

	koltuk3 = tkinter.Button(koltuklar,command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 3"), text="3" ,width=5, height=3, bg="green")
	koltuk3.place(x=190,y=150)

	koltuk4 = tkinter.Button(koltuklar, command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 4"),text="4" ,width=5, height=3, bg="green")
	koltuk4.place(x=280,y=150)

	koltuk5 = tkinter.Button(koltuklar,command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 5"), text="5" ,width=5, height=3, bg="green")
	koltuk5.place(x=370,y=150)

	koltuk6 = tkinter.Button(koltuklar, command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 6"),text="6" ,width=5, height=3, bg="green")
	koltuk6.place(x=50,y= 230)

	koltuk7 = tkinter.Button(koltuklar,command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 7"), text="7" ,width=5, height=3, bg="green")
	koltuk7.place(x=140,y= 230)

	koltuk8 = tkinter.Button(koltuklar, command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 8"),text="8" ,width=5, height=3, bg="green")
	koltuk8.place(x=230,y= 230)

	koltuk9 = tkinter.Button(koltuklar, command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 9"),text="9" ,width=5, height=3, bg="green")
	koltuk9.place(x=320,y=230)

	koltuk10 = tkinter.Button(koltuklar,command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 10"), text="10" ,width=5, height=3, bg="green")
	koltuk10.place(x=10,y= 310)

	koltuk11 = tkinter.Button(koltuklar, command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 11"), text="11" ,width=5, height=3, bg="green")
	koltuk11.place(x=100,y=310)

	koltuk12= tkinter.Button(koltuklar, command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 12"), text="12" ,width=5, height=3, bg="green")
	koltuk12.place(x=190,y=310)

	koltuk13 = tkinter.Button(koltuklar, command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 13"), text="13" ,width=5, height=3, bg="green")
	koltuk13.place(x=280,y=310)

	koltuk14= tkinter.Button(koltuklar,command=lambda : koltukkayit(filmadi, salonadi, "Koltuk 14"), text="14" ,width=5, height=3, bg="green")
	koltuk14.place(x=370,y=310)

	def deneme () :
		try:
			for sayi in range(1,15) :
				numara = tamam[sayi]
				koltuk = numara[0]
				if koltuk == "KOLTUK 1" :
					koltuk1["bg"] = "red"
				elif koltuk == "KOLTUK 2" :
					koltuk2["bg"] = "red"
				elif koltuk == "KOLTUK 3" :
					koltuk3["bg"] = "red"
				elif koltuk == "KOLTUK 4" :
					koltuk4["bg"] = "red"
				elif koltuk == "KOLTUK 5" :
					koltuk5["bg"] = "red"
				elif koltuk == "KOLTUK 6" :
					koltuk6["bg"] = "red"
				elif koltuk == "KOLTUK 7" :
					koltuk7["bg"] = "red"
				elif koltuk == "KOLTUK 8" :
					koltuk8["bg"] = "red"
				elif koltuk == "KOLTUK 9" :
					koltuk9["bg"] = "red"
				elif koltuk == "KOLTUK 10" :
					koltuk10["bg"] = "red"
				elif koltuk == "KOLTUK 11" :
					koltuk11["bg"] = "red"
				elif koltuk == "KOLTUK 12" :
					koltuk12["bg"] = "red"
				elif koltuk == "KOLTUK 13" :
					koltuk13["bg"] = "red"
				elif koltuk == "KOLTUK 14" :
					koltuk14["bg"] = "red"
		except :
			pass
			
			



			
	A = threading.Thread(target=deneme)
	A.start()

	koltuklar.mainloop()



	
# jeszcze nie działa mi ten kod (przepisany z prezentacji Jukiego)
from tkinter import*
okno=Tk()
okno.geometry("400x400")
def usunPrzycisk():
    przyciskPoprzednie.destroy()


przyciskPoprzednie=Button(okno, text="Wciśnij mnie", command=usunPrzycisk).place(x=150,y=100)

okno.mainloop()

# OKNO W BLACKJACKU
from tkinter import messagebox
okno=Tk()
# w rozgrywce przycisk wykonaj RUCH (hit, stand, double down) clasy okna?? Zeby po naqciesnięciu przycisku "wykonaj wuch" otwierało się nowe okienko, żeby można było zaznaczyć opcję
wartosc=IntVar()
def akcja_przycisk_ruch():
    if wartosc.get()==1 or 2 or 3:
        messagebox.showinfo("Twój ruch", "Właśnie wykonałeś swój ruch.")
    else:
        messagebox.showinfo("Twój ruch", "Żeby wykonać ruch musisz zaznaczyć którąś opcję.")

# opcje ruchu w Radiobutton
przycisk_11=Radiobutton(okno,text="Hint", variable=wartosc, value=1).pack()
przycisk_12=Radiobutton(okno,text="stand", variable=wartosc, value=2).pack()
przycisk_13=Radiobutton(okno,text="Double down", variable=wartosc, value=3, ).pack()
przycisk_ruch=Button(okno, text="Wykonaj ruch", command=akcja_przycisk_ruch).pack()
okno.mainloop()

# usuwanie widgetów, inny przykład (z prezki)
from tkinter import*
from random import randint

root=Tk()
root.geometry("400x400")

def usunPrzycisk():
    przyciskPoprzednie.destroy()
    stworzprzycisk()

def stworzprzycisk():
    global przyciskPoprzednie
    przyciskPoprzednie = Button(root, text="Wciśnij mnie!", command=usunPrzycisk)
    losujX=randint(0,300)
    losujY=randint(0,300)
    przyciskPoprzednie.place(x=losujX, y=losujY)

stworzprzycisk()

root.mainloop()

# PASEK MENU
Okno=Tk()
pasekMenu=Menu(Okno)

pierwszeMenu=Menu(pasekMenu, tearoff=0)
pierwszeMenu.add_command(label="Wyjdż", command=Okno.quit)
pasekMenu.add_cascade(label="Pierwsze", menu=pierwszeMenu)

Okno.config(menu=pasekMenu)
Okno.mainloop()

#   P A S E K     M E N U
def akcjaZrob():
    messagebox.showinfo("Coś", "Wyświetlam okno")

def akcjaAutor():
    messagebox.showinfo("Autor", "Autorem jestem ja")

Okno=Tk()
pasekMenu=Menu(Okno)
pierwszeMenu=Menu(pasekMenu, tearoff=0)
pierwszeMenu.add_command(label="Zrób coś", command=akcjaZrob)
pierwszeMenu.add_command(label="Wyjdż", command=Okno.quit)
pasekMenu.add_cascade(label="Pierwsze", menu=pierwszeMenu)

pomocMenu= Menu(pasekMenu, tearoff=0)
pomocMenu.add_command(label="O autorze", command=akcjaAutor)
pasekMenu.add_cascade(label="Autor", menu=pomocMenu)

Okno.config(menu=pasekMenu)
Okno.mainloop()

# WCZYTANIE PLIKU GRAFICZNEGO
from tkinter import*
from PIL import Image, ImageTk

root=Tk()

plotno=Canvas(root, width=400, height=400)
plotno.pack()

obraz=Image.open("pyton.jpg") # ZADZIAŁAŁO W KOŃCU (odznaczyć ukryte foldery na dysku i znaleźć ścieżke jaką wywala python w kodzie błędu i do folderu docelowego dodać plik ze zdjęciem. w '' wystarczy podać nazwę pliku.)
obraz=obraz.rotate(45) # Ta komenda pozwala na obrót obrazka
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(200,200, image=obrazTk)

root.mainloop()

# ZAMIANA PALETY KOLORÓW RGB NA ODCIENIE SZAROŚCI
from tkinter import*
from PIL import Image, ImageTk

root=Tk()

plotno=Canvas(root, width=400, height=400)
plotno.pack()

obraz=Image.open("pyton.jpg").convert("L")
obraz=obraz.convert("L")
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(200,200, image=obrazTk)

root.mainloop()

# WYKORZYSTANIE FILTRÓW
from tkinter import*
from PIL import Image, ImageTk

root=Tk()

plotno=Canvas(root, width=400, height=400)
plotno.pack()

obraz=Image.open("pyton.jpg")
obraz=obraz.filter(ImageFilter.CONTOUR) #(nie chce zadziałać.....TT_TT prwdeopodbnie niekompatybilne do tej wersji tkintera (?)
obrazTk=ImageTk.PhotoImage(obraz)
plotno.create_image(200,200, image=obrazTk)

root.mainloop()

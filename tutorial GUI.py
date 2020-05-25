#polecenie python -m tkinter wpisane w wiersz poleceń pozwoli sprawdzić jaka wersja i czy wgl tkintera jets zainstalowana

from tkinter import * #import tkinter - też działa!!
#w tkinter posługujemy się klasami!
#The Tk class is instantiated without arguments. This creates a toplevel widget of Tk which usually is the main window of an application.

#from tkinter import frame, text, scrollbar, pack, grid, place
#The basic idea for tkinter.ttk is to separate, to the extent possible, the code implementing a widget’s behavior from the code implementing its appearance.
#from tkinter.ttk import*
#That code causes several tkinter.ttk widgets (Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale and Scrollbar) to automatically replace the Tk widgets.

from tkinter import messagebox #(UWAGA MessageBox nie działa! w tej wersji)
#działający przycisk - trzeba dodac funckę def; w funkcji przycisku podać argument command
def akcja_przycisk():
    #print("Cześć")
    #messagebox.showinfo("nazwa okienka", "tekst wyświetlany.")
    messagebox.showinfo("Okno powitalne","facetka")


    #1)trzeba coś stworzyć   #potem umieścic w oknie .pack()/.grid()/.place()
root = Tk() #to open the window (ważne! Tk zamiast tk)
root.title("BLACKJACK")
root.geometry("800x500")
root.configure(background="green") #kolor tła okna

#tutaj wrzucamy wszytsko co ma się znaleźć w oknie
#funkcja label() - tworzy etykiety
#Entry() - służy tworzeniu pola, do którego można wprowadzać dane
opis_pola_tekstowego=Label(root, text="Wprowadź tekst.").pack(side=LEFT)
pole_tekstowe=Entry(root, width="30").pack(side=RIGHT) # width - szerokość, można dodać długość x i y za pomocą padx=40, pady=20


# polecienie: grid(row=1, column=2, sticky=W/E,czli west/east-strona przylegania tekstu w przycisku). Komenda columnspan=2 - łączy ze sobą kolumny.
# polecienie: pack(side=LEFT/RIGHT/TOP/BOTTOM)

przycisk_1=Button(root, text="PRO", bg="black", fg="white", font="none 15 bold", command=akcja_przycisk).pack(side=TOP)
przycisk_2=Button(root, text="GRA", bg="red", fg="white", font="none 15 bold", command=akcja_przycisk).pack(side=LEFT)
przycisk_3=Button(root, text="MO", bg="blue", fg="white", font="none 15 bold", command=akcja_przycisk).pack(side=RIGHT)
przycisk_4=Button(root, text="WAN", bg="yellow", fg="black", font="none 15 bold", command=akcja_przycisk).pack(side=BOTTOM)
przycisk_5=Button(root, text="KO", bg="pink", fg="black", font="none 15 bold", command=akcja_przycisk).pack(side=BOTTOM)

#create label
#create a text entry box
#add a submit button
#create another label
#create a text box
#the dictionary

root.mainloop() #to run application

# 2 nowe Okno
# Radiobutton - zaznacza kółeczko (argument variable - zmienna, value - wartość)
root = Tk()
wartosc=IntVar() #zmienna
def akcja_przycisk():
    if wartosc.get()==1:
        messagebox.showinfo("Say hello", "Witaj")
    if wartosc.get()==2:
        messagebox.showinfo("Say hello", "Eluwina")

przycisk_1=Radiobutton(root,text="Wybor 1", variable=wartosc, value=1, command=akcja_przycisk).pack()
przycisk_2=Radiobutton(root,text="Wybor 2", variable=wartosc, value=2, command=akcja_przycisk).pack()
root=mainloop()

# niezależne przyciski Radiobutton (np. zaznaczasz kółeczkiem opcję i potem przycisk wybierz zaznaczone)
root = Tk()
zadanie1=IntVar() #zmienna
zadanie2=IntVar()

def akcja_przycisk():
    if zadanie1.get()==1:
        messagebox.showinfo("Say hello", "Witaj")
    if zadanie2.get()==2:
        messagebox.showinfo("Say hello", "Eluwina")

przycisk_1=Radiobutton(root,text="Wybor 1", variable=zadanie1, value=1).pack()
przycisk_2=Radiobutton(root,text="Wybor 2", variable=zadanie2, value=2).pack()
przycisk_1=Radiobutton(root,text="Wybor inny 1", variable=zadanie2, value=1).pack()
przycisk_2=Radiobutton(root,text="Wybor inny 2", variable=zadanie1, value=2).pack()
przycisk=Button(root, text="Powitanie",command=akcja_przycisk).pack()
root=mainloop()

# Układ place - przyciski na współrzędnych
root=Tk()
root.title("Moje okno")
root.geometry("300x300")
przyciskCZERWONY=Button(root, text="Czerwony",fg="red").place(x=70, y=50)
przyciskZIELONYY=Button(root, text="zielony",fg="red").place(x=170, y=50)
przyciskNIEBIESKIY=Button(root, text="niebieski",fg="red").place(x=70, y=150)
przyciskBIAŁY=Button(root, text="Biały",fg="red").place(x=170, y=150)
root.mainloop()

# polecenie destroy() do likwidacji niepotrzebnych widżetów

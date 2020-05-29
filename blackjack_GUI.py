from tkinter import *
from tkinter import messagebox

okno = Tk() #to open the window (ważne! Tk zamiast tk)
okno.title("BLACKJACK")
okno.geometry("800x500")
#okno.configure(background="green") #kolor tła okna

# ???jak wrzucić obrazek i wstawić go jako background okna???
#photo=PhotoImage(file="wstawić ścieżkę pliku?".gif)
#Label(root, image=photo, bg="pink").pack() - żeby umieścić obrazek w oknie trzeba dodać etykietę

# imie=Entry(okno, width=20).grid(row=1)
# imie.insert(0, "Wprowadź swoje imię: ") # w polu tekstowym się wyświetli polecenie
# imie.get()

def imie_uzytkownika():
    hello="Hello " + imie.get()
    opis_pola_tekstowego=Label(okno, text=hello, bg="green", fg="black", font="none 20 bold").grid(row=1)

przyciski_0=Button(okno, text="Witaj", command=imie_uzytkownika).grid(row=2)

def akcja_przycisk_1():
    #messagebox.showinfo("Okno powitalne","Zaczynamy! Będę Twoim krupierem :)")
    drugie_okno = Tk()
    drugie_okno.title("Rozgrywka")
    drugie_okno.geometry("800x500")
    opis_drugiego_pl =Label(drugie_okno, text = "Zagrajmy!", fg = "black")
    #po wybraniu opcji:zagraj otwiera się nowe okno, w którym będzie mogła się toczyć rozgrywka

przycisk_1=Button(okno, text="Zagraj", bg="red", fg="white", font="none 15 bold", command=akcja_przycisk_1).grid(row=3,column=1)

def akcja_przycisk_2():
    messagebox.showinfo("Zasady","Celem gry jest pokonać krupiera poprzez uzyskanie sumy jak najbliższej 21 punktów w kartach, jednak nie przekraczając 21. Gracz stawia zakład na specjalnym stole używając żetonów. Następnie gracz i krupier dostają po dwie karty. Obydwie karty gracza są odkryte, natomiast tylko jedna karta krupiera jest pokazana graczowi\nPUNKTACJA KART:\nKarty od dwójki do dziesiątki mają wartość równą numerowi karty.\nWalet, Dama i Król mają wartość równą 10 punktów.\nAs ma wartość równą 1 lub 11, w zależności co jest lepsze dla gracza.\nMOŻLIWOŚCI RUCHU\nW swojej turze możesz:\n1) Dobrać kartę (hit)\n2) Nie dobierać kart (stand)\n3) Podwoić stawkę (double down)\n4) Rozdwoić karty (split)")

przycisk_2=Button(okno, text="Zasady", bg="blue", fg="white", font="none 15 bold", command=akcja_przycisk_2).grid(row=3,column=2)

def akcja_przycisk_3():
    messagebox.showinfo("Okno pożegnalne","Może następnym razem. Do zobaczenia!")

przycisk_3=Button(okno, text="Wyjdź z programu", bg="yellow", fg="black", font="none 15 bold", command=akcja_przycisk_3).grid(row=3,column=3)

def akcja_przycisk_4():
    messagebox.showinfo("Autorki programu","Łzy, krew i pot wylały:\nAnna Cichocka\nAnna Kołodziejczyk\nKatarzyna Ziółkowska\nSylwia Leśniewska")

przycisk_4=Button(okno, text="Autorki", bg="orange", fg="black", font="none 15 bold", command=akcja_przycisk_4).grid(row=3,column=4)





okno.mainloop()

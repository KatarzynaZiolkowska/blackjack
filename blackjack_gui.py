
import os
import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image , ImageTk

okno = tk.Tk() #to open the window (ważne! Tk zamiast tk)
okno.title("BLACKJACK")
okno.geometry("800x500")
okno.config(bg='green')
gracz=[]
krupier=[]

los0 ="0"
los01 ="0"
los02 = "0"
los03 ="0"
los5 = "0"
los6 = "0"

player_total_points=0
croupier_total_points = 0
player_total_money=50


def akcja_karta():
    global img0
    global los0
    los0=los(deck)
    img0 = tk.PhotoImage(file = los0)
    img0 = img0.subsample(6)
    label = tk.Label(okno, image=img0)
    label.place(x=250,y=300)
    gracz.append(los0)
    przycisk1.config(state = tk.DISABLED)
    przycisk2.config(state = tk.DISABLED)
    global przycisk1_1
    global przycisk2_1
    points(p_litera(los0))
    przycisk1_1 = Button(okno, text = "Dobierz kartę", bg="black", fg="white", command = akcja_karta2)
    przycisk1_1.place(x=0,y=50)
    przycisk2_1 = Button(okno, text = "Nie dobieraj", bg="black", fg="white", command= akcja_karta_k1)
    przycisk2_1.place(x=0,y=80)

def akcja_karta2():
    global img01
    global los01
    los01=los(deck)
    img01 = tk.PhotoImage(file = los01)
    img01 = img01.subsample(6)
    label = tk.Label(okno, image=img01)
    label.place(x=325,y=300)
    gracz.append(los01)
    przycisk1_1.config(state = tk.DISABLED)
    przycisk2_1.config(state = tk.DISABLED)
    global przycisk1_2
    global przycisk2_2
    points(p_litera(los01))
    przycisk1_2 = Button(okno, text = "Dobierz kartę", bg="black", fg="white", command = akcja_karta3)
    przycisk1_2.place(x=0,y=50)
    przycisk2_2 = Button(okno, text = "Nie dobieraj", bg="black", fg="white", command= akcja_karta_k1)
    przycisk2_2.place(x=0,y=80)



def akcja_karta3():
    global img02
    global los02
    los02=los(deck)
    img02 = tk.PhotoImage(file = los02)
    img02 = img02.subsample(6)
    label = tk.Label(okno, image=img01)
    label.place(x=400,y=300)
    gracz.append(los02)
    przycisk1_2.config(state = tk.DISABLED)
    przycisk2_2.config(state = tk.DISABLED)
    global przycisk1_3
    global przycisk2_3
    points(p_litera(los02))
    przycisk1_3 = Button(okno, text = "Dobierz kartę", bg="black", fg="white", command = akcja_karta4)
    przycisk1_3.place(x=0,y=50)
    przycisk2_3 = Button(okno, text = "Nie dobieraj", bg="black", fg="white", command= akcja_karta_k1)
    przycisk2_3.place(x=0,y=80)


def akcja_karta4():
    global img03
    global los03
    los03=los(deck)
    img03 = tk.PhotoImage(file = los03)
    img03 = img03.subsample(6)
    label = tk.Label(okno, image=img03)
    label.place(x=475,y=300)
    gracz.append(los03)
    przycisk1_3.config(state = tk.DISABLED)
    przycisk2_3.config(state = tk.DISABLED)
    points(p_litera(los03))
    akcja_karta_k1()


def akcja_karta_k1():
    global img4
    global los4
    los4=los(deck)
    img4 = tk.PhotoImage(file = los4)
    img4 = img4.subsample(6)
    label = tk.Label(okno, image=img4)
    label.place(x=450,y=60)
    krupier.append(los4)
    points2(p_litera(los4))
    if croupier_total_points < 17:
        akcja_karta_k2()
    elif croupier_total_points >= 17:
        liczenie_punktow()

def akcja_karta_k2():
    global img5
    global los5
    los5=los(deck)
    img5 = tk.PhotoImage(file = los5)
    img5 = img5.subsample(6)
    label = tk.Label(okno, image=img5)
    label.place(x=525,y=60)
    krupier.append(los5)
    points2(p_litera(los5))
    if croupier_total_points < 17:
        akcja_karta_k3()
    elif croupier_total_points >= 17:
        liczenie_punktow()

def akcja_karta_k3():
    global img6
    global los6
    los6=los(deck)
    img6 = tk.PhotoImage(file = los6)
    img6 = img6.subsample(6)
    label = tk.Label(okno, image=img6)
    label.place(x=600,y=60)
    krupier.append(los6)
    points2(p_litera(los6))
    liczenie_punktow()

def liczenie_punktow():
    print(player_total_points, croupier_total_points)
    if player_total_points >21 or croupier_total_points > player_total_points and croupier_total_points <21:
        wynik = Label(okno, text = "Przegrałeś.", bg="blue", fg="black", font="none 15 bold")
        wynik.place(x =550, y = 300)
    elif player_total_points == 21 and croupier_total_points !=21:
         wynik = Label(okno, text = "Masz blakcjacka! Gratulacje!", bg="blue", fg="black", font="none 15 bold")
         wynik.place(x =550, y = 300)
    elif croupier_total_points >21 or player_total_points > croupier_total_points and player_total_points <21:
         wynik = Label(okno, text = "Wygrałeś! Gratulacje!", bg="blue", fg="black", font="none 15 bold")
         wynik.place(x =550, y = 300)

def akcja_przycisk_1():

    global img
    global los1
    los1=los(deck)
    img = tk.PhotoImage(file = los1)
    img = img.subsample(6)
    label = tk.Label(okno, image=img)
    label.place(x=100,y=300)
    gracz.append(los1)
    global img2
    global los2
    los2=los(deck)
    img2 = tk.PhotoImage(file = los2)
    img2 = img2.subsample(6)
    label = tk.Label(okno, image=img2)
    label.place(x=175,y=300)
    gracz.append(los2)
    global img3
    global los3
    los3=los(deck)
    img3 = tk.PhotoImage(file = los3)
    img3 = img3.subsample(6)
    label = tk.Label(okno, image=img3)
    label.place(x=375,y=60)
    krupier.append(los3)
    global img5
    img5 = tk.PhotoImage(file = "purple_back.png")
    img5 = img5.subsample(6)
    label = tk.Label(okno, image=img5)
    label.place(x=450,y=60)
    przycisk_1.config(state = tk.DISABLED)
    global przycisk1
    global przycisk2
    przycisk1 = Button(okno, text = "Dobierz kartę", bg="black", fg="white", command = akcja_karta)
    przycisk1.place(x=0,y=50)
    przycisk2 = Button(okno, text = "Nie dobieraj", bg="black", fg="white", command= akcja_karta_k1)
    przycisk2.place(x=0,y=80)
    points(p_litera(los1))
    points(p_litera(los2))
    points2(p_litera(los3))


def akcja_przycisk_2():
    messagebox.showinfo("Zasady","Celem gry jest pokonać krupiera poprzez uzyskanie sumy jak najbliższej 21 punktów w kartach, jednak nie przekraczając 21. Gracz stawia zakład na specjalnym stole używając żetonów. Następnie gracz i krupier dostają po dwie karty. Obydwie karty gracza są odkryte, natomiast tylko jedna karta krupiera jest pokazana graczowi\nPUNKTACJA KART:\nKarty od dwójki do dziesiątki mają wartość równą numerowi karty.\nWalet, Dama i Król mają wartość równą 10 punktów.\nAs ma wartość równą 1 lub 11, w zależności co jest lepsze dla gracza.\nMOŻLIWOŚCI RUCHU\nW swojej turze możesz:\n1) Dobrać kartę (hit)\n2) Nie dobierać kart (stand)\n3) Podwoić stawkę (double down)\n4) Rozdwoić karty (split)")

def akcja_przycisk_4():
    messagebox.showinfo("Autorki programu","Łzy, krew i pot wylały:\nAnna Cichocka\nAnna Kołodziejczyk\nKatarzyna Ziółkowska\nSylwia Leśniewska")


#tworzymy listę wszystkich plików w folderze
deck = os.listdir()
deck.remove("blackjack_gui.py")
# deck.remove("gujuuju.py")
deck.remove("purple_back.png")
# deck.remove("gjuu.py")
def los(deck):
    wylosowana=random.choice(deck)
    return wylosowana

#używamy pierwszej litery pliku do rozpoznania karty (dlatego też dobrze by było, żeby w folderze znajdowały)
def p_litera(wylosowana):
    symbol_wylosowana=wylosowana[0]
    return symbol_wylosowana

przycisk_1=Button(okno, text="Zagraj", bg="red", fg="white", font="none 15 bold", command=akcja_przycisk_1,)
przycisk_1.place(x=0,y=0)

przycisk_2=Button(okno, text="Zasady", bg="blue", fg="white", font="none 15 bold", command=akcja_przycisk_2)
przycisk_2.place(x=75,y=0)

przycisk_3=Button(okno, text="Wyjdź z programu", bg="yellow", fg="black", font="none 15 bold", command=okno.quit)
przycisk_3.place(x=160,y=0)

przycisk_4=Button(okno, text="Autorki", bg="orange", fg="black", font="none 15 bold", command=akcja_przycisk_4)
przycisk_4.place(x=348,y=0)



def points(karta):
    global player_total_points
    if karta=="2":
        player_total_points += 2
    elif karta=="3":
        player_total_points += 3
    elif karta=="4":
        player_total_points += 4
    elif karta=="5":
        player_total_points += 5
    elif karta=="6":
        player_total_points += 6
    elif karta=="7":
        player_total_points += 7
    elif karta=="8":
        player_total_points += 8
    elif karta=="9":
        player_total_points +=9
    elif karta=="A":
        player_total_points += 11
        if player_total_points > 21:
            player_total_points = player_total_points -10
        else:
            player_total_points = player_total_points
    elif karta=="J" or karta=="K" or karta=="Q" or karta=="1":
        player_total_points +=10

    return player_total_points


def points2(karta):
    global croupier_total_points
    if karta=="2":
        croupier_total_points += 2
    elif karta=="3":
        croupier_total_points += 3
    elif karta=="4":
        croupier_total_points += 4
    elif karta=="5":
        croupier_total_points += 5
    elif karta=="6":
        croupier_total_points += 6
    elif karta=="7":
        croupier_total_points += 7
    elif karta=="8":
        croupier_total_points += 8
    elif karta=="9":
        croupier_total_points +=9
    elif karta=="A":
        croupier_total_points += 11
        if croupier_total_points > 21:
            croupier_total_points = croupier_total_points -10
        else:
            croupier_total_points = croupier_total_points
    elif karta=="J" or karta=="K" or karta=="Q" or karta=="1":
        croupier_total_points +=10

    return croupier_total_points


okno.mainloop()


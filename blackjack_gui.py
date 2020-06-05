import os
import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image , ImageTk

window = tk.Tk() #to open the window (ważne! Tk zamiast tk)
window.title("BLACKJACK")
window.geometry("800x500")
window.config(bg='green')

player=[] #stowrzenie pustych list, do których program będzie dodawał kolejne karty
croupier=[]

players_card4 ="0"  #przypisanie początkowych nazw dobieranym kartom, tak by można było doliczyć "zerową ilość punktów" na wypadek niedobrania danej karty.
players_card5 ="0"
players_card6 ="0"
croupier_card3 = "0"
croupier_card4 = "0"

player_total_points=0
croupier_total_points = 0
player_total_money=50


def deal_of_cards():    #Ta funkcja zadziała po naciśnięciu przycisku:Zagraj i rozda po dwie karty graczowi i krupierowi(jedna karta krupiera będzie zakryta).
    player_field = Label(window, text ="Karty gracza:", bg="white", fg="green", font="none 10 bold")
    player_field.place(x= 20, y = 270)
    croupier_field = Label(window, text ="Karty krupiera:", bg="white", fg="green", font="none 10 bold")
    croupier_field.place(x= 250, y = 50)
    
    global image1
    global players_card1
    players_card1=los(deck)
    image1 = tk.PhotoImage(file = players_card1)
    image1 = image1.subsample(6)
    label = tk.Label(window, image=image1)
    label.place(x=100,y=300)
    player.append(players_card1)

    global image2
    global players_card2
    players_card2=los(deck)
    image2 = tk.PhotoImage(file = players_card2)
    image2 = image2.subsample(6)
    label = tk.Label(window, image=image2)
    label.place(x=175,y=300)
    player.append(players_card2)

    global image3
    global croupier_card1
    croupier_card1=los(deck)
    image3 = tk.PhotoImage(file = croupier_card1)
    image3 = image3.subsample(6)
    label = tk.Label(window, image=image3)
    label.place(x=375,y=60)
    croupier.append(croupier_card1)

    global image4
    image4 = tk.PhotoImage(file = "purple_back.png")
    image4 = image4.subsample(6)
    label = tk.Label(window, image=image4)
    label.place(x=450,y=60)
    play_button.config(state = tk.DISABLED)

    points(first_letter(players_card1))
    points(first_letter(players_card2))
    points2(first_letter(croupier_card1))
    printing_points()

    global button1 #Tu powstają przyciski które pozwalają graczowi na podjęcie decyzji czy dobiera kartę, czy też nie dobiera
    global button2
    if player_total_points <21:
        button1 = Button(window, text = "Dobierz kartę", bg="black", fg="white", command = picking_card_player1)
        button1.place(x=0,y=50)
        button2 = Button(window, text = "Nie dobieraj", bg="black", fg="white", command= picking_card_croupier1)
        button2.place(x=0,y=80)
    elif player_total_points ==21:
        result = Label(window, text = "Masz blakcjacka! Gratulacje!", bg="white", fg="black", font="none 15 bold")
        result.place(x =550, y = 350)
        restart.config(state = tk.NORMAL)


 #Teraz rozpisane zostaną funkcje pozwalające graczowi na dobieranie kolejnych kart i doliczanie ich wartości do łącznej liczby punktów gracza
def picking_card_player1(): # To jest funkcja, która dobiera pierwszą kartę dla gracza
    global image7
    global players_card3
    players_card3=los(deck)
    image7 = tk.PhotoImage(file = players_card3)
    image7 = image7.subsample(6)
    label = tk.Label(window, image=image7)
    label.place(x=250,y=300)
    player.append(players_card3)
    button1.config(state = tk.DISABLED)
    button2.config(state = tk.DISABLED)
    global button1_1
    global button2_1
    points(first_letter(players_card3))
    printing_points()
    if player_total_points <21:
        button1_1 = Button(window, text = "Dobierz kartę", bg="black", fg="white", command = picking_card_player2)
        button1_1.place(x=0,y=50)
        button2_1 = Button(window, text = "Nie dobieraj", bg="black", fg="white", command= picking_card_croupier1)
        button2_1.place(x=0,y=80)
    elif player_total_points ==21:
        picking_card_croupier1()
    elif player_total_points >21:
        result = Label(window, text = "Przegrałeś.", bg="white", fg="black", font="none 15 bold")
        result.place(x =550, y = 350)
        restart.config(state = tk.NORMAL)

def picking_card_player2():  # To jest funkcja, która dobiera drugą kartę dla gracza
    global image8
    global players_card4
    players_card4=los(deck)
    image8= tk.PhotoImage(file = players_card4)
    image8 = image8.subsample(6)
    label = tk.Label(window, image=image8)
    label.place(x=325,y=300)
    player.append(players_card4)
    button1_1.config(state = tk.DISABLED)
    button2_1.config(state = tk.DISABLED)
    global button1_2
    global button2_2
    points(first_letter(players_card4))
    printing_points()
    if player_total_points <21:
        button1_2 = Button(window, text = "Dobierz kartę", bg="black", fg="white", command = picking_card_player3)
        button1_2.place(x=0,y=50)
        button2_2 = Button(window, text = "Nie dobieraj", bg="black", fg="white", command= picking_card_croupier1)
        button2_2.place(x=0,y=80)
    elif player_total_points ==21:
        picking_card_croupier1()
    elif player_total_points >21:
        result = Label(window, text = "Przegrałeś.", bg="white", fg="black", font="none 15 bold")
        result.place(x =550, y = 350)
        restart.config(state = tk.NORMAL)


def picking_card_player3():   # To jest funkcja, która dobiera trzecią kartę dla gracza
    global image9
    global players_card5
    players_card5=los(deck)
    image9 = tk.PhotoImage(file = players_card5)
    image9 = image9.subsample(6)
    label = tk.Label(window, image=image9)
    label.place(x=400,y=300)
    player.append(players_card5)
    button1_2.config(state = tk.DISABLED)
    button2_2.config(state = tk.DISABLED)
    global button1_3
    global button2_3
    points(first_letter(players_card5))
    printing_points()
    if player_total_points <21:
        button1_3 = Button(window, text = "Dobierz kartę", bg="black", fg="white", command = picking_card_player4)
        button1_3.place(x=0,y=50)
        button2_3 = Button(window, text = "Nie dobieraj", bg="black", fg="white", command= picking_card_croupier1)
        button2_3.place(x=0,y=80)
    elif player_total_points ==21:
        picking_card_croupier1()
    elif player_total_points >21:
        result = Label(window, text = "Przegrałeś.", bg="white", fg="black", font="none 15 bold")
        result.place(x =550, y = 350)
        restart.config(state = tk.NORMAL)


def picking_card_player4():  # To jest funkcja, która dobiera czwartą kartę dla gracza
    global image10
    global players_card6
    players_card6=los(deck)
    image10 = tk.PhotoImage(file = players_card6)
    image10 = image10.subsample(6)
    label = tk.Label(window, image=image10)
    label.place(x=475,y=300)
    player.append(players_card6)
    button1_3.config(state = tk.DISABLED)
    button2_3.config(state = tk.DISABLED)
    points(first_letter(players_card6))
    printing_points()
    if player_total_points <= 21:
        picking_card_croupier1()
    elif player_total_points >21:
        result = Label(window, text = "Przegrałeś.", bg="white", fg="black", font="none 15 bold")
        result.place(x =550, y = 350)
        restart.config(state = tk.NORMAL)





 #Teraz rozpisane zostaną funkcje, które będą dobierać karty dla krupiera, jeśli suma jego punktów jest <17. W przeciwnym razie program przejdzie do liczenia punktów.

def picking_card_croupier1():  #To jest funkcja, która odkrywa zakrytą kartę krupiera.
    global image5
    global croupier_card2
    croupier_card2=los(deck)
    image5 = tk.PhotoImage(file = croupier_card2)
    image5 = image5.subsample(6)
    label = tk.Label(window, image=image5)
    label.place(x=450,y=60)
    croupier.append(croupier_card2)
    points2(first_letter(croupier_card2))
    printing_points()
    if croupier_total_points < 17:
        picking_card_croupier2()
    elif croupier_total_points ==21:
        result = Label(window, text = "Krupier ma blackjacka. Przegrałeś.", bg="white", fg="black", font="none 15 bold")
        result.place(x =550, y = 350)
        restart.config(state = tk.NORMAL)
    elif croupier_total_points >= 17 and croupier_total_points!=21:
        points_counting()


def picking_card_croupier2(): # To jest funnkcja, która dobiera pierwszą kartę krupiera.
    global image4
    global croupier_card3
    croupier_card3=los(deck)
    image4 = tk.PhotoImage(file = croupier_card3)
    image4 = image4.subsample(6)
    label = tk.Label(window, image=image4)
    label.place(x=525,y=60)
    croupier.append(croupier_card3)
    points2(first_letter(croupier_card3))
    printing_points()
    if croupier_total_points < 17:
        picking_card_croupier3()
    elif croupier_total_points >= 17:
        points_counting()

def picking_card_croupier3():  #To jest funkcja, która dobiera drugą kartę, krupiera.
    global image6
    global croupier_card4
    croupier_card4=los(deck)
    image6 = tk.PhotoImage(file = croupier_card4)
    image6 = image6.subsample(6)
    label = tk.Label(window, image=image6)
    label.place(x=600,y=60)
    croupier.append(croupier_card4)
    points2(first_letter(croupier_card4))
    printing_points()
    points_counting()


def printing_points():  #Ta funkcja służy do wyświetlania punktów gracza i krupiera
    player_points = "Masz: " + str(player_total_points) + " punktów."
    croupier_points = "Krupier ma: " + str(croupier_total_points) + " punktów"
    frame = Label(window, text =player_points, bg="white", fg="black", font="none 15 bold")
    frame.place(x =550, y = 250)
    frame = Label(window, text = croupier_points, bg="white", fg="black", font="none 15 bold")
    frame.place(x =550, y = 300)


def points_counting(): #Ta funkcja pozwala na podsumowanie otrzymanych punktów i wyświetlenie wyniku
    if player_total_points >21 or croupier_total_points > player_total_points and croupier_total_points <21:
        result = Label(window, text = "Przegrałeś.", bg="white", fg="black", font="none 15 bold")
        result.place(x =550, y = 350)
    elif player_total_points == 21 and croupier_total_points !=21:
        result = Label(window, text = "Wygrałeś! Gratulacje!", bg="white", fg="black", font="none 15 bold")
        result.place(x =550, y = 350)
    elif croupier_total_points == 21 and player_total_points != 21:
        result = Label(window, text = "Przegrałeś.", bg="white", fg="black", font="none 15 bold")
        result.place(x =550, y = 350)
    elif player_total_points ==21 and croupier_total_points ==21:
        result = Label(window, text = "Jest remis. Nie tracisz i nie zyskujesz.", bg="white", fg="black", font="none 15 bold")
        result.place(x =550, y = 350)
    elif croupier_total_points >21 or player_total_points > croupier_total_points and player_total_points <21:
        result = Label(window, text = "Wygrałeś! Gratulacje!", bg="white", fg="black", font="none 15 bold")
        result.place(x =550, y = 350)
    elif player_total_points == croupier_total_points:
        result = Label(window, text = "Jest remis. Nie tracisz i nie zyskujesz.", bg="white", fg="black", font="none 15 bold")
        result.place(x =550, y = 350)
    restart.config(state = tk.NORMAL)

#teraz funkcje pieniężne
def stawka_disable():
    five.config(state = tk.DISABLED)
    ten.config(state = tk.DISABLED)
    twenty.config(state = tk.DISABLED)
    thirty.config(state = tk.DISABLED)
    forty.config(state = tk.DISABLED)
    fifty.config(state = tk.DISABLED)
    ok.config(state = tk.NORMAL)
    deal_of_cards()

def stawka5():
    global player_total_money
    player_total_money-=5
    stawka_disable()

def stawka10():
    global player_total_money
    player_total_money-=10
    stawka_disable()

def stawka20():
    global player_total_money
    player_total_money-=20
    stawka_disable()

def stawka30():
    global player_total_money
    player_total_money-=30
    stawka_disable()

def stawka40():
    global player_total_money
    player_total_money-=40
    stawka_disable()

def stawka50():
    global player_total_money
    player_total_money-=50
    stawka_disable()

def messageWindow():
    win = Toplevel()
    win.title('Stawka')
    win.geometry("400x180")
    global five
    global ten
    global twenty
    global thirty
    global forty
    global fifty
    global ok
    message = 'Aktualnie masz '+str(player_total_money)+' złotych, ile chesz postawić?'
    b=Label(win, text=message,font="none 13 bold")
    b.place(x=10,y=10)
    five=Button(win, text='5', bg="black", fg="white", font="none 15 bold", command=stawka5)
    five.place(x=25,y=90)
    ten=Button(win, text='10', bg="black", fg="white", font="none 15 bold",command=stawka10)
    ten.place(x=75,y=90)
    twenty=Button(win, text='20', bg="black", fg="white", font="none 15 bold", command=stawka20)
    twenty.place(x=140,y=90)
    thirty=Button(win, text='30', bg="black", fg="white", font="none 15 bold", command=stawka30)
    thirty.place(x=205,y=90)
    forty=Button(win, text='40', bg="black", fg="white", font="none 15 bold", command=stawka40)
    forty.place(x=270,y=90)
    fifty=Button(win, text='50', bg="black", fg="white", font="none 15 bold", command=stawka50)
    fifty.place(x=330,y=90)
    ok=Button(win, text='OK', state=DISABLED, command=win.destroy)
    ok.place(x=180,y=150)


#tworzymy listę wszystkich plików w folderze
deck = os.listdir()
deck.remove("blackjack.py")
deck.remove("gujuuju.py")
deck.remove("purple_back.png")
deck.remove("gjuu.py")
deck.remove("dużyprojektgui.py")
def los(deck):
    random_card=random.choice(deck)
    return random_card
#używamy pierwszej litery pliku do rozpoznania karty (dlatego też dobrze by było, żeby w folderze znajdowały)
def first_letter(random_card):
    random_card_symbol=random_card[0]
    return random_card_symbol

#Funkcje przypisujące wartości poszczególnym kartom.
def points(card):
    global player_total_points
    if card=="2":
        player_total_points += 2
    elif card=="3":
        player_total_points += 3
    elif card=="4":
        player_total_points += 4
    elif card=="5":
        player_total_points += 5
    elif card=="6":
        player_total_points += 6
    elif card=="7":
        player_total_points += 7
    elif card=="8":
        player_total_points += 8
    elif card=="9":
        player_total_points +=9
    elif card=="A":
        player_total_points += 11
        if player_total_points > 21:
            player_total_points = player_total_points -10
        else:
            player_total_points = player_total_points
    elif card=="J" or card=="K" or card=="Q" or card=="1":
        player_total_points +=10

    return player_total_points


def points2(card):
    global croupier_total_points
    if card=="2":
        croupier_total_points += 2
    elif card=="3":
        croupier_total_points += 3
    elif card=="4":
        croupier_total_points += 4
    elif card=="5":
        croupier_total_points += 5
    elif card=="6":
        croupier_total_points += 6
    elif card=="7":
        croupier_total_points += 7
    elif card=="8":
        croupier_total_points += 8
    elif card=="9":
        croupier_total_points +=9
    elif card=="A":
        croupier_total_points += 11
        if croupier_total_points > 21:
            croupier_total_points = croupier_total_points -10
        else:
            croupier_total_points = croupier_total_points
    elif card=="J" or card=="K" or card=="Q" or card=="1":
        croupier_total_points +=10

    return croupier_total_points

#Funkcje dla przycisków z informacjami
def rules_info():
    messagebox.showinfo("Zasady","Celem gry jest pokonać krupiera poprzez uzyskanie sumy jak najbliższej 21 punktów, jednak nie przekraczając 21. Gracz stawia zakład na specjalnym stole używając żetonów. Następnie gracz i krupier dostają po dwie karty. Obydwie karty gracza są odkryte, natomiast tylko jedna card krupiera jest pokazana graczowi\nPUNKTACJA KART:\nKarty od dwójki do dziesiątki mają wartość równą numerowi karty.\nWalet, Dama i Król mają wartość równą 10 punktów.\nAs ma wartość równą 1 lub 11, w zależności co jest lepsze dla gracza.\nMOŻLIWOŚCI RUCHU\nW swojej turze możesz:\n1) Dobrać kartę (hit)\n2) Nie dobierać kart (stand)\n3) Podwoić stawkę (double down)\n4) Rozdwoić karty (split)")

def authors_info():
    messagebox.showinfo("Autorki programu","Łzy, krew i pot wylały:\nAnna Cichocka\nAnna Kołodziejczyk\nKatarzyna Ziółkowska\nSylwia Leśniewska")

#restart programu
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


# Uruchamianie przycisków
play_button=Button(window, text="Zagraj", bg="red", fg="white", font="none 15 bold", command= messageWindow)
play_button.place(x=0,y=0)

rules_button=Button(window, text="Zasady", bg="blue", fg="white", font="none 15 bold", command= rules_info)
rules_button.place(x=75,y=0)

quit_button=Button(window, text="Wyjdź z programu", bg="yellow", fg="black", font="none 15 bold", command=window.quit)
quit_button.place(x=160,y=0)

authors_button=Button(window, text="Autorki", bg="orange", fg="black", font="none 15 bold", command=authors_info)
authors_button.place(x=348,y=0)

restart=Button(window, text="Zagraj Ponownie", bg="grey", fg="black", font="none 15 bold",state=tk.DISABLED, command=restart_program)
restart.place(x=450,y=0)


window.mainloop()


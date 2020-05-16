
import random

 #creating a game deck

deck = []
for i in ["KIER", "PIK", "KARO", "TREFL"]:
    two = [ "2 " +i]
    deck.append(two)
    three = [ "3 " +i]
    deck.append(three)
    four = [ "4 " +i]
    deck.append(four)
    five = [ "5 " +i]
    deck.append(five)
    six = [ "6 " +i]
    deck.append(six)
    seven = ["7 " +i]
    deck.append(seven)
    eight = ["8 " +i]
    deck.append(eight)
    nine =["9 " +i]
    deck.append(nine)
    ten = ["10 " +i]
    deck.append(ten)
    jack = ["Walet " +i]
    deck.append(jack)
    queen = ["Dama " +i]
    deck.append(queen)
    king = ["Król " +i]
    deck.append(king)
    ace = ["As "+i]
    deck.append(ace)

#
# print(deck)
#
# #
print("Witaj w grze BLACKJACK!")
rate = int(input("Jaką stawkę chcesz postawić (podaj wartość w złotówkach)? "))

#card draw, first round
player_total_points = 0
croupier_total_points = 0

#player's first card draw

player_first_card = random.choice(deck)
print("Twoja pierwsza karta to:", player_first_card)

if player_first_card == ['2 KIER'] or player_first_card == ['2 PIK'] or player_first_card == ['2 KARO'] or player_first_card == ['2 TREFL']:
    player_total_points += 2
elif player_first_card == ['3 KIER'] or player_first_card == ['3 PIK'] or player_first_card == ['3 KARO'] or player_first_card == ['3 TREFL']:
    player_total_points += 3
elif player_first_card == ['4 KIER'] or player_first_card == ['4 PIK'] or player_first_card == ['4 KARO'] or player_first_card == ['4 TREFL']:
    player_total_points += 4
elif player_first_card == ['5 KIER'] or player_first_card == ['5 PIK'] or player_first_card == ['5 KARO'] or player_first_card == ['5 TREFL']:
    player_total_points += 5
elif player_first_card == ['6 KIER'] or player_first_card == ['6 PIK'] or player_first_card == ['6 KARO'] or player_first_card == ['6 TREFL']:
    player_total_points += 6
elif player_first_card == ['7 KIER'] or player_first_card == ['7 PIK'] or player_first_card == ['7 KARO'] or player_first_card == ['7 TREFL']:
    player_total_points += 7
elif player_first_card == ['8 KIER'] or player_first_card == ['8 PIK'] or player_first_card == ['8 KARO'] or player_first_card == ['8 TREFL']:
    player_total_points += 8
elif player_first_card == ['9 KIER'] or player_first_card == ['9 PIK'] or player_first_card == ['9 KARO'] or player_first_card == ['9 TREFL']:
    player_total_points +=9
elif player_first_card == ['As KIER'] or player_first_card == ['As PIK'] or player_first_card == ['As KARO'] or player_first_card == ['As TREFL']:
    player_total_points += 11
else:
    player_total_points +=10





#croupier's first card draw


croupier_first_card = random.choice(deck)
print("Pierwsza karta krupiera to:", croupier_first_card)

if croupier_first_card == ['2 KIER'] or croupier_first_card == ['2 PIK'] or croupier_first_card == ['2 KARO'] or croupier_first_card == ['2 TREFL']:
     croupier_total_points += 2
elif croupier_first_card == ['3 KIER'] or croupier_first_card == ['3 PIK'] or croupier_first_card == ['3 KARO'] or croupier_first_card == ['3 TREFL']:
    croupier_total_points += 3
elif croupier_first_card == ['4 KIER'] or croupier_first_card == ['4 PIK'] or croupier_first_card == ['4 KARO'] or croupier_first_card == ['4 TREFL']:
    croupier_total_points += 4
elif croupier_first_card == ['5 KIER'] or croupier_first_card == ['5 PIK'] or croupier_first_card == ['5 KARO'] or croupier_first_card == ['5 TREFL']:
    croupier_total_points += 5
elif croupier_first_card == ['6 KIER'] or croupier_first_card == ['6 PIK'] or croupier_first_card == ['6 KARO'] or croupier_first_card == ['6 TREFL']:
    croupier_total_points += 6
elif croupier_first_card == ['7 KIER'] or croupier_first_card == ['7 PIK'] or croupier_first_card == ['7 KARO'] or croupier_first_card == ['7 TREFL']:
    croupier_total_points += 7
elif croupier_first_card == ['8 KIER'] or croupier_first_card == ['8 PIK'] or croupier_first_card == ['8 KARO'] or croupier_first_card == ['8 TREFL']:
    croupier_total_points += 8
elif croupier_first_card == ['9 KIER'] or croupier_first_card == ['9 PIK'] or croupier_first_card == ['9 KARO'] or croupier_first_card == ['9 TREFL']:
    croupier_total_points +=9
elif croupier_first_card == ['As KIER'] or croupier_first_card == ['As PIK'] or croupier_first_card == ['As KARO'] or croupier_first_card == ['As TREFL']:
    croupier_total_points +=11
else:
    croupier_total_points +=10

# print("Suma towich punktó to:", player_total_points)
# print("suma punktów krupiera to:", croupier_total_points)

#card draw, second round

#player's second card draw

player_second_card = random.choice(deck)
print("Twoja druga karta to:", player_second_card)

if player_second_card == ['2 KIER'] or player_second_card == ['2 PIK'] or player_second_card == ['2 KARO'] or player_second_card == ['2 TREFL']:
    player_total_points += 2
elif player_second_card == ['3 KIER'] or player_second_card == ['3 PIK'] or player_second_card == ['3 KARO'] or player_second_card == ['3 TREFL']:
    player_total_points += 3
elif player_second_card == ['4 KIER'] or player_second_card == ['4 PIK'] or player_second_card == ['4 KARO'] or player_second_card == ['4 TREFL']:
    player_total_points += 4
elif player_second_card == ['5 KIER'] or player_second_card == ['5 PIK'] or player_second_card == ['5 KARO'] or player_second_card == ['5 TREFL']:
    player_total_points += 5
elif player_second_card == ['6 KIER'] or player_second_card == ['6 PIK'] or player_second_card == ['6 KARO'] or player_second_card == ['6 TREFL']:
    player_total_points += 6
elif player_second_card == ['7 KIER'] or player_second_card == ['7 PIK'] or player_second_card == ['7 KARO'] or player_second_card == ['7 TREFL']:
    player_total_points += 7
elif player_second_card == ['8 KIER'] or player_second_card == ['8 PIK'] or player_second_card == ['8 KARO'] or player_second_card == ['8 TREFL']:
    player_total_points += 8
elif player_second_card == ['9 KIER'] or player_second_card == ['9 PIK'] or player_second_card == ['9 KARO'] or player_second_card == ['9 TREFL']:
    player_total_points +=9
elif player_second_card == ['As KIER'] or player_second_card == ['As PIK'] or player_second_card == ['As KARO'] or player_second_card == ['As TREFL']:
    player_total_points += 11
else:
    player_total_points +=10
#


#croupier's second card draw

croupier_second_card = random.choice(deck)
print("Druga karta krupiera jest zakryta")


if croupier_second_card == ['2 KIER'] or croupier_second_card == ['2 PIK'] or croupier_second_card == ['2 KARO'] or croupier_second_card == ['2 TREFL']:
     croupier_total_points += 2
elif croupier_second_card == ['3 KIER'] or croupier_second_card == ['3 PIK'] or croupier_second_card == ['3 KARO'] or croupier_second_card == ['3 TREFL']:
    croupier_total_points += 3
elif croupier_second_card == ['4 KIER'] or croupier_second_card == ['4 PIK'] or croupier_second_card == ['4 KARO'] or croupier_second_card == ['4 TREFL']:
    croupier_total_points += 4
elif croupier_second_card == ['5 KIER'] or croupier_second_card == ['5 PIK'] or croupier_second_card == ['5 KARO'] or croupier_second_card == ['5 TREFL']:
    croupier_total_points += 5
elif croupier_second_card == ['6 KIER'] or croupier_second_card == ['6 PIK'] or croupier_second_card == ['6 KARO'] or croupier_second_card == ['6 TREFL']:
    croupier_total_points += 6
elif croupier_second_card == ['7 KIER'] or croupier_second_card == ['7 PIK'] or croupier_second_card == ['7 KARO'] or croupier_second_card == ['7 TREFL']:
    croupier_total_points += 7
elif croupier_second_card == ['8 KIER'] or croupier_second_card == ['8 PIK'] or croupier_second_card == ['8 KARO'] or croupier_second_card == ['8 TREFL']:
    croupier_total_points += 8
elif croupier_second_card == ['9 KIER'] or croupier_second_card == ['9 PIK'] or croupier_second_card == ['9 KARO'] or croupier_second_card == ['9 TREFL']:
    croupier_total_points +=9
elif croupier_second_card == ['As KIER'] or croupier_second_card == ['As PIK'] or croupier_second_card == ['As KARO'] or croupier_second_card == ['As TREFL']:
    croupier_total_points += 11
else:
    croupier_total_points +=10

 #counting points when player has ace
if player_first_card == ['As KIER'] or player_first_card == ['As PIK'] or player_first_card == ['As KARO'] or player_first_card == ['As TREFL'] or player_second_card == ['As KIER'] or player_second_card == ['As PIK'] or player_second_card == ['As KARO'] or player_second_card == ['As TREFL']:
    if player_total_points > 21:
        player_total_points = player_total_points - 10
        print("Suma towich punktów to:", player_total_points)
    elif player_total_points == 21:
        print("Suma towich punktów to:", player_total_points)
        print("Masz blackjacka! Sprawdźmy teraz co kryje się pod drugą kartą krupiera!")
        print("Druga karta krupiera to:", croupier_second_card)
        print("Suma punktów krupiera to:", croupier_total_points)
        if croupier_total_points == 21:
            print("Jest remis! Pieniądze wracją do ciebie. Nic nie tracisz, ale też nic nie wygrywasz.")
        else:
            print("Pokonałeś krupiera! Wygrałeś", 2* rate, "! Gratulację!")

    else:
        player_total_points = player_total_points
        print("Suma towich punktów to:", player_total_points)
else:
    player_total_points = player_total_points
    print("Suma towich punktów to:", player_total_points)



#possible actions when croupier's first card is ace - you can buy insurance and be sure that you won't lose your money or you can risk it all
    if croupier_first_card == ['As KIER'] or croupier_first_card == ['As PIK'] or croupier_first_card == ['As KARO'] or croupier_first_card == ['As TREFL']:
        choice_of_buying_insurance = input("Czy chcesz wykupić ubezpieczenie? ")
        if choice_of_buying_insurance == "tak" or choice_of_buying_insurance == "TAK" or choice_of_buying_insurance == "Tak":
            print("Jeśli chcesz wykupić ubezpieczenie musić wpłacić połowę swojej początkowej stawki")
            value_of_insurance = 0.5 * rate
            new_rate = value_of_insurance + rate
            print("Stawiasz dodatkowe", value_of_insurance, "złotych")
        else:
            print("Cóż, podejmujesz to ryzyko na własną odpowiedzialnosć. Grajmy dalej!")


#creating new round - the player is going to choose his next move now
if player_total_points <21:
    print("Przyszedł czas na podjęcie ważnej decyzji!")
    print("Jeśli chcesz dobrać kolejną kartę wpisz: 'hit'")
    print("Jeśli nie chcesz dobierać kart wpisz: 'stand'")
    first_choice_of_move = input()
    if first_choice_of_move == "hit" or first_choice_of_move == "HIT" or first_choice_of_move == "Hit":
        player_third_card = random.choice(deck)
        print("Twoja trzecia karta to:", player_third_card)

        if player_third_card == ['2 KIER'] or player_third_card == ['2 PIK'] or player_third_card == ['2 KARO'] or player_third_card == ['2 TREFL']:
            player_total_points += 2
        elif player_third_card == ['3 KIER'] or player_third_card == ['3 PIK'] or player_third_card == ['3 KARO'] or player_third_card == ['3 TREFL']:
            player_total_points += 3
        elif player_third_card == ['4 KIER'] or player_third_card == ['4 PIK'] or player_third_card == ['4 KARO'] or player_third_card == ['4 TREFL']:
            player_total_points += 4
        elif player_third_card == ['5 KIER'] or player_third_card == ['5 PIK'] or player_third_card == ['5 KARO'] or player_third_card == ['5 TREFL']:
            player_total_points += 5
        elif player_third_card == ['6 KIER'] or player_third_card == ['6 PIK'] or player_third_card == ['6 KARO'] or player_third_card == ['6 TREFL']:
            player_total_points += 6
        elif player_third_card == ['7 KIER'] or player_third_card == ['7 PIK'] or player_third_card == ['7 KARO'] or player_third_card == ['7 TREFL']:
            player_total_points += 7
        elif player_third_card == ['8 KIER'] or player_third_card == ['8 PIK'] or player_third_card == ['8 KARO'] or player_third_card == ['8 TREFL']:
            player_total_points += 8
        elif player_third_card == ['9 KIER'] or player_third_card == ['9 PIK'] or player_third_card == ['9 KARO'] or player_third_card == ['9 TREFL']:
            player_total_points +=9
        elif player_third_card == ['As KIER'] or player_third_card == ['As PIK'] or player_third_card == ['As KARO'] or player_third_card == ['As TREFL']:
            player_total_points += 11
            if player_total_points > 21:
                player_total_points = player_total_points -10
            else:
                player_total_points = player_total_points
        else:
            player_total_points +=10

        print("Suma twoich punktów to:", player_total_points)
        if player_total_points < 21:
            print("Znowu podejmujesz decyzję!")
            print("Jeśli chcesz dobrać kartę wpisz: 'hit'")
            print("Jesli nie chcesz dobierać kart wpisz: 'stand'")
            second_choice_of_move = input()
            if second_choice_of_move == "hit" or second_choice_of_move == "HIT" or second_choice_of_move == "Hit":
                player_fourth_card = random.choice(deck)
                print("Twoja czwarta karta to:", player_fourth_card)
                if player_fourth_card == ['2 KIER'] or player_fourth_card == ['2 PIK'] or player_fourth_card == ['2 KARO'] or player_fourth_card == ['2 TREFL']:
                    player_total_points += 2
                elif player_fourth_card == ['3 KIER'] or player_fourth_card == ['3 PIK'] or player_fourth_card == ['3 KARO'] or player_fourth_card == ['3 TREFL']:
                    player_total_points += 3
                elif player_fourth_card == ['4 KIER'] or player_fourth_card == ['4 PIK'] or player_fourth_card == ['4 KARO'] or player_fourth_card == ['4 TREFL']:
                    player_total_points += 4
                elif player_fourth_card == ['5 KIER'] or player_fourth_card == ['5 PIK'] or player_fourth_card == ['5 KARO'] or player_fourth_card == ['5 TREFL']:
                    player_total_points += 5
                elif player_fourth_card == ['6 KIER'] or player_fourth_card == ['6 PIK'] or player_fourth_card == ['6 KARO'] or player_fourth_card == ['6 TREFL']:
                    player_total_points += 6
                elif player_fourth_card == ['7 KIER'] or player_fourth_card == ['7 PIK'] or player_fourth_card == ['7 KARO'] or player_fourth_card == ['7 TREFL']:
                    player_total_points += 7
                elif player_fourth_card == ['8 KIER'] or player_fourth_card == ['8 PIK'] or player_fourth_card == ['8 KARO'] or player_fourth_card == ['8 TREFL']:
                    player_total_points += 8
                elif player_fourth_card == ['9 KIER'] or player_fourth_card == ['9 PIK'] or player_fourth_card == ['9 KARO'] or player_fourth_card == ['9 TREFL']:
                    player_total_points +=9
                elif player_fourth_card == ['As KIER'] or player_fourth_card == ['As PIK'] or player_fourth_card == ['As KARO'] or player_fourth_card == ['As TREFL']:
                    player_total_points += 11
                    if player_total_points >21:
                        player_total_points = player_total_points - 10
                    else:
                        player_total_points = player_total_points
                else:
                    player_total_points +=10
                print("Suma twoich punktów to:", player_total_points)
                if player_total_points < 21:
                    print("Znowu podejmujesz decyzję!")
                    print("Jeśli chcesz dobrać kartę wpisz: 'hit'")
                    print("Jesli nie chcesz dobierać kart wpisz: 'stand'")
                    third_choice_of_move = input()
                    if third_choice_of_move == "hit" or third_choice_of_move == "HIT" or third_choice_of_move == "Hit":
                        player_fith_card = random.choice(deck)
                        print("Twoja piąta karta to:", player_fith_card)
                        if player_fith_card == ['2 KIER'] or player_fith_card == ['2 PIK'] or player_fith_card == ['2 KARO'] or player_fith_card == ['2 TREFL']:
                            player_total_points += 2
                        elif player_fith_card == ['3 KIER'] or player_fith_card == ['3 PIK'] or player_fith_card == ['3 KARO'] or player_fith_card == ['3 TREFL']:
                            player_total_points += 3
                        elif player_fith_card == ['4 KIER'] or player_fith_card == ['4 PIK'] or player_fith_card == ['4 KARO'] or player_fith_card == ['4 TREFL']:
                            player_total_points += 4
                        elif player_fith_card == ['5 KIER'] or player_fith_card == ['5 PIK'] or player_fith_card == ['5 KARO'] or player_fith_card == ['5 TREFL']:
                            player_total_points += 5
                        elif player_fith_card == ['6 KIER'] or player_fith_card == ['6 PIK'] or player_fith_card == ['6 KARO'] or player_fith_card == ['6 TREFL']:
                            player_total_points += 6
                        elif player_fith_card == ['7 KIER'] or player_fith_card == ['7 PIK'] or player_fith_card == ['7 KARO'] or player_fith_card == ['7 TREFL']:
                            player_total_points += 7
                        elif player_fith_card == ['8 KIER'] or player_fith_card == ['8 PIK'] or player_fith_card == ['8 KARO'] or player_fith_card == ['8 TREFL']:
                            player_total_points += 8
                        elif player_fith_card == ['9 KIER'] or player_fith_card == ['9 PIK'] or player_fith_card == ['9 KARO'] or player_fith_card == ['9 TREFL']:
                            player_total_points +=9
                        elif player_fith_card == ['As KIER'] or player_fith_card == ['As PIK'] or player_fith_card == ['As KARO'] or player_fith_card == ['As TREFL']:
                            player_total_points += 11
                            if player_total_points >21:
                                player_total_points = player_total_points - 10
                            else:
                                player_total_points = player_total_points
                        else:
                            player_total_points +=10
                        print("Suma twoich punktów to:", player_total_points)
                        print("Suma punktów krupiera to:", croupier_total_points)
                        if croupier_total_points > player_total_points and croupier_total_points <= 21:
                           print("Krupier wygrywa, tracisz postawione pieniądze.")
                        elif croupier_total_points > 21:
                           print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")
                        elif croupier_total_points == 21 and croupier_first_card == ['As KIER'] or croupier_total_points ==21 and croupier_first_card == ['As PIK'] or croupier_total_points == 21 and croupier_first_card == ['As KARO'] or croupier_total_points == 21 and croupier_first_card == ['As TREFL']:
                            if choice_of_buying_insurance == "tak" or choice_of_buying_insurance == "TAK" or choice_of_buying_insurance == "Tak":
                                print("Krupier ma BLACKJACKA! Ty na szczęscię wykupiłeś ubezpieczenie, więc nic nie tracisz")
                            else:
                                print("Krupier ma BLACKJACKA! Tracisz postawione pieniądze")
                    else:
                        print("Druga karta krupiera to:", croupier_second_card)
                        print("Suma twoich punktów to:", player_total_points)
                        print("Suma punktów krupiera to:", croupier_total_points)
                        if croupier_total_points < 17:
                            print("Krupier dobiera kolejną kartę")
                            croupier_third_card = random.choice(deck)
                            print("Trzecia karta krupiera to:", croupier_third_card)
                            if croupier_third_card == ['2 KIER'] or croupier_third_card == ['2 PIK'] or croupier_third_card == ['2 KARO'] or croupier_third_card == ['2 TREFL']:
                                 croupier_total_points += 2
                            elif croupier_third_card == ['3 KIER'] or croupier_third_card == ['3 PIK'] or croupier_third_card == ['3 KARO'] or croupier_third_card == ['3 TREFL']:
                                croupier_total_points += 3
                            elif croupier_third_card == ['4 KIER'] or croupier_third_card == ['4 PIK'] or croupier_third_card == ['4 KARO'] or croupier_third_card == ['4 TREFL']:
                                croupier_total_points += 4
                            elif croupier_third_card == ['5 KIER'] or croupier_third_card == ['5 PIK'] or croupier_third_card == ['5 KARO'] or croupier_third_card == ['5 TREFL']:
                                croupier_total_points += 5
                            elif croupier_third_card == ['6 KIER'] or croupier_third_card == ['6 PIK'] or croupier_third_card == ['6 KARO'] or croupier_third_card == ['6 TREFL']:
                                croupier_total_points += 6
                            elif croupier_third_card == ['7 KIER'] or croupier_third_card == ['7 PIK'] or croupier_third_card == ['7 KARO'] or croupier_third_card == ['7 TREFL']:
                                croupier_total_points += 7
                            elif croupier_third_card == ['8 KIER'] or croupier_third_card == ['8 PIK'] or croupier_third_card == ['8 KARO'] or croupier_third_card == ['8 TREFL']:
                                croupier_total_points += 8
                            elif croupier_third_card == ['9 KIER'] or croupier_third_card == ['9 PIK'] or croupier_third_card == ['9 KARO'] or croupier_third_card == ['9 TREFL']:
                                croupier_total_points +=9
                            elif croupier_third_card == ['As KIER'] or croupier_third_card == ['As PIK'] or croupier_third_card == ['As KARO'] or croupier_third_card == ['As TREFL']:
                                croupier_total_points += 11
                            else:
                                croupier_total_points +=10
                            print("Suma punktów krupiera to:", croupier_total_points)
                            if croupier_total_points <17:
                                print("Krupier dobiera kolejną kartę")
                                croupier_fourth_card = random.choice(deck)
                                print("Czwarta karta krupiera to:", croupier_fourth_card)
                                if croupier_fourth_card == ['2 KIER'] or croupier_fourth_card == ['2 PIK'] or croupier_fourth_card == ['2 KARO'] or croupier_fourth_card == ['2 TREFL']:
                                     croupier_total_points += 2
                                elif croupier_fourth_card == ['3 KIER'] or croupier_fourth_card == ['3 PIK'] or croupier_fourth_card == ['3 KARO'] or croupier_fourth_card == ['3 TREFL']:
                                    croupier_total_points += 3
                                elif croupier_fourth_card == ['4 KIER'] or croupier_fourth_card == ['4 PIK'] or croupier_fourth_card == ['4 KARO'] or croupier_fourth_card == ['4 TREFL']:
                                    croupier_total_points += 4
                                elif croupier_fourth_card == ['5 KIER'] or croupier_fourth_card == ['5 PIK'] or croupier_fourth_card == ['5 KARO'] or croupier_fourth_card == ['5 TREFL']:
                                    croupier_total_points += 5
                                elif croupier_fourth_card == ['6 KIER'] or croupier_fourth_card == ['6 PIK'] or croupier_fourth_card == ['6 KARO'] or croupier_fourth_card == ['6 TREFL']:
                                    croupier_total_points += 6
                                elif croupier_fourth_card == ['7 KIER'] or croupier_fourth_card == ['7 PIK'] or croupier_fourth_card == ['7 KARO'] or croupier_fourth_card == ['7 TREFL']:
                                    croupier_total_points += 7
                                elif croupier_fourth_card == ['8 KIER'] or croupier_fourth_card == ['8 PIK'] or croupier_fourth_card == ['8 KARO'] or croupier_fourth_card == ['8 TREFL']:
                                    croupier_total_points += 8
                                elif croupier_fourth_card == ['9 KIER'] or croupier_fourth_card == ['9 PIK'] or croupier_fourth_card == ['9 KARO'] or croupier_fourth_card == ['9 TREFL']:
                                    croupier_total_points +=9
                                elif croupier_fourth_card == ['As KIER'] or croupier_fourth_card == ['As PIK'] or croupier_fourth_card == ['As KARO'] or croupier_fourth_card == ['As TREFL']:
                                    croupier_total_points += 11
                                else:
                                    croupier_total_points +=10
                                print("Suma punktów krupiera to:", croupier_total_points)
                                if croupier_total_points > player_total_points and croupier_total_points <= 21:
                                   print("Krupier wygrywa, tracisz postawione pieniądze.")
                                elif croupier_total_points > 21:
                                   print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")
                                elif croupier_total_points == 21 and croupier_first_card == ['As KIER'] or croupier_total_points ==21 and croupier_first_card == ['As PIK'] or croupier_total_points == 21 and croupier_first_card == ['As KARO'] or croupier_total_points == 21 and croupier_first_card == ['As TREFL']:
                                    if choice_of_buying_insurance == "tak" or choice_of_buying_insurance == "TAK" or choice_of_buying_insurance == "Tak":
                                        print("Krupier ma BLACKJACKA! Ty na szczęscię wykupiłeś ubezpieczenie, więc nic nie tracisz")
                                    else:
                                        print("Krupier ma BLACKJACKA! Tracisz postawione pieniądze")
                                else:
                                    print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")
                            else:
                                if croupier_total_points > player_total_points and croupier_total_points <= 21:
                                   print("Krupier wygrywa, tracisz postawione pieniądze.")
                                elif croupier_total_points > 21:
                                   print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")
                                elif croupier_total_points == 21 and croupier_first_card == ['As KIER'] or croupier_total_points ==21 and croupier_first_card == ['As PIK'] or croupier_total_points == 21 and croupier_first_card == ['As KARO'] or croupier_total_points == 21 and croupier_first_card == ['As TREFL']:
                                    if choice_of_buying_insurance == "tak" or choice_of_buying_insurance == "TAK" or choice_of_buying_insurance == "Tak":
                                        print("Krupier ma BLACKJACKA! Ty na szczęscię wykupiłeś ubezpieczenie, więc nic nie tracisz")
                                    else:
                                        print("Krupier ma BLACKJACKA! Tracisz postawione pieniądze")
                                else:
                                    print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")

                elif  player_total_points == 21:
                    print("Suma punktów krupiera to:", croupier_total_points)
                    if croupier_total_points == 21:
                        print("Jest remis! Pieniądze wracją do ciebie. Nic nie tracisz, ale też nic nie wygrywasz.")
                    else:
                        print("Pokonałeś krupiera! Wygrałeś", 2* rate, "! Gratulację!")
                else:
                    print("Masz więcej punktów niż 21. Przegrałeś. Tracisz postawione pieniądze")


            else:
                print("Druga karta krupiera to:", croupier_second_card)
                print("Suma twoich punktów to:", player_total_points)
                print("Suma punktów krupiera to:", croupier_total_points)
                if croupier_total_points < 17:
                    print("Krupier dobiera kolejną kartę")
                    croupier_third_card = random.choice(deck)
                    print("Trzecia karta krupiera to:", croupier_third_card)
                    if croupier_third_card == ['2 KIER'] or croupier_third_card == ['2 PIK'] or croupier_third_card == ['2 KARO'] or croupier_third_card == ['2 TREFL']:
                         croupier_total_points += 2
                    elif croupier_third_card == ['3 KIER'] or croupier_third_card == ['3 PIK'] or croupier_third_card == ['3 KARO'] or croupier_third_card == ['3 TREFL']:
                        croupier_total_points += 3
                    elif croupier_third_card == ['4 KIER'] or croupier_third_card == ['4 PIK'] or croupier_third_card == ['4 KARO'] or croupier_third_card == ['4 TREFL']:
                        croupier_total_points += 4
                    elif croupier_third_card == ['5 KIER'] or croupier_third_card == ['5 PIK'] or croupier_third_card == ['5 KARO'] or croupier_third_card == ['5 TREFL']:
                        croupier_total_points += 5
                    elif croupier_third_card == ['6 KIER'] or croupier_third_card == ['6 PIK'] or croupier_third_card == ['6 KARO'] or croupier_third_card == ['6 TREFL']:
                        croupier_total_points += 6
                    elif croupier_third_card == ['7 KIER'] or croupier_third_card == ['7 PIK'] or croupier_third_card == ['7 KARO'] or croupier_third_card == ['7 TREFL']:
                        croupier_total_points += 7
                    elif croupier_third_card == ['8 KIER'] or croupier_third_card == ['8 PIK'] or croupier_third_card == ['8 KARO'] or croupier_third_card == ['8 TREFL']:
                        croupier_total_points += 8
                    elif croupier_third_card == ['9 KIER'] or croupier_third_card == ['9 PIK'] or croupier_third_card == ['9 KARO'] or croupier_third_card == ['9 TREFL']:
                        croupier_total_points +=9
                    elif croupier_third_card == ['As KIER'] or croupier_third_card == ['As PIK'] or croupier_third_card == ['As KARO'] or croupier_third_card == ['As TREFL']:
                        croupier_total_points += 11
                    else:
                        croupier_total_points +=10
                    print("Suma punktów krupiera to:", croupier_total_points)
                    if croupier_total_points <17:
                        print("Krupier dobiera kolejną kartę")
                        croupier_fourth_card = random.choice(deck)
                        print("Czwarta karta krupiera to:", croupier_fourth_card)
                        if croupier_fourth_card == ['2 KIER'] or croupier_fourth_card == ['2 PIK'] or croupier_fourth_card == ['2 KARO'] or croupier_fourth_card == ['2 TREFL']:
                             croupier_total_points += 2
                        elif croupier_fourth_card == ['3 KIER'] or croupier_fourth_card == ['3 PIK'] or croupier_fourth_card == ['3 KARO'] or croupier_fourth_card == ['3 TREFL']:
                            croupier_total_points += 3
                        elif croupier_fourth_card == ['4 KIER'] or croupier_fourth_card == ['4 PIK'] or croupier_fourth_card == ['4 KARO'] or croupier_fourth_card == ['4 TREFL']:
                            croupier_total_points += 4
                        elif croupier_fourth_card == ['5 KIER'] or croupier_fourth_card == ['5 PIK'] or croupier_fourth_card == ['5 KARO'] or croupier_fourth_card == ['5 TREFL']:
                            croupier_total_points += 5
                        elif croupier_fourth_card == ['6 KIER'] or croupier_fourth_card == ['6 PIK'] or croupier_fourth_card == ['6 KARO'] or croupier_fourth_card == ['6 TREFL']:
                            croupier_total_points += 6
                        elif croupier_fourth_card == ['7 KIER'] or croupier_fourth_card == ['7 PIK'] or croupier_fourth_card == ['7 KARO'] or croupier_fourth_card == ['7 TREFL']:
                            croupier_total_points += 7
                        elif croupier_fourth_card == ['8 KIER'] or croupier_fourth_card == ['8 PIK'] or croupier_fourth_card == ['8 KARO'] or croupier_fourth_card == ['8 TREFL']:
                            croupier_total_points += 8
                        elif croupier_fourth_card == ['9 KIER'] or croupier_fourth_card == ['9 PIK'] or croupier_fourth_card == ['9 KARO'] or croupier_fourth_card == ['9 TREFL']:
                            croupier_total_points +=9
                        elif croupier_fourth_card == ['As KIER'] or croupier_fourth_card == ['As PIK'] or croupier_fourth_card == ['As KARO'] or croupier_fourth_card == ['As TREFL']:
                            croupier_total_points += 11
                        else:
                            croupier_total_points +=10
                        print("Suma punktów krupiera to:", croupier_total_points)
                        if croupier_total_points > player_total_points and croupier_total_points <= 21:
                           print("Krupier wygrywa, tracisz postawione pieniądze.")
                        elif croupier_total_points > 21:
                           print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")
                        elif croupier_total_points == 21 and croupier_first_card == ['As KIER'] or croupier_total_points ==21 and croupier_first_card == ['As PIK'] or croupier_total_points == 21 and croupier_first_card == ['As KARO'] or croupier_total_points == 21 and croupier_first_card == ['As TREFL']:
                            if choice_of_buying_insurance == "tak" or choice_of_buying_insurance == "TAK" or choice_of_buying_insurance == "Tak":
                                print("Krupier ma BLACKJACKA! Ty na szczęscię wykupiłeś ubezpieczenie, więc nic nie tracisz")
                            else:
                                print("Krupier ma BLACKJACKA! Tracisz postawione pieniądze")
                        else:
                            print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")
                    else:
                        if croupier_total_points > player_total_points and croupier_total_points <= 21:
                           print("Krupier wygrywa, tracisz postawione pieniądze.")
                        elif croupier_total_points > 21:
                           print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")
                        elif croupier_total_points == 21 and croupier_first_card == ['As KIER'] or croupier_total_points ==21 and croupier_first_card == ['As PIK'] or croupier_total_points == 21 and croupier_first_card == ['As KARO'] or croupier_total_points == 21 and croupier_first_card == ['As TREFL']:
                            if choice_of_buying_insurance == "tak" or choice_of_buying_insurance == "TAK" or choice_of_buying_insurance == "Tak":
                                print("Krupier ma BLACKJACKA! Ty na szczęscię wykupiłeś ubezpieczenie, więc nic nie tracisz")
                            else:
                                print("Krupier ma BLACKJACKA! Tracisz postawione pieniądze")
                        else:
                            print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")


                else:
                    if croupier_total_points > player_total_points and croupier_total_points <= 21:
                       print("Krupier wygrywa, tracisz postawione pieniądze.")
                    elif croupier_total_points > 21:
                       print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")
                    elif croupier_total_points == 21 and croupier_first_card == ['As KIER'] or croupier_total_points ==21 and croupier_first_card == ['As PIK'] or croupier_total_points == 21 and croupier_first_card == ['As KARO'] or croupier_total_points == 21 and croupier_first_card == ['As TREFL']:
                        if choice_of_buying_insurance == "tak" or choice_of_buying_insurance == "TAK" or choice_of_buying_insurance == "Tak":
                            print("Krupier ma BLACKJACKA! Ty na szczęscię wykupiłeś ubezpieczenie, więc nic nie tracisz")
                        else:
                            print("Krupier ma BLACKJACKA! Tracisz postawione pieniądze")
                    else:
                        print("Pokonałeś krupiera! Wygrywasz", 2 * rate, "złotych! Gratulacje!")

        elif player_total_points == 21:
            print("Suma punktów krupiera to:", croupier_total_points)
            if croupier_total_points == 21:
                print("Jest remis! Pieniądze wracją do ciebie. Nic nie tracisz, ale też nic nie wygrywasz.")
            else:
                print("Pokonałeś krupiera! Wygrałeś", 2* rate, "! Gratulację!")
        else:
            print("Masz więcej punktów niż 21. Przegrałeś. Tracisz postawione pieniądze")


    else:
        print("Druga karta krupiera to:", croupier_second_card)
        print("Suma twoich punktów to:", player_total_points)
        print("Suma punktów krupiera to:", croupier_total_points)
        if croupier_total_points < 17:
            print("Krupier dobiera kolejną kartę")
            croupier_third_card = random.choice(deck)
            print("Trzecia karta krupiera to:", croupier_third_card)
            if croupier_third_card == ['2 KIER'] or croupier_third_card == ['2 PIK'] or croupier_third_card == ['2 KARO'] or croupier_third_card == ['2 TREFL']:
                 croupier_total_points += 2
            elif croupier_third_card == ['3 KIER'] or croupier_third_card == ['3 PIK'] or croupier_third_card == ['3 KARO'] or croupier_third_card == ['3 TREFL']:
                croupier_total_points += 3
            elif croupier_third_card == ['4 KIER'] or croupier_third_card == ['4 PIK'] or croupier_third_card == ['4 KARO'] or croupier_third_card == ['4 TREFL']:
                croupier_total_points += 4
            elif croupier_third_card == ['5 KIER'] or croupier_third_card == ['5 PIK'] or croupier_third_card == ['5 KARO'] or croupier_third_card == ['5 TREFL']:
                croupier_total_points += 5
            elif croupier_third_card == ['6 KIER'] or croupier_third_card == ['6 PIK'] or croupier_third_card == ['6 KARO'] or croupier_third_card == ['6 TREFL']:
                croupier_total_points += 6
            elif croupier_third_card == ['7 KIER'] or croupier_third_card == ['7 PIK'] or croupier_third_card == ['7 KARO'] or croupier_third_card == ['7 TREFL']:
                croupier_total_points += 7
            elif croupier_third_card == ['8 KIER'] or croupier_third_card == ['8 PIK'] or croupier_third_card == ['8 KARO'] or croupier_third_card == ['8 TREFL']:
                croupier_total_points += 8
            elif croupier_third_card == ['9 KIER'] or croupier_third_card == ['9 PIK'] or croupier_third_card == ['9 KARO'] or croupier_third_card == ['9 TREFL']:
                croupier_total_points +=9
            elif croupier_third_card == ['As KIER'] or croupier_third_card == ['As PIK'] or croupier_third_card == ['As KARO'] or croupier_third_card == ['As TREFL']:
                croupier_total_points += 11
            else:
                croupier_total_points +=10
            print("Suma punktów krupiera to:", croupier_total_points)
            if croupier_total_points < 17:
                print("Krupier dobiera kolejną kartę")
                croupier_fourth_card = random.choice(deck)
                print("Czwarta karta krupiera to:", croupier_fourth_card)
                if croupier_fourth_card == ['2 KIER'] or croupier_fourth_card == ['2 PIK'] or croupier_fourth_card == ['2 KARO'] or croupier_fourth_card == ['2 TREFL']:
                     croupier_total_points += 2
                elif croupier_fourth_card == ['3 KIER'] or croupier_fourth_card == ['3 PIK'] or croupier_fourth_card == ['3 KARO'] or croupier_fourth_card == ['3 TREFL']:
                    croupier_total_points += 3
                elif croupier_fourth_card == ['4 KIER'] or croupier_fourth_card == ['4 PIK'] or croupier_fourth_card == ['4 KARO'] or croupier_fourth_card == ['4 TREFL']:
                    croupier_total_points += 4
                elif croupier_fourth_card == ['5 KIER'] or croupier_fourth_card == ['5 PIK'] or croupier_fourth_card == ['5 KARO'] or croupier_fourth_card == ['5 TREFL']:
                    croupier_total_points += 5
                elif croupier_fourth_card == ['6 KIER'] or croupier_fourth_card == ['6 PIK'] or croupier_fourth_card == ['6 KARO'] or croupier_fourth_card == ['6 TREFL']:
                    croupier_total_points += 6
                elif croupier_fourth_card == ['7 KIER'] or croupier_fourth_card == ['7 PIK'] or croupier_fourth_card == ['7 KARO'] or croupier_fourth_card == ['7 TREFL']:
                    croupier_total_points += 7
                elif croupier_fourth_card == ['8 KIER'] or croupier_fourth_card == ['8 PIK'] or croupier_fourth_card == ['8 KARO'] or croupier_fourth_card == ['8 TREFL']:
                    croupier_total_points += 8
                elif croupier_fourth_card == ['9 KIER'] or croupier_fourth_card == ['9 PIK'] or croupier_fourth_card == ['9 KARO'] or croupier_fourth_card == ['9 TREFL']:
                    croupier_total_points +=9
                elif croupier_fourth_card == ['As KIER'] or croupier_fourth_card == ['As PIK'] or croupier_fourth_card == ['As KARO'] or croupier_fourth_card == ['As TREFL']:
                    croupier_total_points += 11
                else:
                    croupier_total_points +=10
                print("Suma punktów krupiera to:", croupier_total_points)
                if croupier_total_points > player_total_points and croupier_total_points <= 21:
                   print("Krupier wygrywa, tracisz postawione pieniądze.")
                elif croupier_total_points > 21:
                   print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")
                elif croupier_total_points == 21 and croupier_first_card == ['As KIER'] or croupier_total_points ==21 and croupier_first_card == ['As PIK'] or croupier_total_points == 21 and croupier_first_card == ['As KARO'] or croupier_total_points == 21 and croupier_first_card == ['As TREFL']:
                    if choice_of_buying_insurance == "tak" or choice_of_buying_insurance == "TAK" or choice_of_buying_insurance == "Tak":
                        print("Krupier ma BLACKJACKA! Ty na szczęscię wykupiłeś ubezpieczenie, więc nic nie tracisz")
                    else:
                        print("Krupier ma BLACKJACKA! Tracisz postawione pieniądze")
                else:
                    print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")

            else:
                if croupier_total_points > player_total_points and croupier_total_points <= 21:
                   print("Krupier wygrywa, tracisz postawione pieniądze.")
                elif croupier_total_points > 21:
                   print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")
                elif croupier_total_points == 21 and croupier_first_card == ['As KIER'] or croupier_total_points ==21 and croupier_first_card == ['As PIK'] or croupier_total_points == 21 and croupier_first_card == ['As KARO'] or croupier_total_points == 21 and croupier_first_card == ['As TREFL']:
                    if choice_of_buying_insurance == "tak" or choice_of_buying_insurance == "TAK" or choice_of_buying_insurance == "Tak":
                        print("Krupier ma BLACKJACKA! Ty na szczęscię wykupiłeś ubezpieczenie, więc nic nie tracisz")
                    else:
                        print("Krupier ma BLACKJACKA! Tracisz postawione pieniądze")
                else:
                    print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")


        else:
            if croupier_total_points > player_total_points and croupier_total_points <= 21:
               print("Krupier wygrywa, tracisz postawione pieniądze.")
            elif croupier_total_points > 21:
               print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")
            elif croupier_total_points == 21 and croupier_first_card == ['As KIER'] or croupier_total_points ==21 and croupier_first_card == ['As PIK'] or croupier_total_points == 21 and croupier_first_card == ['As KARO'] or croupier_total_points == 21 and croupier_first_card == ['As TREFL']:
                if choice_of_buying_insurance == "tak" or choice_of_buying_insurance == "TAK" or choice_of_buying_insurance == "Tak":
                    print("Krupier ma BLACKJACKA! Ty na szczęscię wykupiłeś ubezpieczenie, więc nic nie tracisz")
                else:
                    print("Krupier ma BLACKJACKA! Tracisz postawione pieniądze")
            else:
                print("Krupier przgerywa, wygrywasz", 2* rate, "złotych")



else:
    print("To już koniec gry")

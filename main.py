# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

#Daniils Baranovs 10B

import random
# ievadam visus mainīgos
player1_name = str()
player2_name = str()
player1_pos = 1
player2_pos = 1

#prasam spēlētājus, lai tie ivadītu savu vārdu    
print("spēlētājs nr1 ievadiet savu vārdu")
player1_name = input()
    
print("spēlētājs nr2 ievadiet savu vārdu")
player2_name = input()
#cikls for atkārtos kodu 25 reizes
for _ in range(25):
#prasam mest kauliņu
    print(player1_name + " lai mest kauliņu, press enter ")
    player1_turn = input()
#ņemam random ciparu
    random_1 = random.randint(1, 6)
    player1_pos = player1_pos + random_1
    print("jums izkrita: " + str(random_1))
#tas pats tikai 2 spēlētājam   
    print(player2_name + " lai mest kauliņu, press enter ")
    player2_turn = input()
    random_2 = random.randint(1,6)
    player2_pos = player2_pos + random_2
    print("jums izkrita: " + str(random_2))

    
#pārbaudam kāpnes
    if player1_pos == 18:
        player1_pos = player1_pos-11
        print(player1_name + " uzkāpa uz kāpnēm: - 11")
    elif player1_pos == 67:
        player1_pos=player1_pos-21
        print(player1_name + " uzkāpa uz kāpnēm: - 21")
    elif player1_pos == 80:
        player1_pos=player1_pos-11
        print(player1_name + " uzkāpa uz kāpnēm: - 11")
    elif player1_pos == 74:
        player1_pos=player1_pos-11
        print(player1_name + " uzkāpa uz kāpnēm: - 11")
    
#pārbaudam kāpnes    
    if player2_pos == 18:
        player2_pos== player2_pos-11
        print(player1_name + " uzkāpa uz kāpnēm: - 11")
    elif player2_pos == 67:
        player2_pos=player2_pos-21
        print(player1_name + " uzkāpa uz kāpnēm: - 21")
    elif player2_pos == 80:
        player2_pos=player2_pos-11
        print(player1_name + " uzkāpa uz kāpnēm: - 11")
    elif player2_pos == 74:
        player2_pos=player2_pos-11
        print(player1_name + " uzkāpa uz kāpnēm: - 11")    

#pārbaudam kāpnes    
    if player1_pos == 15:
        player1_pos = player1_pos+9
        print(player1_name + " uzkāpa uz kāpnēm: + 9")
    elif player1_pos == 39:
        player1_pos=player1_pos+9
        print(player1_name + " uzkāpa uz kāpnēm: + 19")
    elif player1_pos == 52:
        player1_pos=player1_pos+19
        print(player1_name + " uzkāpa uz kāpnēm: + 9")
    elif player1_pos == 87:
        player1_pos=player1_pos+9
        print(player1_name + " uzkāpa uz kāpnēm: + 9")

#pārbaudam kāpnes
    if player2_pos == 15:
        player2_pos = player2_pos+9
        print(player1_name + " uzkāpa uz kāpnēm: + 9")
    elif player2_pos == 39:
        player2_pos=player2_pos+9
        print(player1_name + " uzkāpa uz kāpnēm: + 19")
    elif player2_pos == 52:
        player2_pos=player2_pos+19
        print(player1_name + " uzkāpa uz kāpnēm: + 9")
    elif player2_pos == 87:
        player2_pos=player2_pos+9
        print(player1_name + " uzkāpa uz kāpnēm: + 9")

#pārbaudam vinnētāju
    if player1_pos >= 100:
        print(player1_name + " tu esi vinnējis")
        break

    if player2_pos >= 100:
        print(player2_name + " tu esi vinnējis")
        break
    if player2_pos > 100 and player1_pos > 100:
        print("abi vinnēja")
        break
#izvadam spēlētāju vietas
    print(player1_name + " atrodas lauciņā nr " + str(player1_pos))
    
    print(player2_name + " atrodas lauciņā nr " + str(player2_pos))

#pēc 25 koda atkartojumiem, būs neizšķirts
if player1_pos < 100 and player2_pos < 100:
    print( "neizšķirts, ļoti daudz mēģinājumu")
        



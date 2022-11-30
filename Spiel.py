import json
from collections import defaultdict
import random
from random import randint






def Game(player):
    
    l = ["Stein", "Papier", "Schere", "Echse", "Spock"]
    count= {"Stein":0, "Papier":0, "Schere":0, "Echse":0, "Spock":0} 


    comp = l[randint(0,4)]

   
    #for v in comp:
    #       count[v]+=1

    count[comp] +=1


    #player = input("Wähle Stein, Papier, Schere, Echse, Spock ")

    count[player] +=1
   
    print("Computer wählt " + str(comp))

    compst = 0
    playerst= 0
    draw = 0

    if (player == "Stein" and comp == "Schere") or (player == "Stein" and comp == "Echse") or (player == "Papier" and comp == "Stein") or (player == "Schere" and comp == "Papier") or (player == "Schere" and comp == "Echse")  or (player == 'Spock' and comp == "Stein") or (player == "Echse" and comp == "Papier") or (player == "Echse" and comp == 'Spock') or (player == "Papier" and comp == "Spock") or (player == 'Spock' and comp == "Schere"):
        print("Gewonnen! ")
        playerst += 1
    
    elif (player == "Stein" and comp == "Papier") or (player == "Stein" and comp == 'Spock') or (player == "Papier" and comp == "Schere") or (player == "Papier" and comp == "Echse") or (player == "Schere" and comp == "Stein") or (player == "Schere" and comp == 'Spock') or (player == 'Spock' and comp == "Papier") or (player == 'Spock' and comp == "Echse") or (player == "Echse" and comp == "Stein") or (player == "Echse" and comp == "Schere"):
        print("Verloren :((( ")
        compst += 1

    else:
        print("Unentschieden ")
        draw += 1

    print(count)
    
    
    
if __name__ == '__main__':
    Game(player = input("Wähle Stein, Papier, Schere, Echse, Spock "))
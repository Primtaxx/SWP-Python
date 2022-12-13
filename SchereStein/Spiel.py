import json
from collections import defaultdict
import random
from random import randint
import json

import requests
import rest

def Analyse():
    with open('mydata.json', 'r') as f:
        analyse = json.load(f)
        print(" ")
        print("Anzahl der gewonnenen Spiele Spieler: " + str(analyse["playerwins"]))
        print("Symbole gezogen Spieler: " + "Stein: " + str(analyse["playerstats"]["stein"]) + " " + "Schere: " + str(analyse["playerstats"]["schere"]) + " " + "Papier: " + str(analyse["playerstats"]["papier"]) + " " + "Echse: " + str(analyse["playerstats"]["echse"]) + " " + "Spock: " + str(analyse["playerstats"]["spock"]))
        print(" ")
        print("Anzahl der gewonnenen Spiele Computer: " + str(analyse["computerwins"]))
        print("Symbole gezogen Computer: " + "Stein: " + str(analyse["compstats"]["stein"]) + " " + "Schere: " + str(analyse["compstats"]["schere"]) + " " + "Papier: " + str(analyse["compstats"]["papier"]) + " " + "Echse: " + str(analyse["compstats"]["echse"]) + " " + "Spock: " + str(analyse["compstats"]["spock"]))
        print(" ")
        print("Unentschieden: " + str(analyse["computerwins"]))
        print(" ")
        

def Game(player, comp):
    
    with open('mydata.json', 'r+') as f:
        spiel = json.load(f)

        # l = ["Stein", "Papier", "Schere", "Echse", "Spock"]
        # count= {"Stein":0, "Papier":0, "Schere":0, "Echse":0, "Spock":0} 


        # comp = l[randint(0,4)]

   
        #for v in comp:
        #       count[v]+=1

        #count[comp] +=1
        spiel["compstats"][str(comp).lower()] = spiel["compstats"][str(comp).lower()] + 1
        f.seek(0)
        json.dump(spiel, f, indent=4)
        spiel["playerstats"][str(player).lower()] = spiel["playerstats"][str(player).lower()] + 1
        f.seek(0)
        json.dump(spiel, f, indent=4)

        #player = input("Wähle Stein, Papier, Schere, Echse, Spock ")

        #count[player] +=1
        print(" ")
        print("Computer wählt " + str(comp))

        #compst = 0
       #playerst= 0
        #draw = 0

        if (player == "Stein" and comp == "Schere") or \
           (player == "Stein" and comp == "Echse") or \
           (player == "Papier" and comp == "Stein") or \
           (player == "Schere" and comp == "Papier") or \
           (player == "Schere" and comp == "Echse")  or \
           (player == 'Spock' and comp == "Stein") or \
           (player == "Echse" and comp == "Papier") or \
           (player == "Echse" and comp == 'Spock') or \
           (player == "Papier" and comp == "Spock") or \
           (player == 'Spock' and comp == "Schere"):
            print(" ")
            print("Gewonnen! ")
            print(" ")
            #playerst += 1
            spiel["playerwins"] = spiel["playerwins"] +1
            f.seek(0)
            json.dump(spiel, f, indent=4)
    
        elif (player == "Stein" and comp == "Papier") or \
             (player == "Stein" and comp == 'Spock') or \
             (player == "Schere" and comp == 'Stein') or \
             (player == "Papier" and comp == "Schere") or \
             (player == "Papier" and comp == "Echse") or \
             (player == "Schere" and comp == 'Spock') or \
             (player == 'Spock' and comp == "Papier") or \
             (player == 'Spock' and comp == "Echse") or \
             (player == "Echse" and comp == "Stein") or \
             (player == "Echse" and comp == "Schere"):
            print(" ")
            print("Verloren :((( ")
            print(" ")
            #compst += 1
            spiel["computerwins"] = spiel["computerwins"] +1
            f.seek(0)
            json.dump(spiel, f, indent=4)

        else:
            print(" ")
            print("Unentschieden ")
            print(" ")
            #draw += 1
            spiel["draw"] = spiel["draw"] +1
            f.seek(0)
            json.dump(spiel, f, indent=4)

    
def HardGame():
 with open('mydata.json') as f:
    events = json.load(f)
    a = events["playerstats"]
    max_keys = [key for key, value in a.items() if value == max(a.values())]

    if max_keys == ['stein']:
        b = "Papier"
    elif max_keys == ['schere']:
        b = "Stein"
    elif max_keys == ['papier']:
        b = "Schere"
    elif max_keys == ['echse']:
        b = "Schere"
    else:
        b = "Papier"
    
   
    Game(player = input("Wähle Stein, Papier, Schere, Echse, Spock "), comp = b)



    
if __name__ == '__main__':

    while True:
        print("1) Game")
        print("2) Analyse")
        print("3) Upload")
        print(" ")
  
  
        choice = input("Wähle: ")
  
        choice = choice.strip()
   
        if (choice == "1"):
            print(" ")
            l = ["Stein", "Papier", "Schere", "Echse", "Spock"]
            print("1) Normal")
            print("2) Hard")

  
  
            choice1 = input("Wähle: ")
  
            choice1 = choice1.strip()
            
            if (choice1 == "1"):

                Game(player = input("Wähle Stein, Papier, Schere, Echse, Spock "), comp = l[randint(0,4)])
            if (choice1 == "2"):
                HardGame()

        elif (choice == "2"):
            Analyse()
        elif (choice == "3"):
            print("hochgeladen")
            requests.get('http://127.0.0.1:5000/')
            
       
        else:
          print("Falsche Eingabe!")


    
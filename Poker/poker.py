import random

def card():
    suit = 0
    x = 0
    x = random.randint(1,13)
    suit = random.randint(0,3)
    if(x == 11):
      x = 'Jack'
    elif(x == 12):
      x = 'Queen'
    elif(x == 13):
      x = 'King'
    elif(x == 1):
      x = 'Ace'
    if(suit == 0):
      suit = 'Clubs'
    elif(suit == 1):
      suit = 'Spades'
    elif(suit == 2):
      suit = 'Hearts'
    else:
      suit = 'Diamonds'
    card = ((x,suit))
    return card


def deck_table():
  cards = []
  x = 5
  for i in range(0,x):
    v = card()
    if(v not in cards):
      cards.append(card())
    else:
      x +=1
  return cards


if __name__ == '__main__':
    print(deck_table())
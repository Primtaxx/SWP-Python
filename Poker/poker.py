from collections import defaultdict
import itertools
from operator import truediv
import random

def card():
    suit = 0
    x = 0
    x = random.randint(1,13)
    suit = random.randint(0,3)
    
    if(suit == 0):
      suit = 'C'
    elif(suit == 1):
      suit = 'S'
    elif(suit == 2):
      suit = 'H'
    else:
      suit = 'D'
    #card = str(x) + suit
    card = ((x,suit))
    return card

def deck_table2(x):
  cards = []
  while len(cards) < x:
    v = card()
    if(v not in cards):
      cards.append(card())
  return cards

hand = deck_table2(5)
hand2 = [(14, 'H'), (13, 'H'), (12, 'H'), (11, 'H'), (10, 'H')]


def one_pair(hand):
  values = sorted([c[0] for c in hand])
  count = defaultdict(int)
  for v in values:
        count[v]+=1
  if 2 in count.values():
        return True
  else:
        return False
  
 
def two_pair(hand):
  values = sorted([c[0] for c in hand])
  for v, group in itertools.groupby(values):
    count = sum(1 for _ in group)
    if count == 2: return True
    else:
      return False
  

def three_of_a_kind(hand):
  values = sorted([c[0] for c in hand])
  for v, group in itertools.groupby(values):
    count = sum(1 for _ in group)
    if count == 3: return True
    else:
      return False

def straight(hand):
  values = sorted([c[0] for c in hand], reverse=True)
  straight = (values == list(range(values[0], values[0]-5, -1))
                or values == [14, 5, 4, 3, 2])
  if straight:
    return True
  else: 
    return False


def flush(hand):
  suits = [c[1] for c in hand]
  flush = all(s == suits[0] for s in suits)
  return flush

def full_house(hand):
  if three_of_a_kind(hand) and one_pair(hand):
    return True
  else:
    return False


def four_of_a_Kind(hand):
  values = sorted([c[0] for c in hand])
  for v, group in itertools.groupby(values):
    count = sum(1 for _ in group)
    if count == 4: return True
    else:
      return False

def straight_flush(hand):
  if straight(hand) and flush(hand): 
    return True
  else:
    return False

def royal_flush(hand):
  values = sorted([c[0] for c in hand])
  suits = [c[1] for c in hand]
  if values == [10, 11, 12, 13, 14] and all(s == suits[0] for s in suits):
    return True
  else:
    return False
  pass



royalflush = 0
straightflush = 0
fourofakind = 0
fullhouse = 0
flusha = 0
straighta = 0
threeofakind = 0
twopair = 0
onepair1 = 0
highcard = 0

def statistics(hand,cards,anz):
  royalflush = 0
  straightflush = 0
  fourofakind = 0
  fullhouse = 0
  flusha = 0
  straighta = 0
  threeofakind = 0
  twopair = 0
  onepair = 0
  highcard = 0
  for i in range(anz):
        hand = deck_table2(cards)
        if royal_flush(hand):
          royalflush += 1
        elif straight_flush(hand):
          straightflush += 1  
        elif four_of_a_Kind(hand):
          fourofakind += 1
        elif full_house(hand):
          fullhouse += 1
        elif flush(hand):
          flusha += 1
        elif straight(hand):
          straighta += 1
        elif three_of_a_kind(hand):
          threeofakind += 1
        elif two_pair(hand):
          twopair += 1
        elif one_pair(hand):
          onepair += 1
        else:
          highcard += 1

        
    
    

  print("Number of high card hands is: ", highcard)
  print("% of hands: ", 100.0 * highcard / anz )

  print("Number of one pair hands is: ", onepair)
  print("% of hands: ", 100.0 * onepair / anz)

  print("Number of two pair hands is: ", twopair)
  print("% of hands: ", 100.0 * twopair / anz)

  print("Number of three of a kind hand is: ", threeofakind)
  print("% of hands: ", 100.0 * threeofakind / anz)

  print("Number of straights hand is: ", straighta)
  print("% of hands: ", 100.0 * straighta / anz)

  print("Number of flush hand is: ", flusha)
  print("% of hands: ", 100.0 * flusha / anz)

  print("Number of fullhouse hand is: ", fullhouse)
  print("% of hands: ", 100.0 * fullhouse / anz)

  print("Number of four of a kind hand is: ", fourofakind)
  print("% of hands: ", 100.0 * straightflush / anz)

  print("Number of straight flush hand is: ", straightflush)
  print("% of hands: ", 100.0 * straightflush / anz)

  print("Number of royal flush hand is: ", royalflush)
  print("% of hands: ", 100.0 * royalflush / anz)




if __name__ == '__main__':
    #print(royal_flush(hand2))
    #print(one_pair(hand))
    #print(two_pair(hand))
    #print(three_of_a_kind(hand))
    #print(four_of_a_Kind(hand))
    #print(straight(hand2))
    #print(straight_flush(hand))
    #print(flush(hand))
    #print(full_house(hand))
    #print(eval_hand(hand2))
    statistics(hand,7,10000)
    
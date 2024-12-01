text="""AAAQA 769
JJJJJ 638""".splitlines()

with open('data/data-day7.txt', 'r') as f:
    text = f.readlines()

from collections import Counter
from operator import itemgetter

d = {str(i):i for i in range(2, 10)}
d['T'] = 10
d['J'] = 0
d['Q'] = 12
d['K'] = 13
d['A'] = 14

class Hand:
    def __init__(self, cards) -> None:
        cards = map(lambda x: d[x], list(cards))
        self.hand = list(cards)
        c = Counter(self.hand)
        jokers = 0
        if 0 in c:
            jokers = c[0]
            del c[0]
        cards = list(c.items())
        self.cards = sorted(cards, key=itemgetter(1, 0), reverse=True)
        if self.cards:
            self.cards[0] = (self.cards[0][0], self.cards[0][1] + jokers)
        else:
            self.cards = [(14, 5)]
        

    def __lt__(self, other: 'Hand'):
        # check if someone has a higher max
        for i in range(len(self.cards)):
           if self.cards[i][1] < other.cards[i][1]:
               return True
           elif self.cards[i][1] > other.cards[i][1]:
               return False
        
        for i in range(len(self.hand)):
            if self.hand[i] != other.hand[i]:
                return self.hand[i] < other.hand[i]
            
        return False

hands = []
for line in text:
    hands.append(line.split(" "))

hands.sort(key=lambda x: Hand(x[0]))

print(hands[-10:])
sol = 0
for i, (_, bid) in enumerate(hands):
    sol += (i+1) * int(bid)

print(sol)

            
                
        
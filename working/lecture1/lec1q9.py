'''
Q9: Poker odds

Use the deck of cards class from the notebook we worked through class 
to write a _Monte Carlo_ code that plays a lot of hands of straight poker 
(like 100,000). 
Count how many of these hands has a particular poker hand (like 3-of-a-kind).  
The ratio of # of hands with 3-of-a-kind to total hands is 
an approximation to the odds of getting a 3-of-a-kind in poker.

### Bonus: 
Just to practice modules, write that into a `.py` file to allow you 
to import and reuse them here.
'''
import random

class Card:
    
    def __init__(self, suit=1, rank=2):
        if suit < 1 or suit > 4:
            print("invalid suit, setting to 1")
            suit = 1
            
        self.suit = suit
        self.rank = rank
        
    def value(self):
        """ we want things order primarily by rank then suit """
        return self.suit + (self.rank-1)*14
    
    # we include this to allow for comparisons with < and > between cards 
    def __lt__(self, other):
        return self.value() < other.value()

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        suits = [u"\u2660",  # spade
                 u"\u2665",  # heart
                 u"\u2666",  # diamond
                 u"\u2663"]  # club
        
        r = str(self.rank)
        if self.rank == 11:
            r = "J"
        elif self.rank == 12:
            r = "Q"
        elif self.rank == 13:
            r = "K"
        elif self.rank == 14:
            r = "A"
                
        return r +':'+suits[self.suit-1]

class Deck:
    """ the deck is a collection of cards """

    def __init__(self):

        self.nsuits = 4
        self.nranks = 13
        self.minrank = 2
        self.maxrank = self.minrank + self.nranks - 1

        self.cards = []

        for rank in range(self.minrank,self.maxrank+1):
            for suit in range(1, self.nsuits+1):
                self.cards.append(Card(rank=rank, suit=suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def get_cards(self, num=1):
        hand = []
        for n in range(num):
            hand.append(self.cards.pop())

        return hand
    
    def __str__(self):
        string = ""
        for c in self.cards:
            string += str(c) + " "
        return string
    

total = 0
N = 10000
for _ in range(N):
    mydeck = Deck()
    mydeck.shuffle()
    
    for _ in range(10):
        hand = sorted(mydeck.get_cards(5))
        diffs = []
        for i in range(3):
            diff = hand[i+2].value() - hand[i].value()
            diffs.append(1 if diff < 4 else 0)
        if sum(diffs) == 1:
            total += 1
print(f'fraction of hands with a three-of-a-kind: {(total / N * 10)/100:.3f} %')

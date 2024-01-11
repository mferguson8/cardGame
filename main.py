import random

def createDeck(numDecks):
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    fullDeck = deck * numDecks
    return fullDeck

def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 1000
        
class Dealer:
    def __init__(self, name):
        self.name = name
        self.hand = []

def dealCards():
    fullDeck = createDeck(2)
    players = [Player('Player')]
    dealer = Dealer('Dealer')
    
    for _ in range(4):
        for player in players:
            player.hand.append(fullDeck.pop(0))
        dealer.hand.append(fullDeck.pop(0))
        
        
def main():
    fullDeck = createDeck(1)
    shuffleDeck(fullDeck)
    print(fullDeck);
    
main()

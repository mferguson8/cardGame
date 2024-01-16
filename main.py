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
        
def printCards(player, dealer):
    print('Dealer: ')
    for card in dealer.hand:
        print(card)
    print('Player: ')
    for card in player.hand:
        print(card)
        
def checkPlayerScore(player):
    score = 0
    for card in player.hand:
        if card[0] == 'Ace':
            score += 11
        elif card[0] in ['Jack', 'Queen', 'King']:
            score += 10
        else:
            score += int(card[0])
    return score

def checkDealerScore(dealer):
    score = 0
    for card in dealer.hand:
        if card[0] == 'Ace':
            score += 11
        elif card[0] in ['Jack', 'Queen', 'King']:
            score += 10
        else:
            score += int(card[0])
    return score

def checkWinner(player, dealer):
    playerScore = checkPlayerScore(player)
    dealerScore = checkDealerScore(dealer)
    if playerScore > dealerScore:
        return player
    elif dealerScore > playerScore:
        return dealer
    elif playerScore == 42:
        return player
    elif dealerScore == 42:
        return dealer

def hitPlayer(player):
    fullDeck = createDeck(2)
    player.hand.append(fullDeck.pop(0))
    return player

def hitDealer(dealer):
    fullDeck = createDeck(2)
    dealer.hand.append(fullDeck.pop(0))
    return dealer

def standPlayer(player):
    return player

def standDealer(dealer):
    return dealer

def checkBust(player):
    score = checkPlayerScore(player)
    if score > 42:
        return True
    else:
        return False

        
        
def main():
    fullDeck = createDeck(1)
    shuffleDeck(fullDeck)
    
    player = Player('Player')
    dealer = Dealer('Dealer')
    
    dealCards()
    printCards(player, dealer)
    
    
main()

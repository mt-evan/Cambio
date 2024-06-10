import random

class Player:
    
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        numCards = 4

    def printHand(self):
        print(self.name + "'s hand:")
        for card in self.hand:
            print(card)
        


# deck of cards
def makeDeck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Ace', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    standardDeck = []

    # iterate through ranks and suits to create cards
    for suit in suits:
        for rank in ranks:
            card = rank + ' of ' + suit
            standardDeck.append(card)
    standardDeck.append("Black Joker")
    standardDeck.append("Red Joker")

    return standardDeck





def main():
    print("Welcome to Cambio")
    
    deck = makeDeck()
    
    # shuffle deck
    random.shuffle(deck)

    playerHand = []
    for _ in range(4):
        playerHand.append(deck.pop())

    name = input("Player 1 name: ")
    player1 = Player(name, playerHand)

    playerHand = []
    for _ in range(4):
        playerHand.append(deck.pop())

    name = input("Player 2 name: ")
    player2 = Player(name, playerHand)

    players = [player1, player2]
    
    

    # show each player their two cards out of four
    for player in players:
        print()
        player.printHand()



    print()

    # now the game actually begins, use a while loop
        




main()
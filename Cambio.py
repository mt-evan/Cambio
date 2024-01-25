import random

class Player:
    def __init__(self, name):
        self.name = name
       # hand = getHand()


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
  #  player1 = Player(input("Player 1's name: "))
  #  player2 = Player(input("Player 2's name: "))
    deck = makeDeck()
    
    # shuffle deck
    random.shuffle(deck)
    
    player1Hand = []
    player2Hand = []

    for _ in range(4):
        player1Hand.append(deck.pop())
        player2Hand.append(deck.pop())

    # show each player their two cards out of four
    print("Player 1's hand: ")
    for i in range(4):
        if i < 2: 
            print(player1Hand[i] + ", ")
        else:
            print("? ")
    print()
    print("Player 2's hand: ")
    for i in range(4):
        if i < 2: 
            print(player2Hand[i] + ", ")
        else:
            print("? ")
    print()

    # now the game actually begins, use a while loop
        




main()
import random

class Player:
    
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.numCards = len(hand)

    def printHand(self):
        print(self.name + "'s hand:")
        for card in self.hand:
            print(card)

    def replaceCard(self, i, newCard):
        discardCard = self.hand[i]
        self.hand[i] = newCard
        return discardCard

    
        


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

def drawCard(player, otherPlayer):
    card = deck.pop()
    print(card)
    choice = input("1: Discard\n2: Replace\n")
    if choice == '1':
        discardPile.append(card)
    else:
        print("Choose a card to replace")
        for i in range(player.numCards):
            print(i+1)
        choice = int(input())-1
        discardCard = player.replaceCard(choice, card)
        discardPile.append(discardCard)
        print("Card discarded is a " + discardCard)

# list of options a player has in a turn
def playerTurn(player, otherPlayer):
    print(player.name + "'s turn:")
    choice = input("1: Draw a card\n2: Call Cambio\n3: Stack\n")
    if choice == '1':
        drawCard(player, otherPlayer)
    elif choice == '2':
        callCambio(player, otherPlayer)



def main():
    print("Welcome to Cambio")
    
    global deck
    deck = makeDeck()
    global discardPile
    discardPile = []
    
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
    # with two players, a fullTurn is equal to two playerTurns
    playerTurns = 0
    while True:
        playerTurn(players[playerTurns % 2], players[playerTurns+1 % 2])
        playerTurns += 1
        break



main()

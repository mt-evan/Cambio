import random

cambioCalled = False

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def printHand(self):
        print(self.name + "'s hand:")
        for card in self.hand:
            print(card)
        print()

    def replaceCard(self, i, newCard):
        discardCard = self.hand[i]
        self.hand[i] = newCard
        return discardCard

    def printScore(self):
        score = 0
        for card in self.hand:
            if 'Joker' in card:
                continue  # Jokers have 0 points, so no need to add anything
            rank, suit = card.split()[0], card.split()[-1]
            if rank.isdigit():
                score += int(rank)
            elif rank == 'Ace':
                score += 1
            elif rank == 'Jack':
                score += 11
            elif rank == 'Queen':
                score += 12
            elif rank == 'King':
                if suit in ['Hearts', 'Diamonds']:
                    score += -1  # Red Kings
                else:
                    score += 13  # Black Kings
        print(f"{self.name}'s score: {score}")
        return score

    def stackOwnCard(self, i):
        topCard = discardPile[-1]
        def get_rank(card):
            return card.split(' of ')[0]

        topRank = get_rank(topCard)
        handCardRank = get_rank(self.hand[i])

        if handCardRank != topRank:
            print(f"Incorrect stack, {self.name} draws an extra card")
            self.hand.append(deck.pop())
        else:
            print(f"{self.name} correctly stacked a " + topCard)
            discardPile.append(self.hand.pop(i))
    
    def stackOpponentCard(self, i, opponent):
        topCard = discardPile[-1]
        def get_rank(card):
            return card.split(' of ')[0]

        topRank = get_rank(topCard)
        handCardRank = get_rank(opponent.hand[i])

        if handCardRank != topRank:
            print(f"Incorrect stack, {self.name} draws an extra card")
            self.hand.append(deck.pop())
        else:
            print(f"{self.name} correctly stacked a " + topCard + f" from {opponent.name}")
            discardPile.append(opponent.hand[i])
            print("Choose a card to give")
            for i in self.numCards:
                print(i)
            choice = int(input())-1
            opponent.hand[i] = self.hand.pop(choice)

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
    checkDeck()
    print(card)
    choice = input("1: Discard\n2: Replace\n")
    if choice == '1':
        discardPile.append(card)
        isSpecialCard(card, player, otherPlayer)
    else:
        print("Choose a card to replace")
        for i in range(len(player.hand)):
            print(i+1)
        choice = int(input())-1
        discardCard = player.replaceCard(choice, card)
        discardPile.append(discardCard)
        print("Card discarded is a " + discardCard)

def isSpecialCard(card, player, otherPlayer):
    sevenOrEight = ['7', '8']
    nineOrTen = ['9', '10']
    jackOrQueen = ['Jack', 'Queen']
    blackKing = ['King of Clubs', 'King of Spades']
    for rank in sevenOrEight:
        if rank in card:
            viewCard(player)
    for rank in nineOrTen:
        if rank in card:
            viewCard(otherPlayer)
    for rank in jackOrQueen:
        if rank in card:
            blindSwap(player, otherPlayer)
    for rank in blackKing:
        if rank in card:
            kingSwap(player, otherPlayer)
    
def viewCard(player):
    print(f"Select card to view from {player.name}")
    for i in range(len(player.hand)):
        print(i+1)
    choice = int(input())-1
    print(player.hand[choice])

def viewCard(player):
    print(f"Select card to view from {player.name}")
    for i in range(len(player.hand)):
        print(i+1)
    choice = int(input())-1
    print(player.hand[choice])
    return choice

def blindSwap(player, otherPlayer):
    choice = input("Blind swap?\n1: Yes\n2: No")
    if choice == '1':
        print("List of your cards:")
        for i in range(len(player.hand)):
            print(i+1)
        playerCard = int(input("Card: "))-1
        print("List of opponent's cards:")
        for i in range(len(otherPlayer.hand)):
            print(i+1)
        otherPlayerCard = int(input("Card: "))-1

        temp = player.hand[playerCard]
        player.hand[playerCard] = otherPlayer.hand[otherPlayerCard]
        otherPlayer.hand[otherPlayerCard] = temp
        
def kingSwap(player, otherPlayer):
    playerCard = viewCard(player)
    otherPlayerCard = viewCard(otherPlayer)
    choice = input("Swap?\n1: Yes\n2: No")
    if choice == '1':
        temp = player.hand[playerCard]
        player.hand[playerCard] = otherPlayer.hand[otherPlayerCard]
        otherPlayer.hand[otherPlayerCard] = temp

def stack(player, otherPlayer):
    choice = input(f"1: Stack from your deck\n2: Stack from {otherPlayer.name}'s deck")
    if choice == '1':
        print("Choose a card to stack")
        for i in range(len(player.hand)):
            print(i+1)
        choice = int(input())-1
        player.stackOwnCard(choice)
    else:
        print("Choose a card to stack")
        for i in range(len(otherPlayer.hand)):
            print(i+1)
        choice = int(input())-1
        player.stackOpponentCard(choice, otherPlayer)

def callCambio(player, otherPlayer):
    global cambioCalled
    cambioCalled = True
    print(player.name + " has called Cambio")
    print(otherPlayer.name + "'s final turn")
    # otherPlayer gets one last turn
    drawCard(otherPlayer, player)
    player.printHand
    otherPlayer.printHand
    playerScore = player.printScore()
    otherPlayerScore = otherPlayer.printScore()
    if playerScore < otherPlayerScore:
        print(player.name + " wins the game")
    elif playerScore > otherPlayerScore:
        print(otherPlayer.name + " wins the game")
    else:
        print("Game is a draw")


# list of options a player has in a turn
def playerTurn(player, otherPlayer):
    print()
    checkDeck()
    print(player.name + "'s turn:")
    player.printHand()
    otherPlayer.printHand()
    choice = input("1: Don't stack\n2: Stack\n")
    if choice == '2':
        stack(player, otherPlayer)
        checkDeck()
    choice = input("1: Draw a card\n2: Call Cambio\n")
    if choice == '1':
        checkDeck()
        drawCard(player, otherPlayer)
    else:
        checkDeck()
        callCambio(player, otherPlayer)
    choice = input("1: Don't stack\n2: Stack\n")
    if choice == '2':
        stack(player, otherPlayer)
        checkDeck()

        
def checkDeck():
    global deck, discardPile
    if len(deck) == 0:
        deck = discardPile
        random.shuffle(deck)
        discardPile.clear()



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
    while not cambioCalled:
        checkDeck()
        playerTurn(players[playerTurns % 2], players[(playerTurns+1) % 2])
        playerTurns += 1



main()

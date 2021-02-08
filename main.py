import random as rand
from Card import Card
from Player import Player
from Dealer import Dealer

#DEFAULT CARD SUITS, VALUES (used in makeDeck())
suits = [
    "spades",
    "hearts",
    "clubs",
    "diamonds"
]
values = [
    (1,11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10
]

#MAKES A GIVEN AMOUNT OF DECKS AND RETURNS A LIST OF CARD OBJECTS
def makeDeck(num):
    d = list()
    for suit in suits:
        for value in range(1, 14):
            if value == 1:
                d.append(Card([(1, 11), suit, "A", True]))
            elif value == 11:
                d.append(Card([10, suit, "J", True]))
            elif value == 12:
                d.append(Card([10, suit, "Q", True]))
            elif value == 13:
                d.append(Card([10, suit, "K", True]))
            else:
                d.append(Card([value, suit, str(value), True]))
    return d*num

#DEALS CARDS INTO ALL HANDS OF PLAYER OBJECTS IN LIST
def deal(list):
    for player in list:
        player.setHand(deck)
    #print("dealt")



#THE DEALER IS PLAYER 0
dealer = Player(0)
playerList = [dealer]

#MAKES DECK OF CERTAIN SIZE
deck = makeDeck(1)

#DEFAULT PLAYER VALUE (0 By Default)
playerNum = 1

#USER INPUT FOR # OF PLAYERS
while playerNum == 0:
    playerNum = int(input("How many players? (1 or more):"))
    if playerNum == 0:
        print("Please enter a number >= 1.")

#ADDS PLAYER OBJECTS TO PLAYERLIST LIST
for i in range(1, playerNum+1):
    playerList.append(Player(i))


#SHUFFLES THE DECK
rand.shuffle(deck)

# deck.append(Card([(1, 11), "spades", "A"]))
# deck.append(Card([(1, 11), "spades", "A"]))
# deck.append(Card([(1, 11), "spades", "A"]))
# deck.append(Card([(1, 11), "spades", "A"]))
#deck.append(Card([(1, 11), "spades", "A"]))

#PUTS CARDS IN EVERY PLAYER OBJECT'S HAND
deal(playerList)



#print(len(deck))

# playerList[1].hand[1].printUI()

#playerList[1].splitHand(deck)

# playerList[1].hand2[0].printUI()

#print(len(deck))

# for x in playerList[1]:
#     x.printHand()


#GAME LOOP
userIn = ""
while userIn != "stop":
    playerList[0].printHand()
    playerList[1].printHand()
    userIn = input("1) Hit\n2) Split")


#print(playerList[1].handTotal())

#playerList[1].hit(deck)
#playerList[1].hit(playerList[1].hands[0], deck)

#playerList[1].printHand()

#print(len(deck))

#print(playerList[1].handTotal())
#print(deck[4].cardML)
#print(playerList[0].isBust())
    


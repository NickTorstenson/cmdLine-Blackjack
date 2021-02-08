from Card import Card

class Player:

    #DEFAULT MONEY IN PLAYER OBJECT
    balance = 100

    #INITIALIZATION
    def __init__(self, place):
        #self.balance = balance
        self.place = place
        self.bet = 0
        self.hands = [[],[]]
        self.isDealer = (place == 0)
        self.canSplit = False
        self.isSplit = False

    #TAKES 2 CARDS OUT OF DECK AND PUTS INTO HAND
    def setHand(self, deck):
        self.hands[0] = [deck.pop(), deck.pop()]
        if self.isDealer:
            self.hands[0][0].updateCard(False)


    #CLEARS THE PLAYER HAND LIST
    def clearHand(self):
        for hand in self.hands:
            hand.clear()
        self.isSplit = False

    #TAKES A CARD OUT OF HAND AND PUTS INTO HAND2, THEN PUTS ONE MORE CARD IN EACH
    def splitHand(self, deck):
        if not(self.canSplit):
            print("Cannot Split")
            return
        self.hands[1].append(self.hands[0].pop())
        self.hit(self.hands[0], deck)
        self.hit(self.hands[1], deck)
        self.isSplit = True
    
    #TAKES A CARD OUT OF DECK AND PUTS INTO HAND(Needs to be specified)
    def hit(self, deck, hnd=0):
        #DECIDES WHICH HAND TO HIT BASED ON GIVEN HAND
        if hnd == 0:
            self.hands[0].append(deck.pop())
        else:
            self.hands[1].append(deck.pop())
        
    #SETS THE BET TO BE USED IN CURRENT ROUND
    def setBet(self, b):
        self.bet = b

    #SUBRACTS BET FROM BALANCE
    def subBal(self):
        self.balance -= self.bet

    def addBal(self, num):
        self.balance += num

    #RETURNS THE TOTAL OF THE HAND GIVEN
    def handTotal(self, hnd=0):
        total = 0
        total2 = 0
        hasAce = False
        #CHECKS IF BOTH CARDS ARE ACES
        if self.hands[hnd][-1].name == self.hands[hnd][-2].name == "A":
            return (2, 12)
        for card in self.hands[hnd]: 
            if card.name == "A":
                print("Ace")
                hasAce = True
                total += 1
                total2 += 11
                continue
            total += card.value
            total2 += card.value
        
        if hasAce and total2 < 21:
            return (total, total2)
        elif total2 == 21:
            return 21
        else:
            return total

    #WHEN CALLED RETURNS WHETHER PLAYER HAS BUSTED
    def isBust(self, hnd=0):

        return self.hands[hnd].handTotal(hnd)

    #PRINTS ALL HANDS THAT THE PLAYER HAS
    def printHand(self):
        te = ""
        tl = ""
        ml = ""
        bl = ""

        if not self.isSplit:
            for c in self.hands[0]:
                te+=c.cardTE
                tl+=c.cardTL
                ml+=c.cardML
                bl+=c.cardBL
        else:
            for c in self.hands[0]:
                te+=c.cardTE
                tl+=c.cardTL
                ml+=c.cardML
                bl+=c.cardBL
            te += "  "
            tl += "  "
            ml += "  "
            bl += "  "
            for c in self.hands[1]:
                te+=c.cardTE
                tl+=c.cardTL
                ml+=c.cardML
                bl+=c.cardBL
        print(te + "\n" + tl + "\n" + ml + "\n" + bl)


    
        



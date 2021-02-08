

class Card:
    def __init__(self, card, shown = True):
        self.card = card
        self.value = card[0]
        self.suit = card[1]
        self.name = card[2]
        self.shown = shown
        self.cardTE = " ___ "
        self.cardTL = ""
        self.cardML = ""
        self.cardBL = ""
        self.suitSymbol = ""

        #MAKES THE DIFFERENT LINES OF THE CARD GRAPHIC
        # -___-    
        # |10-|        "-" are spaces
        # |-♠-|
        # |_10|
        if self.suit == "spades":
            self.suitSymbol = "♠"
        if self.suit == "hearts":
            self.suitSymbol = "♥"
        if self.suit == "clubs":
            self.suitSymbol = "♣"
        if self.suit == "diamonds":
            self.suitSymbol = "♦"

        if len(self.name) == 1:
            self.cardTL = "|" + self.name + "  |"
            self.cardBL = "|__" + self.name + "|"
        else:
            self.cardTL = "|" + self.name + " |"
            self.cardBL = "|_" + self.name + "|"
            
        self.cardML = "| " + self.suitSymbol + " |"

    def updateCard(self, showing):
        if showing:
            if self.suit == "spades":
                self.suitSymbol = "♠"
            if self.suit == "hearts":
                self.suitSymbol = "♥"
            if self.suit == "clubs":
                self.suitSymbol = "♣"
            if self.suit == "diamonds":
                self.suitSymbol = "♦"

            if len(self.name) == 1:
                self.cardTL = "|" + self.name + "  |"
                self.cardBL = "|__" + self.name + "|"
            else:
                self.cardTL = "|" + self.name + " |"
                self.cardBL = "|_" + self.name + "|"
            
            self.cardML = "| " + self.suitSymbol + " |"
        else:
            if self.suit == "spades":
                self.suitSymbol = "♠"
            if self.suit == "hearts":
                self.suitSymbol = "♥"
            if self.suit == "clubs":
                self.suitSymbol = "♣"
            if self.suit == "diamonds":
                self.suitSymbol = "♦"

            self.cardTL = "|░░░|"
            self.cardML = "|▒▒▒|"
            self.cardBL = "|▓▓▓|"
                
            

    #PRINTS SINGLE CARD GRAPHIC
    def printUI(self):
        print(self.cardTE + "\n" + self.cardTL + "\n" + self.cardML + "\n" + self.cardBL)




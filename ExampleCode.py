# Blackjack by @TokyoEdTech Version 0.9
# YouTube Channel: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg

import random
import os
import time

os.system("clear")

class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    def print_card(self):
        print("+---+")
        print("|{}  |".format(self.suit))
        print("| {} |".format(self.name))
        print("|  {}|".format(self.suit))
        print("+---+")

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards.clear()
        values = [11, 10, 10, 10, 10, 9, 8, 7 ,6, 5, 4, 3, 2]
        names = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        suits = ["♣", "♠", "♦", "♥"]
           
        for i in range(len(values)):
            for suit in suits:
                self.cards.append(Card(names[i], suit, values[i]))

        self.shuffle()

    def print_deck(self):
        for card in self.cards:
            card.print_card()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        card = self.cards.pop()
        return card


class Player():
    def __init__(self):
        self.hand = []
        self.chips = 100
        self.choice = ""

    def print_hand(self):
        number_of_cards = len(self.hand)
        
        # Top row
        for i in range(number_of_cards):
            print("+---+ ", end="")

        print()
        for i in range(number_of_cards):
            card = self.hand[i]
            print("|{}  | ".format(card.suit), end="")

        print()
        for i in range(number_of_cards):
            card = self.hand[i]
            print("| {} | ".format(card.name), end="")

        print()
        for i in range(number_of_cards):
            card = self.hand[i]
            print("|  {}| ".format(card.suit), end="")

        print()    
        for i in range(number_of_cards):
            print("+---+ ", end="")


    def calculate_hand(self):
        value = 0
        for card in self.hand:
            value += card.value

        # Check for aces
        if value > 21:
            for card in self.hand:
                if card.value == 11:
                    value -= 10
                if value <= 21:
                    break

        return value

def print_header():
    print("*********************************************")
    print("***Welcome to TokyoEdTech's Blackjack Game***")
    print("*********************************************")

# Create the players
dealer = Player()
player1 = Player()

# Create the deck
deck = Deck()

def reset_game():
        # Reset
        deck.reset()

        player1.hand.clear()
        player1.choice = ""

        dealer.hand.clear()
        dealer.choice = ""

        print_game()

        # Deal

        player1.hand.append(deck.draw())
        print_game()

        dealer.hand.append(deck.draw())
        print_game()

        player1.hand.append(deck.draw())
        print_game()


def print_game():
    time.sleep(0.5)
    os.system("clear")
    print_header()

    print("\n---DEALER---")
    dealer.print_hand()
    print("\nChips: {}".format(dealer.chips))
    if(dealer.choice == "H" or dealer.choice == "S"):
        print("Hand value: {}".format(dealer.calculate_hand()))
    else:
        print()
    
    print("\n---PLAYER 1---")
    player1.print_hand()
    print("\nChips: {}".format(player1.chips))
    print("Hand value: {}".format(player1.calculate_hand()))
    
reset_game()

while True:

    # Player's turn

    while(player1.choice != "S"):
        print_game()

        player1.choice = input("\nWould you like to H)it or S)tay? > ").upper()

        if(player1.choice == "H"):
            player1.hand.append(deck.draw())

        print_game()

        # Check for a player bust

        if(player1.calculate_hand() > 21):
            dealer.choice = "S"
            dealer.hand.append(deck.draw())
            player1.chips -= 10
            dealer.chips += 10
            print_game()
            print("\nPLAYER 1 BUSTS")
            print("***DEALER WINS!***")
            play_again = input("Press ENTER to continue.")
            reset_game()
            continue


    # Dealer's turn
    while(dealer.choice != "S"):
        print_game()

        if(dealer.calculate_hand() < player1.calculate_hand()):
            dealer.hand.append(deck.draw())
            dealer.choice = "H"
        elif (dealer.calculate_hand() < 17):
            dealer.hand.append(deck.draw())
            dealer.choice = "H"
        else:
            dealer.choice = "S"

        print_game()

        if(dealer.calculate_hand() > 21):
            player1.chips += 10
            dealer.chips -= 10
            print_game()
            print("\nDEALER BUSTS")
            print("***PLAYER 1 WINS!***")
            play_again = input("\nPress ENTER to continue.")
            reset_game()    


    # Determine the winner
    if(player1.calculate_hand() > dealer.calculate_hand()):
        player1.chips += 10
        dealer.chips -= 10
        print_game()
        print("***PLAYER 1 WINS!***")
        play_again = input("Press ENTER to continue.")
        reset_game()    
    else:
        player1.chips -= 10
        dealer.chips += 10
        print_game()
        print("***DEALER WINS!***")
        play_again = input("Press ENTER to continue.")
        reset_game()

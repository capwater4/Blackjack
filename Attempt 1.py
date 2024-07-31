import itertools, random, time

#Draws a new card, removes old card from deck, returns card value
def cardDraw(deck):
    print("*******new card*******")
    time.sleep(2)
    card_index = random.randint(1,len(deck)-1)
    try:
        new_card = deck[card_index][0]
        print(f"New card is: {new_card}")
        deck.pop(card_index)
    except:
        print("Error in new card: " + str(card_index))
    return new_card
#Compares player value and dealer value to determine winner
def determine_winner(p_val, d_val):
    print("Determining Winner")
    time.sleep(2)
    if d_val > p_val and d_val < 21:
        print("Dealer Win")
    elif d_val == p_val:
        print("Push")
    else:
        print("Player Win")

def game():
    values = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    names = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    suits = ['Spade', 'Heart', 'Diamond', 'Club']
    num_deck = 1
    #creates the deck which has 3 values per list element, card value,card name and card suite
    #cupid shuffle
    deck = list((*a,b) for a,b in itertools.product(zip(values, names), suits)) * num_deck
    random.shuffle(deck)
    #draws the player cards and the dealer cards, removes cards from deck
    p1_index = random.randint(0,len(deck)-1)
    p1 = deck[p1_index][0]
    deck.pop(p1_index)
    p2_index = random.randint(0,len(deck)-1)
    p2 = deck[p2_index][0]
    deck.pop(p2_index)
    d1_index = random.randint(0,len(deck)-1)
    d1 = deck[d1_index][0]
    deck.pop(d1_index)
    d2_index = random.randint(0,len(deck)-1)
    d2 = deck[d2_index][0]
    deck.pop(d2_index)
    #puts player cards and dealer cards into lists
    p_cards =[p1, p2]
    d_cards = [d1, d2]
    player_value = p1 + p2
    dealer_value = d1 + d2

    while player_value <= 21: 
        print("Player Cards: " + ','.join(map(str, p_cards)) + " value: " + str(player_value))
        print("Dealer Showing: " + str(d2))
        choice = "X"
        #Check if player has blackjack
        # If player has 21 with more than 2 cards, they automatically stay
        if player_value == 21 and len(p_cards) == 1:
            print("Blackjack!")
        elif player_value == 21:
            choice = "S"
            break
        else:
            choice = input("H or S?")
        #If player hits draw new card and display
        if choice == "H":
            new_card = cardDraw(deck)
            player_value += new_card
            p_cards.append(new_card)
        elif choice == "S":
            print("Dealer Cards: "+ ','.join(map(str, d_cards)) + " value: " + str(dealer_value))
            #dealer needs to draw to 17 when player has stayed
            while dealer_value < 17:
                new_card = cardDraw(deck)
                dealer_value += new_card
                p_cards.append(new_card)
            determine_winner(player_value, dealer_value)
            break
        else:
            break
        #condition to try to catch bust, not sure if it should be here
        if player_value > 21:
            print(f"Player Value: {player_value}")
            print(f"Dealer Value: {dealer_value}")
            print("BUST")
            break

if __name__ == '__main__':
    game()

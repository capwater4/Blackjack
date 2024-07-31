import itertools, random, time

#prints the new card out to the console
def print_new_card(card):
    print("*******new card*******")
    time.sleep(1)
    print(f"New card is: {str(card[0])} of {str(card[2])}")
    time.sleep(1)

#Draws a new card, removes old card from deck, returns card value
#If drawing first few cards (post_deal), we don't need to print them out
def card_draw(deck, post_deal=None):
    try:
        card_index = random.randint(1,len(deck)-1)
        new_card = deck[card_index]
        if post_deal:
            print_new_card(new_card)
        deck.pop(card_index)
    except:
        print("Error in new card: " + str(card_index))
    return new_card

#Compares player value and dealer value to determine winner
def determine_winner(p_val, d_val):
    print("Determining Winner")
    time.sleep(2)
    if d_val > p_val and d_val <= 21:
        print("Dealer Win")
    elif d_val == p_val:
        print("Push")
    else:
        print("Player Win")

def game():
    values = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    names = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    num_deck = 1
    #creates the deck which has 3 values per list element, card value,card name and card suite
    #cupid shuffle, deck example: [(11, 'A', 'Spades'), (10, 'Q', 'Spades')] etc.
    deck = list((*a,b) for a,b in itertools.product(zip(values, names), suits)) * num_deck
    random.shuffle(deck)
    #draws the player cards and the dealer cards, removes cards from deck
    p1 = card_draw(deck)
    p2 = card_draw(deck)
    d1 = card_draw(deck)
    d2 = card_draw(deck)
    #puts player cards and dealer cards into lists
    p_cards =[p1[0], p2[0]]
    d_cards = [d1[0], d2[0]]
    player_value = p1[0] + p2[0]
    dealer_value = d1[0] + d2[0]
    while player_value <= 21: 
        time.sleep(1)
        print(f"Player Cards: {','.join(map(str, p_cards))} | Value: {str(player_value)}")
        time.sleep(1)
        print(f"Dealer Showing: {str(d2[0])} of {str(d2[2])}")
        choice = "X"
        #Check if player has blackjack
        #If player has 21 with more than 2 cards, they automatically stay
        if player_value == 21 and len(p_cards) == 1:
            print("Blackjack!")
        elif player_value == 21:
            choice = "S"
            break
        else:
            choice = input("H or S?")
        #If player hits draw new card and display
        if choice == "H":
            new_card = card_draw(deck, post_deal="Yes")
            player_value += new_card[0]
            p_cards.append(new_card[0])
        elif choice == "S":
            print(f"Dealer Cards: {','.join(map(str, d_cards))} | Value: {str(dealer_value)}")
            #dealer needs to draw to 17 when player has stayed
            while dealer_value < 17:
                new_card = card_draw(deck, post_deal="Yes")
                dealer_value += new_card[0]
                p_cards.append(new_card)
            determine_winner(player_value, dealer_value)
            break
        else:
            break
        #condition to try to catch bust, not sure if it should be here
        if player_value > 21:
            print(f"Player Value: {player_value}")
            time.sleep(1)
            print(f"Dealer Value: {dealer_value}")
            time.sleep(1)
            print("BUST")
            break

if __name__ == '__main__':
    game()

from Ascii import logo
import random

# Define the suits and ranks for a standard deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Create a deck of cards
deck = [rank + ' of ' + suit for suit in suits for rank in ranks]

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = sum(values[card.split()[0]] for card in hand)
    num_aces = sum(card.startswith('A') for card in hand)
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

# Function to deal a card from the deck
def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

# Function to display the hand
def display_hand(hand, is_dealer=False):
    if is_dealer:
        print("Dealer's hand: " + " ".join(hand))
    else:
        print("Your hand: " + " ".join(hand))

# Main game function
def play_blackjack():
    deck = [rank + ' of ' + suit for suit in suits for rank in ranks]
    random.shuffle(deck)

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    print(logo)
    print("Welcome to Blackjack!\n")

    display_hand(player_hand)
    print("Dealer's hand: " + dealer_hand[0] + " ?")

    while calculate_hand_value(player_hand) < 21:
        move = input("Would you like to (H)it or (S)tand? ").upper()
        if move == 'H':
            player_hand.append(deal_card(deck))
            display_hand(player_hand)
        elif move == 'S':
            break
        else:
            print("Invalid input. Please enter 'H' to hit or 'S' to stand.")

    player_value = calculate_hand_value(player_hand)
    if player_value > 21:
        print("You bust! Dealer wins.")
        return

    display_hand(dealer_hand, is_dealer=True)
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
        display_hand(dealer_hand, is_dealer=True)

    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21:
        print("Dealer busts! You win.")
    elif dealer_value > player_value:
        print(f"Dealer wins with {dealer_value}.")
    elif dealer_value < player_value:
        print(f"You win with {player_value}.")
    else:
        print(f"It's a tie with {player_value}.")

# Play the game
play_blackjack()

#Draft version of the program.

# from Ascii import logo
# import random
#
# def calculate_hand(hand):
#     '''Calculates the total score of the hand.'''
#     score = 0
#     for cards in hand:
#         score = score + cards
#     return score
#
# def draw_cards():
#     '''Adds an additional card to the hand.'''
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     hand = random.choice(cards)
#     return hand
#
#
# player_name = input("Enter your name to begin: \n")
# player_name = player_name.title()
#
# # play_again = True
# # players_hand = []
# # players_total = 0
# #
# # computers_hand = []
# # computers_total = 0
#
# def play_blackjack():
#     '''Starts a new game of Blackjack for the player.'''
#
#     players_hand = []
#     players_total = 0
#
#     computers_hand = []
#     computers_total = 0
#
#     print(logo)
#     computer_drawing = True
#     print(f"Hello {player_name}, and welcome to Blackjack.\n \n")
#     game_over = False
#     while not game_over:
#         players_hand.append(draw_cards())
#         players_hand.append(draw_cards())
#         players_total = calculate_hand(players_hand)
#
#         print(f"Your current hand is {players_hand}, with a total of {players_total}.\n\n")
#
#         computers_hand.append(draw_cards())
#         print(f"The dealer has {computers_hand}.\n")
#
#         more_cards = True
#         while more_cards:
#             draw = input("Draw a card? 'Y' for Yes, 'N' for No.\n")
#             draw = draw.upper()
#             if draw == "Y":
#                 players_hand.append(draw_cards())
#                 players_total = calculate_hand(players_hand)
#                 print(f"Your current hand is {players_hand}, with a total of {players_total}.\n\n")
#             elif draw == 'N':
#                 while computer_drawing:
#                     computers_total = calculate_hand(computers_hand)
#                     if players_total > computers_total:
#                         if computers_total < 21:
#                             #computers_total = calculate_hand(computers_hand)
#                             computers_hand.append(draw_cards())
#                             print(computers_hand)
#                         else:
#                             #computer_drawing = False
#                             more_cards = False
#                     computer_drawing = False
#                     more_cards = False
#
#         input("Press Enter to start a new game...\n\n\n\n\n")
#         game_over = False
#         players_hand.clear()
#         computers_hand.clear()
#
# play_blackjack()
# BlackJack Overview
# Play free online blackjack - also called '21' - the classic casino card game of luck and skill!
# Free Blackjack Game Overview
# Welcome to this online blackjack page where you can play the best free blackjack games. The benefits of playing online are that you can learn blackjack rules in no rush and there is no actual monetary loss if you lose! You can click the menu button on the top right corner to read the rules. What's best: We also automatically save your game so you can come back anytime to play blackjack online! Remember, you don't win because you are closer to the value of 21 -- you win because your combined value of the cards is greater than that of dealer.

# Blackjack Strategy
# 1. When the value of dealer's revealed card is 4,5 or 6, it may be fruitful to double your bet with an Ace and 4 in hand.

# 2. You may want to surrender if you have 16 in your hand while the dealer has a 9,10 or A.

# 3. You should always split if you have a pair of Aces.

# 4. If you get a pair of 7s, only press hit if the dealer has 8,9,10 or Ace.

# Play Blackjack for free now to test whether the strategy works!



from art import logo
print(logo)








# from art import logo
# from random import choice



# def is_bust(score):

#     return score > 21

# def hit(hand):

#     hand.append(choice(cards))


# def score(hand):
#     return sum(hand)

# def soft_ace(hand):

#     if hand[0] == 11 and hand[1] == 11:
#         replace_both = input("replace both aces? (y/n)" ).lower()
#         if replace_both == 'y':
#             hand[0] =choice(cards)
#             hand[1] =choice(cards)
#     elif hand[0] == 11:
#         replace_first = input("replace ace? (y/n)").lower()
#         if replace_first == 'y':
#             hand[0] = choice(cards)
#     elif hand[1] == 11:
#         replace_second = input("replace ace? (y/n)")
#         if replace_second == 'y':
#             hand[1] = choice(cards)

# def display_hand(hand):

#     cards =''
#     for card in hand[:-1]:
#         cards +=f"{card}, "
#     return cards + str(hand[-1])

# def build_starting_hand():

#     return [choice(cards) for _ in range(2)]

# cards = [11,2,3,4,5,6,7,8,9,10]

# while True:
#     play = input("Do you want to play Blackjack? (y/n)")
#     if play == 'n':
#         break
#     else:
#         print(logo)
#         print("Dealer always hits on 16 or less, always stands on 17 or more")
#         player_hand = build_starting_hand()
#         dealer_hand = build_starting_hand()
#         print(f"Your cards: {display_hand(player_hand)}")
#         soft_ace(player_hand)
#         print(f"Your cards: {display_hand(player_hand)}")
#         player_score = score(player_hand)
#         print(f"Your current score is: {player_score}")
#         print(f"Dealer's first card: {dealer_hand[0]}")
#         dealer_score = score(dealer_hand)
#         completing_player_hand = True
#         completing_dealers_hand = True

#         while completing_player_hand:
#             player_action = input("Do you want to [h]it or [s]tick? ").lower()
#             if player_action == 'h':
#                 hit(player_hand)
#             else:
#                 completing_player_hand = False
#             print(f"Your hand: {display_hand(player_hand)}")
#             player_score = score(player_hand)
#             print(f"Your score is {player_score}")
#             if is_bust(player_score):
#                 print("You are bust! Dealer wins!")
#                 print(f"\nDealer's hand: {display_hand(dealer_hand)}")
#                 print(f"Dealer's score is {dealer_score}")
#                 completing_player_hand = False
#                 completing_dealers_hand = False

#         determine_winner = True
#         while completing_dealers_hand:
#             print(f"Dealer's hand: {display_hand(dealer_hand)}")
#             dealer_score = score(dealer_hand)
#             print(f"Dealer's score is {dealer_score}")
#             if is_bust(dealer_score):
#                 print("Dealer is bust! You win!")
#                 completing_dealers_hand = False
#                 determine_winner = False
#             elif dealer_score < 16:
#                 hit(dealer_hand)
#             else:
#                 completing_dealers_hand = False

#             if determine_winner:
#                 if player_score > dealer_score:
#                     print("You win!")
#                 elif dealer_score > player_score:
#                     print("Dealer win!")
#                 else:
#                     print("Push.")
# print("Thank you. Goodbye!")


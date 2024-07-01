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



## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.



# import random
# from art import logo

# def cards_deck():
#   """Returns a single random card from the deck."""
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   card = random.choice(cards)
#   return card

# def score(cards):
#   """Take a list of cards and return the score calculated from the cards."""
#   score = sum(cards)

#   # Check for a blackjack (a hand with only 2 cards: an ace and a 10-value card)
#   if score == 21 and len(cards) == 2:
#       return 0 #means blackjack

#   # Adjust for aces if the score is over 21
#   if 11 in cards and score > 21:
#       cards[cards.index(11)] = 1
#       score = sum(cards)

#   return score

# def compare(user_score, computer_score):
#   #compariation If user and the computer are both over 21, user lose.
#   if user_score > 21 and computer_score > 21:
#     return "You went over. You lose 😤"

#   if user_score == computer_score:
#     return "Draw 🙃"
#   elif computer_score == 0:
#     return "Lose, opponent has Blackjack 😱"
#   elif user_score == 0:
#     return "Win with a Blackjack 😎"
#   elif user_score > 21:
#     return "You went over. You lose 😭"
#   elif computer_score > 21:
#     return "Opponent went over. You win 😁"
#   elif user_score > computer_score:
#     return "You win 😃"
#   else:
#     return "You lose 😤"

# def game_starts():
#   """Users and computers cards are randomized list."""
#   user_cards = []
#   computer_cards = []
#   game_over = False
  
#   for _ in range(2):
#     user_cards.append(cards_deck())
#     computer_cards.append(cards_deck())
    
#   while not game_over:
#     user_score = score(user_cards)
#     computer_score = score(computer_cards)
#     print(f"   Your cards: {user_cards}, current score: {user_score}")
#     print(f"   Computer's first card: {computer_cards[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#       game_over = True
#     else:
#       user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#       if user_should_deal == "y":
#         user_cards.append(cards_deck())
#       else:
#         game_over = True

#   while computer_score != 0 and computer_score < 17:
#     computer_cards.append(cards_deck())
#     computer_score = score(computer_cards)

#   print(f"   Your final hand: {user_cards}, final score: {user_score}")
#   print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#   print(compare(user_score, computer_score))

# ask_user = True
# while ask_user:
#   print(logo)
#   player = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#   if player =='y':
#     game_starts()
#   elif player == 'n':
#     print("See you next time. Good-bye..!")
#   else:
#     ask_user = True


  
import random
from art import logo

def cards_deck():
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
"Returns a single random card from the deck."

def score_calculation(cards):
    total = sum(cards)
    "Check for a blackjack (hand with only 2 cards: an ace and a 10-value card)"
    if total == 21 and len(cards) == 2:
        return 0
    "Adjust for aces if the score is over 21"
    if total > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        total = sum(cards)
    return total

def comparization(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    return "You lose 😤"

def game_starts():
    user_cards = []
    computer_cards = []
  
    for two in range(2):
       user_cards.append(cards_deck())
       computer_cards.append(cards_deck())
    # the "walrus operator" (:=) allows you to assign a value to a variable as part of an expression.
    while (user_score := score_calculation(user_cards)) != 0 and user_score <= 21:
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
      
        if input("Type 'y' to hit, type 'n' to stay: ") == 'y':
            user_cards.append(cards_deck())
        else:
            break

    while (computer_score := score_calculation(computer_cards)) < 17:
        computer_cards.append(cards_deck())
        computer_score = score_calculation(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(comparization(user_score, computer_score))

ask_user = True
while ask_user:
  print(logo)
  player = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if player =='y':
    game_starts()
  elif player == 'n':
    print("\nSee you next time. Good-bye..!")
  else:
    ask_user = True







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


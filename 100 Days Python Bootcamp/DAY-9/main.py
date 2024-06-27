# import clear
# from art import logo

# print(logo)
# bids={}
# taking_bids = True
# print("Welcome to the secret auction program.")

# while taking_bids:
#   users = input("What is your name?:")
#   bid = input("What is your Bid?:$ ")

#   bids[users] = bid
#   more_bidders = input("Are there any other bidders? Type 'y' or 'n' \n")

#   if more_bidders == 'n':
#     taking_bids = False
#   else:
#     print("\n")
# winner = next(iter(bids)) 
# for bid, bidder_value in bids.items():
#   print(f"[{bid}: {bidder_value}]")
# highest_bid = 0
# for bidder in bids:
#   bid_amount = int(bids[bidder])
#   if bid_amount > highest_bid:
#     highest_bid = bid_amount
#     winner = bidder
# print(f"The winner is {winner} with a bid of ${highest_bid}")


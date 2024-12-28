from day9_art import logo
import os #for clearing terminal
print(logo)
bidding = True
auction = {}

def addparticipant(name,bid):
    auction[name] = bid
while(bidding):
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: "))
    addparticipant(name,bid)
    decision = input("Are there any other bidders?Type 'yes' or 'no'.  ")
    os.system('clear') #for clearning terminal for linux and mac
    #for windows os.system('cls')
    if(decision == "no"):
        bidding = False

highest_bidder = ""
highest_bid = 0

for key in auction:
    if(auction[key]>highest_bid):
        highest_bid = auction[key]
        highest_bidder = key


print(f"The Highest bidder is {highest_bidder} and bid is {highest_bid}")
from day11_art import logo
import random
import os 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ace = cards[0]
king = cards[9]
queen = cards[10]
jack = cards[11]


def score(data):
    return sum(data)
def blackjack_check(data):
    if (ace and ( king or queen or jack ) in data):
        return True
def printing(data1,data2):
    print(f"Your cards are {data1} and score is {score(data1)}")
    print(f"computer cards are {data2} and score is {score(data2)}")
    

def prints(data1,data2):
    print(f"Your cars {data1} and score is {score(data1)}")
    print(f"computer first card {data2[0]}")

def checkscores(dat1,data2):
    userscore = score(user_cards)
    computerscore = score(computer_cards)
    if(userscore>21):
        print("compter won")
    elif(computerscore>21):
        print("You won")
    elif(userscore > computerscore):
        print("You won")
    elif(userscore < computerscore):
        print("computer won")
    elif(userscore == computerscore):
        print("Draw")
game = True
while(game):
    os.system('clear')
    print(logo)
    computer_cards = [random.choice(cards),random.choice(cards)]
    user_cards = [random.choice(cards),random.choice(cards)]
    if blackjack_check(computer_cards):
        print("computer won!")
    elif blackjack_check(user_cards):
        print("You won!")
    elif blackjack_check(computer_cards) and blackjack_check(user_cards) :
        print("computer won")
    prints(user_cards,computer_cards)


    if(score(user_cards)>21 and ace in user_cards):
        user_cards[user_cards.index(ace)] = 1

    while(input("if you want another card press 'y' type n to pass  ") == 'y'and score(user_cards)<21):
        user_cards.append(random.choice(cards))
        prints(user_cards,computer_cards)

    while(score(computer_cards)<17):
        computer_cards.append(random.choice(cards))

    checkscores(user_cards,computer_cards)
    printing(user_cards,computer_cards)
    if(input("if you want to play game again press 'y' to exit press 'n") == 'n'):
        game = False


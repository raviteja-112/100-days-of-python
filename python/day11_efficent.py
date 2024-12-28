
import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ace = 11

def score(data):
    return sum(data)

def blackjack_check(data):
    return ace in data and any(card in data for card in [10, 11, 12])

def print_game_state(user_cards, computer_cards, reveal_computer=False):
    print(f"Your cards are {user_cards} and score is {score(user_cards)}")
    if reveal_computer:
        print(f"Computer cards are {computer_cards} and score is {score(computer_cards)}")
    else:
        print(f"Computer first card: {computer_cards[0]}")

def check_scores(user_cards, computer_cards):
    user_score = score(user_cards)
    computer_score = score(computer_cards)
    
    if user_score > 21:
        return "Computer won"
    elif computer_score > 21:
        return "You won"
    elif user_score > computer_score:
        return "You won"
    elif user_score < computer_score:
        return "Computer won"
    else:
        return "Draw"

def play_game():
    user_cards = [random.choice(cards) for _ in range(2)]
    computer_cards = [random.choice(cards) for _ in range(2)]


    print_game_state(user_cards, computer_cards)

    while True:
        user_score = score(user_cards)
        if user_score > 21:
            print("You went over 21. Computer wins!")
            return

        action = input("If you want another card, press 'y'. Type 'n' to pass: ")
        
        if action.lower() == 'y':
            user_cards.append(random.choice(cards))
            print_game_state(user_cards, computer_cards)
        else:
            break

    while score(computer_cards) < 17:
        computer_cards.append(random.choice(cards))

    result = check_scores(user_cards, computer_cards)
    print_game_state(user_cards, computer_cards, reveal_computer=True)
    print(result)

while True:
    play_game()
    play_again = input("If you want to play again, press 'y'. To exit, press 'n': ")
    if play_again.lower() == 'n':
        break

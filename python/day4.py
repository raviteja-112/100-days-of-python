import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock,1 for paper or 2 for Scissors. "))

game_images = [rock,paper,scissors]
#better approach
#it would be print(game_images[user_choice])
#to get the ascii art not printing them manually
if(user_choice == 0):
    print(f"You chose:\n{rock}")
    if(computer_choice == 0):
        print(f"computer chose :\n{rock}\n") #testing print(f"computer chose :\n")  #print(game_images[user_choice])
        print("Draw!")
    elif(computer_choice == 1):
        print(f"computer chose :\n{paper}\n")
        print("Computer Won!")
    elif(computer_choice == 2):
        print(f"Computer chose :\n{scissors}\n")
        print("You won!")
elif(user_choice == 1):
    print(f"You chose:\n{paper}")
    if(computer_choice == 0):
        print(f"computer chose :\n{rock}\n")
        print("You won!")
    elif(computer_choice == 1):
        print(f"computer chose :\n{paper}\n")
        print("Draw!")
    elif(computer_choice == 2):
        print(f"Computer chose :\n{scissors}\n")
        print("Computer Won!")
elif(user_choice == 2):
    print(f"You chose:\n{scissors}")
    if(computer_choice == 0):
        print(f"computer chose :\n{rock}\n")
        print("Computer Won!")
    elif(computer_choice == 1):
        print(f"computer chose :\n{paper}\n")
        print("You won!")
    elif(computer_choice == 2):
        print(f"Computer chose :\n{scissors}\n")
        print("Draw!")

print("Thanks for playing!")
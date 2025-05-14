import random
def gamewin(you,computer):
    if computer == you:
        return None
    elif computer == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif computer == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif computer == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False
you = input("Enter your choice in rock(r),paper(p),sicssor(s):")
if you == 'r' or you == 'p' or you == 's':
    print("computer  choice in rock(r),paper(p),sicssor(s):")
    comi = random.randint(1,3)
    if comi == 1:
        computer = "r"
    elif comi == 2:
        computer = "p"
    else:
        computer = "s"
    a = gamewin(you,computer)
    print(f"computer choice is {computer}")
    print(f"your  choice is {you}")
    if a == None:
        print("The game is a tie ")
    elif a == True:
        print("you won")
    else:
        print("you lost")
    
else:
    print("invalid input")


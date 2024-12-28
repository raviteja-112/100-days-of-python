import random
from day14_art import logo,vs
from day14_data import data
import os
print(logo)
def details(dataa):
    return (f"{dataa['name']},a {dataa['description']} from {dataa['country']}" )

def getfollowers(data):
    return data["follower_count"]

def check_answer(option,a_followers,b_followers):
    if a_followers > b_followers:
        return option == "a"
    else:
        return option == "b"
continuegame = True
score = 0
b = random.choice(data)
while continuegame:
    a = b
    b = random.choice(data)
    while(a==b):
        b = random.choice(data)
    print(f"Compare A:{details(a)}")
    print(vs)
    print(f"Agaist B:{details(b)}")

    a_followers = getfollowers(a)
    b_followers = getfollowers(b)
  
    option = input("Who has more followers?Type 'A' or 'B' :").lower()
    os.system('clear')
    print(logo)
    correct = check_answer(option,a_followers,b_followers)

    if correct:
        score = score +1
        print(f"you are right! Current score :{score}")
    else:
        print(f"Sorry it's wrong ! Final score is :{score}")
        continuegame = False



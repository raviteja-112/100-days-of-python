import pandas
import turtle


data = pandas.read_csv("day-25-us-states-game-start/50_states.csv")
states = data.state.tolist()

correct_states = []

learing_states = []

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape("day-25-us-states-game-start/blank_states_img.gif")
pen = turtle.Turtle()
turtle.shape("day-25-us-states-game-start/blank_states_img.gif")

while len(correct_states) != 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct",prompt="What's the another state's name").title()

    if answer_state == "Exit":
        break

    if answer_state in states and answer_state not in correct_states:
        correct_states.append(answer_state)
        state_data = data[data.state == answer_state]
        pen.hideturtle()
        pen.penup()
        pen.goto(float(state_data.x),float(state_data.y))
        pen.write(f"{answer_state}")

for i in states:
    if i not in correct_states:
        learing_states.append(i)


df = pandas.DataFrame(learing_states)
df.to_csv("learning_states.csv",index=False)
from flask import Flask
from random import randint
app = Flask(__name__)

class Guess():
    def __init__(self) -> None:
        self.correct_answer = int(randint(0,9))
    def refresh(self):
        self.correct_answer = int(randint(0,9))


# def h1(function):
#     def wrapper():
#         return'<h1>'+function()+"</h1>"
#     return wrapper

guess = Guess()
# @h1
@app.route("/")
def numbers():
    global guess
    guess.refresh()
    return "<h1>Guess a number 0 and 9 </h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='0 to 9'>"


@app.route("/<int:guessed_number>")
def guess_numbers(guessed_number):
    if guessed_number > guess.correct_answer:
        return "<h1 style = 'color:purple'>Too high,try again!</h1>" \
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='too high'>"
    
    elif guessed_number < guess.correct_answer:
        return "<h1 style = 'color:red'>Too low,try again!</h1>" \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='too low'>"
    else:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'





if __name__ == "__main__":
    app.run(debug=True)
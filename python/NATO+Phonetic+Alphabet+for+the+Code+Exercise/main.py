# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("NATO+Phonetic+Alphabet+for+the+Code+Exercise/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def function():
    word = input("Enter a word: ").upper()
    try:  
        output_list = [phonetic_dict[letter] for letter in word]
        
    except KeyError:
        print("Sorry,only letters in the alphabet please")
        function()
    else:
        print(output_list)
function()


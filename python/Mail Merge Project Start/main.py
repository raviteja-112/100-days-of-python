#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for i in names:
    with open(f"Mail Merge Project Start/Output/ReadyToSend/letter_for_{i}.txt",mode = "w") as file:
        stripped_name = i.strip("\n")
        personal_letter = letter.replace(f"[name]",stripped_name)
        file.write(personal_letter)


        
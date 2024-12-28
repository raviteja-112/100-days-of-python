# file = open("text.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("text.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("text.txt",mode= "w") as file:
#     file.write("come on ")


with open("text.txt",mode= "a") as file:
    file.write("\ncome on ")
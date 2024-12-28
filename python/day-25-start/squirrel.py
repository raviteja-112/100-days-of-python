import pandas

data = pandas.read_csv("day-25-start/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# squirrel_data = data["Primary Fur Color"]
# gray = red = black = 0

# for i in squirrel_data:
#     if i == "Gray":
#         gray = gray +1 
#     elif i == "Cinnamon":
#         red = red +1 
#     elif i == "Black":
#         black = black +1 

# new_dict = {
#     "Primary color" : ["gray" , "red","black"],
#     "Number" : [gray,red,black]
# }

# new_data = pandas.DataFrame(new_dict)

# print(new_data)


#optimized solution

grey_squirrels = len(data[data["Primary Fur Color"]== "Gray"])
red_squirrels = len(data[data["Primary Fur Color"]== "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"]== "Black"])

print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fur color" : ["gray","cinnamon","black"],
    "count" : [grey_squirrels , red_squirrels,black_squirrels]

}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel count")
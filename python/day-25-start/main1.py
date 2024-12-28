import pandas

data = pandas.read_csv("day-25-start/weather_data.csv")
data_dict = data.to_dict()
# print(data_dict)

list = data["temp"].to_list()
# print(list)
# temp = 0
# for i in list:
#     temp = i + temp

# average = temp / len(list)

# print(average)

## to calculate mean by pandas
## inbuilt funciton

# print(data["temp"].mean())

## to get highest value in the list using pandas

# print(data["temp"].max())

#get data in oolumns 

# print(data["condition"])
# print(data.condition)


## to get data from rows

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# temp = monday.temp[0]

# print(temp)

#create a dataframe from scratch

data_dict = {
    "students" : ["ajay","geetha","arya"],
    "scores" : [80,95,55]
}

data = pandas.DataFrame(data_dict)
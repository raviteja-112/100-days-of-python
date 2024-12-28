# with open("weather_data.csv") as file:
#     data = file.readlines()


# import csv 

# with open("day-25-start/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for rows in data:
#         for row in data:
#             temperatures.append(int(row[1]))

      
#         print(temperatures)



import pandas

data = pandas.read_csv("day-25-start/weather_data.csv")
print(data)



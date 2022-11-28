import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average = 0
# for temp in temp_list:
#     average += int(temp)
# just use sum function || sum(temp_list)
# average /= len(temp_list)
# print(average)

# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data.condition)
#
# print(data[data.day == 'Monday'])

# maximum = data["temp"].max()
# print(data[data.temp == maximum])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# f_temp = int(monday.temp) * 1.8 + 32
# print(f_temp)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
# data_student = pandas.DataFrame(data_dict)
# print(data_student)
# data_student.to_csv("new_data_student.csv")

squirrel_data = pandas.read_csv("central_park_data.csv")

print(len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]))

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]),
              len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]),
              len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])],
}

data_squirrel = pandas.DataFrame(data_dict)
data_squirrel.to_csv("central_park_squirrels.csv")


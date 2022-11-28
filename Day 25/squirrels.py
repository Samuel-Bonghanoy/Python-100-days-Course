import pandas

squirrel_data = pandas.read_csv("central_park_data.csv")

print(len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]))

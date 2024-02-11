import csv

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240205.csv")
grey= len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black= len(data[data["Primary Fur Color"]== "Black"])

dictionary = {
    "Fur Color" : ["Gray" ,"Cinnamon" ,"Black"],
    "count" : [grey,cinnamon,black]
}
data_frame= pandas.DataFrame(dictionary)
data_frame.to_csv("squirrel_count.csv")






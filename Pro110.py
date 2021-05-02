import plotly.figure_factory as ff 
import plotly.graph_objects as go
import random
import pandas as pd
import csv 
import statistics 

f = pd.read_csv("Pro110 - Data.csv")
data = f["claps"].tolist()




dataSet = []
for i in range(0,100):
    randomIndex = random.randint(0,len(data))
    value = data[randomIndex]
    dataSet.append(value)

mean = statistics.mean(dataSet)
median = statistics.median(dataSet)
std_deviation = statistics.stdev(dataSet)

print(mean , median , std_deviation)

figure = ff.create_distplot([dataSet],["claps"],show_hist= False)
figure.add_trace(go.Scatter(x = [mean,mean], y = [0,1] , mode = "lines" , name = "Mean" ))
figure.show()





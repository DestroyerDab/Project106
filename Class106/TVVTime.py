import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Size of TV", y="Average Time")
        fig.show()

def getDataSource(data_path):
    SOT = []
    AT = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            SOT.append(float(row["Size of TV"]))
            AT.append(float(row["Average Time"]))

    return {"x" : SOT, "y": AT}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between TV Size vs Time Spent on TV :-  \n--->",correlation[0,1])

data_path  = "TVVTime.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)
plotFigure(data_path)
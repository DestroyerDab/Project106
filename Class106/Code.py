import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    Days = []
    Percentage = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Days.append(float(row["Days Present"]))
            Percentage.append(float(row["Marks In Percentage"]))

    return {"x" : Days, "y": Percentage}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Days Present vs Marks Of Percentage :-  \n--->",correlation[0,1])

data_path  = "AttendanceVScore.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)
plotFigure(data_path)
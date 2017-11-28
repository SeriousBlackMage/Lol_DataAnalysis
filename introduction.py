import plotly.graph_objs as go
import plotly.plotly as py

from Lol_DataAnalysis.getdata import DataScraper

if __name__ == '__main__':
    labels = []
    values = []
    root = DataScraper('RGAPI-1d3d34c6-5a35-48f7-bdc4-15b5e3a5af54')
    data = root.getMatchData("SeriousBlackMage",'euw1',kills=True,deaths=True)
    #data = root.average(str(input("Name: ")),'euw1')
    print(data)
    for i in data:
        for j in data[i]:
            labels.append(j)
            values.append(data[i][j])

    trace = go.Pie(labels=labels, values=values)
    py.plot([trace])

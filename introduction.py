import plotly.graph_objs as go
import plotly.plotly as py

from Lol_Data.getdata import DataScraper

if __name__ == '__main__':
    labels = []
    values = []
    root = DataScraper('RGAPI-a444d470-72a1-47c7-9b4a-52acf6674e64')
    data = root.average(str(input("Name: ")),'euw1')
    for i in data:
        labels.append(i)
        values.append(data[i])

    trace = go.Pie(labels=labels, values=values)
    py.plot([trace])

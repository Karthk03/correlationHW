import plotly.express as px
import csv
import numpy as np
import pandas as py

def setup():
    with open('./data/gradeData.csv') as f:
        atendance = []
        grades = []
        df = csv.DictReader(f)
        for i in df:
            atendance.append(float(i['Days Present']))
            grades.append(float(i['Marks In Percentage']))
    return{'x':atendance,'y':grades}

data = setup()
correlation = np.corrcoef(data['x'],data['y'])
print(correlation[0,1])

df = py.read_csv('./data/gradeData.csv')
fd = px.scatter(df,x = 'Marks In Percentage', y = 'Days Present')
fd.show()
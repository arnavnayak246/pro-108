import plotly.figure_factory as ff
import pandas as pd 
import random
import scipy
import csv

df = pd.read_csv("Data2.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=True)
fig.show()
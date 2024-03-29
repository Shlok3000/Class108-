import csv
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["height"], show_hist=False)
fig.show()
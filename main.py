import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
df=pd.read_csv('data.csv')
#print(df)
#fig=px.bar(x=dice_result,y=count)
rating=df['Avg Rating']
#print(rating.median())
fig=ff.create_distplot([rating],['AVG RATING OF MOBILE BRANDS'])
fig.show()
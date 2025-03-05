import pandas as pd
import seaborn as sns
import plotly.express as px

df = sns.load_dataset('iris')
#df.head()

fig = px.scatter(df, x='sepal_length', y = 'sepal_width', color='species',
title='Sepal Length vs Sepal Width', labels={'sepal_length':'sepal Length', 'sepal_width':'Sepal Width'},
symbol='species', template='plotly_dark',size='petal_length',)
fig.show()
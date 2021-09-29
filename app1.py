import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from bokeh.plotting import figure
import plotly.figure_factory as ff

import matplotlib.pyplot as plt
import matplotlib

import seaborn as sns

det = pd.read_csv('F:\PyCharm\Data Analytics\Sports\Teams.csv')

df = det[det['franchID'] == 'DET']

df2 = df[df.franchID.str.contains('DET', case=False).replace('null', np.nan).dropna()]

st.title('Detroit Red Wings History')
#
# st.write('Playoff Rounds ')
# my_colors = ['r', 'k']*5

st.subheader('Goals for Goals Against')
# st.write(df2)
# st.bar_chart(df2['GF'])
# st.bar_chart(df2['GA'])



x = det['GF']
y = det['year']

p = figure(
    title='Goals for every year',
    x_axis_label='Goals for',
    y_axis_label='year'

)

p.line(x, y, legend_label='Goals for over the year')

st.bokeh_chart(p, use_container_width=True)
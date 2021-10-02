import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image
st.set_option('deprecation.showPyplotGlobalUse', False)


det = pd.read_csv('F:\PyCharm\Data Analytics\Sports\Teams.csv')

df = det[det['franchID'] == 'DET']

df2 = df[df.franchID.str.contains('DET', case=False).replace('null', np.nan).dropna()]



img=Image.open('redwingslogo.png')
st.image(img, width=400)

st.title('Detroit Red Wings History')
st.markdown("The Detroit Red Wings are a professional ice hockey team based in Detroit. They compete in the NHL, and "
            "are one of the Original Six teams of the league. They were founded in 1926. As of 2021, the Red Wings have"
            "won the most Stanley Cup championships out of all American teams. The Red Wings are one of the most "
            "successful and popular franchises in the NHL.")


st.sidebar.subheader('Explore Stats')
st.sidebar.markdown('Tick a box on the side panel to explore the dataset')
if st.sidebar.checkbox('Basic Info'):
    if st.sidebar.checkbox('Dataset Quick Look'):
        st.subheader('Dataset Quick Look: ')
        st.write(df2.head())

    if st.sidebar.checkbox('Show raw data', False):
        st.subheader('Raw data')
        st.write(df)

    if st.sidebar.checkbox('Show Columns'):
        st.subheader('Show columns list')
        all_columns = df2.columns.to_list()
        st.write(all_columns)

    if st.sidebar.checkbox('Statistical Description'):
        st.subheader('Statistical Data Description')
        st.write(df2.describe())
    if st.sidebar.checkbox('Missing Values?'):
        st.subheader('Missing values')
        st.table(df2.isnull().sum())

st.sidebar.title('Creating Visualizations')
st.sidebar.subheader('Create and show visualizations.')
if st.sidebar.checkbox('Graphics'):
    if st.sidebar.checkbox('Count Plot'):
        st.subheader('Count Plot')
        st.info("If there's an error, adjust column name on side panel.")
        column_count_plot = st.sidebar.selectbox('Choose a column to plot count.', df2.columns)
        hue_opt = st.sidebar.selectbox('Optional categorical variables (countplot hue)',
                                       df2.columns.insert(0, None))
        fig = sns.countplot(x=column_count_plot, data=df2, hue=hue_opt)
        fig.tick_params(axis='x', rotation=90)
        st.pyplot()

    if st.sidebar.checkbox('Histogram | Distplot'):
        st.subheader('Histogram | Distplot')
        st.info("If there's an error, adjust column name on side panel.")
        if st.checkbox('Dist plot'):
            column_dist_plot = st.sidebar.selectbox("Optional categorical variables (countplot hue)", df2.columns)
            fig = sns.displot(df2[column_dist_plot])
            st.pyplot()

    if st.sidebar.checkbox('Boxplot'):
        st.subheader('Boxplot')
        st.info("If there's an error, adjust column name on side panel.")
        column_box_plot_X = st.sidebar.selectbox("X (Choose a column)", df2.columns.insert(0, None))
        column_box_plot_Y = st.sidebar.selectbox("Y (Choose a column - only numerical)", df2.columns)
        hue_box_opt = st.sidebar.selectbox("Optional categorical variables (boxplot hue)", df2.columns.insert(0, None))
        if st.checkbox('Plot Boxplot'):
            fig = sns.boxplot(x=column_box_plot_X,
                              y=column_box_plot_Y,
                              data=df2,
                              palette='Set3')
            fig.tick_params(axis='x', rotation=90)
            st.pyplot()
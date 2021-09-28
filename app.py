import streamlit as st
from PIL import Image

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import pandas as pd
import numpy as np

import cufflinks as cf

det = pd.read_csv('F:\PyCharm\Data Analytics\Sports\Teams.csv')

df = det[det['franchID'] == 'DET']

df2 = df[df.franchID.str.contains('DET', case=False).replace('null', np.nan).dropna()]

st.title('Red Wings History')


if st.button('Goals for and Goals Against between 1926-2011'):
    images = ('GF and GA')
    st.image(images, width=300)

st.info('The dataset contains the Goals for and Goals against over the years.')

st.sidebar.markdown('##Side Panel')
st.sidebar.markdown("Use this panel to explore stats on the Red Wings over the years.")

@st.cache(persist=True, show_spinner=True)
# Load the data
def load_data(nrows):
    # Parse date and time
    df = pd.read_csv(det, nrows=nrows)
    lowercase = lambda x:str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)
    return df


st.markdown




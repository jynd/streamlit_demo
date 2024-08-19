import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('This is a header')

#example 1

st.write('This is a write')

#example 2
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
    'third column': [101, 210, 310, 140],
})

st.write(df)

#example 3

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
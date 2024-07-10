import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c'])

chart = alt.Chart(data).mark_circle().encode(
    x='a',y='b',tooltip=['a','b']
)
st.altair_chart(chart)

plt.scatter(data['a'],data['b'])
st.pyplot()
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

st.graphviz_chart("""
digraph{
watch -> share
share -> like
like -> subscribe
like -> watch}
""")

city = pd.DataFrame({
'awesome cities': ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
'lat' : [41.868171, 44.979840, 38.257972, 39.030575],
'lon' : [-87.667458, -93.272474, -85.765187, -95.702548]
})
st.map(city)
st.map()

st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fletsenhance.io%2F&psig=AOvVaw1sugHR4VcQhmBlkZK9fhOj&ust=1720720903399000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCOiOt4OHnYcDFQAAAAAdAAAAABAE")
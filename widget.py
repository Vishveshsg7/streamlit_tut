import streamlit as st

st.title("Widgets")

#to add button
if st.button("Press here to hit a spank"):
    st.write("You had just hit spank on the juicy ass")

name = st.text_input("ENter the name of the person's ass")
st.write(name)

address = st.text_area("Enter hers address")
st.write(address)

st.date_input("Enter a date you mate")

st.time_input("Enter your time of hitting")

if st.checkbox("You proposed",value=False):
    st.write("now kiss her!!!")

st.radio("Colours",["r","g","b"],index=1)

st.selectbox("Colours",["r","g","b"],index=2)

st.multiselect("Colours",["r","g","b"])

age= st.slider("age",min_value=18, max_value=60, value=30, step=5)
st.write(age)

#remeber to use float
st.number_input("numbers",min_value=18.0, max_value=60.0, value=30.0, step=5.0)

#upload a file
uploaded_file = st.file_uploader("Choose a file")

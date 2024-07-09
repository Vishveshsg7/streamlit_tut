import streamlit as st
st.title("Hello Vishvesh")
st.header("Engineer")
st.subheader("None")
st.text("Me kuch nahi bolunga")
st.markdown(""" # h1 tag
## h2 tag
### h3 tag
:laugh:
:sunglasses:
** bold **
_ itlaics _""",True)
st.write("Vishvesh","And", "Sneha")
d = {
"name": "Harsh",
"language":"Python",
"topic":"Streamlit"}
st.write(d)
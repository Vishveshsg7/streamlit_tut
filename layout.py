import streamlit as st
st.title("Registered form")

first,last = st.columns(2)

first.text_input("First Name")
last.text_input("Last Name")

email,job = st.columns([3,1]) 
email.text_input("Email Id")
job.selectbox("Job",["Student","Teacher","Researcher","Others"])

user,pw,pw2 = st.columns(3)
user.text_input("Username")
pw.text_input("Password",type="password")
pw2.text_input("Confirm Password",type="password")

st.checkbox("By clicking this checkbox you accept all the informaton given as the true information")
st.button("Submit")
import streamlit as st

st.title("Model Deployment")

name = st.text_input("Enter Your Name")

salary = st.number_input("Enter Your Salary",min_value=0,max_value=100)

doj = st.date_input("Enter Your Joining date")

gender =  st.radio("Select Your Gender",["Male","Female"],horizontal=True)

st.write("Select Your hobblies")
cricket=st.checkbox("Cricket")
football = st.checkbox("Football")

age=st.slider("Select Your Age")
print(name,salary,doj,)
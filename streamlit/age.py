import  streamlit as st
from datetime import date

st.title("age calculator~")
st.subheader("enter the dob and get the age")

current_year = date.today().year
dob = st.date_input("dob")

if dob.year > current_year:
    st.error("invalid date")
else:
    age = current_year - dob.year
    st.success(f"your age is {age} years")
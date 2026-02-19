import  streamlit as st

st.title("smart bedroom")

if st.button("make chai"):
    st.write("ban rhi...intezaar kare~")

add_masala = st.checkbox("masala daale")

if add_masala:
    st.success("masala dal gya")

tea_type = st.radio("chai base?", ["milk", "water"])
st.write(f"selected base: {tea_type}")

flavour = st.selectbox("choose flavour:  ", ["plain", "adrak", "jaggery", "tulsi"])
st.write(f"selected flavour: {flavour} ")

sugar = st.slider("suger qty (spoons)", 0, 5, 2)
st.write(f"selected sugar qty: {sugar} ")

cups = st.number_input("how many cups ", min_value=1, max_value=10, step=1)
st.write(f"selected cups: {cups}")

name = st.text_input("enter your name ")
if name:
    st.write(f"welcome, {name} ! chai ban rhi hai, sabr rakho")

dob = st.date_input("select ur DOB")
st.write(f"ur dob is {dob}")


import streamlit as st

st.title("Hello inte")
st.subheader("made with streamlit")
st.text("welcome inte, this is first streamlit interactive application~ #st.text")
st.write("lets learn streamlit~ #st.write")

# favorite game
game = st.selectbox("what's your favorite game?  " , ["Minecraft", "plato", "brawlstars", "pubg"])
st.write(f"you chose {game}. Excellent choice!")
st.success(f"then go play {game}")
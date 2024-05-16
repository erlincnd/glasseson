import streamlit as st

st.title("Glasses On")
st.subheader("Explore various eyeglass shapes according to your face shape for a visually more attractive appearance...")
st.image('logo glasses-on 2.png', caption=None, width=300, )
st.write ("Ketahui bentuk wajah kamu terlebih dahulu")
if st.button("Mulai"):
    st.switch_page("pages/2-Upload.py")

import streamlit as st
from PIL import Image
import io

st.title("Glasses On")
st.image('logo glasses-on 2.png', caption=None, width=200, )
wajah = st.text_input("Bentuk Wajah: ",st.session_state['bentuk'])
st.session_state['wajah']=wajah
jeniskelamin = st.selectbox(
    "Jenis Kelamin",
    ("Pria", "Wanita"),
    index=None,
    placeholder= "Pilih jenis kelamin")
st.session_state['jeniskelamin']=jeniskelamin
tinggimin = st.selectbox(
    "Tinggi Minus",
    ("Kecil <-1.00", "Sedang -1.00 s.d -3.00", "Tinggi -3.01 s.d -6.00", "Sangat tinggi >-6.00"),
    index=None,
    placeholder= "Berapa minus kamu?")
st.session_state['tinggimin']=tinggimin
penggunaan = st.selectbox(
    "Penggunaan",
    ("Fashion", "Sehari-hari"),
    index=None,
    placeholder= "Pilih jenis penggunaan")
st.session_state['penggunaan']=penggunaan

if st.button("Lihat Rekomendasi Frame Kacamata"):
    st.switch_page("pages/Rekomendasi.py")
    

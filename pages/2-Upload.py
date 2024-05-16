import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Glasses On", page_icon="👓")
st.title("Glasses On")
st.image('logo glasses-on 2.png', caption=None, width=300, )
st.write ("Input gambar wajah dengan ketentuan sebagai berikut :")
st.write ("1. Posisi tegak dan dari jarak dekat")
st.write ("2. Tidak menggunakan kacamata dan tidak menggunakan aksesoris pada wajah")
st.write ("3. Pencahayaan yang cukup")
uploaded_file = st.file_uploader("Pilih file gambar", type=["jpg","jpeg","png"])
if uploaded_file is not None:
    # Membaca file yang diunggah sebagai gambar
    image = Image.open(uploaded_file)
    
    # Menampilkan gambar
    st.image(image, caption='Gambar yang diunggah', width=200)

    # Menampilkan informasi tentang gambar
    st.write("Format gambar:", image.format)
    st.write("Ukuran gambar:", image.size)
    st.write("Mode gambar:",image.mode)

    st.session_state['my_image']=uploaded_file
if st.button("Lanjutkan"):
    st.switch_page("pages/3-Identifikasi.py")

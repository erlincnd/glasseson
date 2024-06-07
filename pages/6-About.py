import streamlit as st

st.set_page_config(page_title="Glasses On", page_icon="👓")
st.title("Glasses On")
st.image('logo glasses-on 2.png', caption=None, width=300, )

st.write ("Website ini merupakan sistem yang dibuat untuk menyelesaikan tugas akhir pendidikan S-1 Ilmu Komputer di Universitas Sumatera Utara.")
st.write ("dengan judul : ")

g1,g2,g3 = st.columns(3)
with g1:
    st.write (" ")
with g2:
    st.image("lambang usu.png", caption=None, width=200)
with g3:
    st.write (" ")
    
st.markdown('<strong><h3 style="color:#006400;" align="center">Penerapan Convolutional Neural Network dan Evaluation Based on Distance from Average Solution dalam Sistem Cerdas Kesesuaian Frame Kacamata dengan Identifikasi Bentuk Wajah</h3></strong>', unsafe_allow_html=True)


c1,c2,c3 = st.columns(3)

with c1:
    st.markdown('<strong><p style="color:green;">Penulis.</p></strong>', unsafe_allow_html=True)
    st.write ("Erlin Cindini Manullang")
    st.write ("NIM 201401047")

with c2:
    st.markdown('<strong><p style="color:green;">Dosen Pembimbing I.</p></strong>', unsafe_allow_html=True)
    st.write ("Dewi Sartika Br. Ginting, S.Kom., M.Kom.")
    st.write ("NIP 199005042019032023")

with c3:
    st.markdown('<strong><p style="color:green;">Dosen Pembimbing II.</p></strong>', unsafe_allow_html=True)
    st.write ("Dr. Ir. Elviawaty Muisa Zamzami S.T., M.T., MM., IPU")
    st.write ("NIP 197007162005012002")

if st.button("Kembali ke Menu utama"):
    st.switch_page("main.py")

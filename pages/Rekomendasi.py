import streamlit as st
import numpy as np
from PIL import Image
import io
import os
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import pickle
from mtcnn.mtcnn import MTCNN

st.title("Glasses On")
c1,c2 = st.columns(2)

with c1:
    with st.container() :
        if 'my_image' in st.session_state:
          st.image(st.session_state['my_image'], width=200)

with c2:
    st.write ("Bentuk Wajah: ", st.session_state['bentuk'])
    st.write ("Jenis Kelamin: ", st.session_state['jeniskelamin'])
    st.write ("Tinggi Minus: ", st.session_state['tinggimin'])
    st.write ("Penggunaan: ", st.session_state['penggunaan'])
    if st.button("Kembali ke Menu utama"):
       st.switch_page("main.py")

wajah = st.session_state['bentuk']
jeniskelamin = st.session_state['jeniskelamin']
tinggimin = st.session_state['tinggimin']
penggunaan = st.session_state['penggunaan']

def rata(matriks):
    return np.mean(matriks, axis=0)

mat2 = np.zeros((4, 4))
if wajah == 'Round' :
  values = [0.1, 0.8, 0.8, 0.7]
  for i in range(len(values)):
    mat2[i, 0] = values[i]
elif wajah == 'Oval' :
  values = [0.8, 0.6, 0.7, 0.4]
  for i in range(len(values)):
    mat2[i, 0] = values[i]
elif wajah == 'Heart' :
  values = [0.6, 0.2, 0.7, 0.7]
  for i in range(len(values)):
    mat2[i, 0] = values[i]
elif wajah == 'Oblong' :
  values = [0.7, 0.2, 0.5, 0.5]
  for i in range(len(values)):
    mat2[i, 0] = values[i]
elif wajah == 'Square' :
  values = [0.8, 0.2, 0.6, 0.1]
  for i in range(len(values)):
    mat2[i, 0] = values[i]

if jeniskelamin == 'Pria' :
  values = [0.3, 0.6, 0.2, 0.7]
  for i in range(len(values)):
    mat2[i, 1] = values[i]
elif jeniskelamin == 'Wanita' :
  values = [0.7, 0.2, 0.6, 0.4]
  for i in range(len(values)):
    mat2[i, 1] = values[i]

if tinggimin == 'Kecil <-1.00' :
  values = [0.7, 0.5, 0.7, 0.6]
  for i in range(len(values)):
    mat2[i, 2] = values[i]
elif tinggimin == 'Sedang -1.00 s.d -3.00' :
  values = [0.8, 0.4, 0.6, 0.5]
  for i in range(len(values)):
    mat2[i, 2] = values[i]
elif tinggimin == 'Tinggi -3.01 s.d -6.00' :
  values = [0.8, 0.3, 0.2, 0.5]
  for i in range(len(values)):
    mat2[i, 2] = values[i]
else :
  values = [0.9, 0.2, 0.1, 0.4]
  for i in range(len(values)):
    mat2[i, 2] = values[i]

if penggunaan == 'Sehari-hari' :
   values = [0.7, 0.2, 0.8, 0.9]
   for i in range(len(values)):
    mat2[i, 3] = values[i]
elif penggunaan == 'Fashion' :
   values = [0.8, 0.4, 0.5, 0.3]
   for i in range(len(values)):
    mat2[i, 3] = values[i]

hasil = rata(mat2)
print(mat2)

def jarak(alternative,mean, weight):

  n = len(alternative)  # Jumlah kriteria
  pda_sum = 0
  nda_sum = 0

  for j in range(n):
        # print(alternative[j])
        # print(mean[j])
        d_plus = max(0, (alternative[j] - mean[j])/mean[j])
        d_minus = max(0, (mean[j] - alternative[j])/mean[j])
        # print("pda ", j, "=", d_plus)
        # print("nda ", j, "=", d_minus)
        pda_sum += d_plus*weight[j]
        nda_sum += d_minus*weight[j]

  pda = pda_sum
  nda = nda_sum

  return pda, nda

bobot = np.array([0.4, 0.3, 0.2, 0.1])

bobot_pda = np.zeros(4)
bobot_nda = np.zeros(4)
for i, alternative in enumerate(mat2):
    pda, nda = jarak(alternative, hasil, bobot)
    bobot_pda[i] = pda
    bobot_nda[i] = nda

print('bobot pda',bobot_pda)
print('bobot nda',bobot_nda)

def norm(bobot_pda,bobot_nda) :
  max_pda = max(bobot_pda)
  max_nda = max(bobot_nda)
  norm_pda = np.zeros(4)
  norm_nda = np.zeros(4)
  for i in range(len(bobot_pda)):
    norm_pda[i] = bobot_pda[i]/max_pda
    norm_nda[i] = bobot_nda[i]/max_nda
  return norm_pda, norm_nda
norm_pda, norm_nda = norm(bobot_pda, bobot_nda)
print("normalisasi NSP : ")
print(norm_pda)
print("normalisasi NSN : ")
print(norm_nda)

def skor(norm_pda, norm_nda) :
  return ((norm_pda + norm_nda)/2)

skoring = np.zeros(4)
for i in range(len(norm_pda)) :
  skoring[i] = skor(norm_pda[i], norm_nda[i])

print("hasil skoring")
print(skoring)

def rank(skoring) :
  print(np.argsort(skoring)[::-1])
  return np.argsort(skoring)[::-1]

ranking = rank(skoring)
print("ranking = ", ranking)

test_path_round = 'D:\kuliah\skripsi\glasses on\Eyeglasses Dataset\Round'
test_files_round = os.listdir(test_path_round)

test_img_round = []

for i in test_files_round:
    img_round = os.path.join(test_path_round,i)
    test_img_round.append(img_round)

test_path_square = 'D:\kuliah\skripsi\glasses on\Eyeglasses Dataset\Square'
test_files_square = os.listdir(test_path_square)

test_img_square = []

for i in test_files_square:
    img_square = os.path.join(test_path_square,i)
    test_img_square.append(img_square)

test_path_cateye = 'D:\kuliah\skripsi\glasses on\Eyeglasses Dataset\Cat Eye'
test_files_cateye = os.listdir(test_path_cateye)

test_img_cateye = []

for i in test_files_cateye:
    img_cateye = os.path.join(test_path_cateye,i)
    test_img_cateye.append(img_cateye)

test_path_aviator = 'D:\kuliah\skripsi\glasses on\Eyeglasses Dataset\Aviator'
test_files_aviator = os.listdir(test_path_aviator)

test_img_aviator = []

for i in test_files_aviator:
    img_aviator = os.path.join(test_path_aviator,i)
    test_img_aviator.append(img_aviator)

urutan = ['round', 'square', 'cat eye', 'aviator']
urutan_baru = [urutan[i] for i in ranking]

tab1, tab2 = st.tabs(["Paling Rekomendasi", "Cukup Rekomendasi"])
with tab1:
    st.write ("Frame Kacamata yang paling direkomendasikan sesuai bentuk wajah kamu : ")
    for i in range (2) :
        if urutan_baru[i] == 'round' : 
         st.image(test_img_round[1], caption='Round', width=150)
        elif urutan_baru[i] == 'square' :
          st.image(test_img_square[1], caption='Square', width=150)
        elif urutan_baru[i] == 'cat eye' :
          st.image(test_img_cateye[1], caption='Cat Eye', width=150)
        elif urutan_baru[i] == 'aviator' :
          st.image(test_img_aviator[1], caption='Aviator', width=150)

with tab2:
    st.write ("Frame Kacamata yang cukup direkomendasikan sesuai bentuk wajah kamu : ")
    for i in range (2,4) :
        if urutan_baru[i] == 'round' : 
         st.image(test_img_round[1], caption='Round', width=150)
        elif urutan_baru[i] == 'square' :
          st.image(test_img_square[1], caption='Square', width=150)
        elif urutan_baru[i] == 'cat eye' :
          st.image(test_img_cateye[1], caption='Cat Eye', width=150)
        elif urutan_baru[i] == 'aviator' :
          st.image(test_img_aviator[1], caption='Aviator', width=150)

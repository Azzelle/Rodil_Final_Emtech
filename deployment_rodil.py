# -*- coding: utf-8 -*-
"""Deployment_Rodil.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y2wvwU8TgxNcfC5vAoi_Qgav96tbufv9
"""

import streamlit as st
import tensorflow as tf

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('final_model2.h5')
  return model
model=load_model()
st.write("""
# Weather Classifier"""
)
st.write("""Final Requirement""")
st.write("""Submitted by: Azzelle Leira Rodil""")
st.write("""This activity classify the sky weather condition, whether it is Cloudyy, Sunshine, Sunrise and Rain.""")

file=st.file_uploader("Choose sky weather photo from computer",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import cv2
def import_and_predict(image_data,model):
    input_arr = img_to_array(image_data)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    prediction = model.predict(input_arr)
    return prediction

if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    image=load_img(file, target_size=(32,32,3))
    prediction=import_and_predict(image,model)
    class_names=['Cloudy', 
                 'Rain', 
                 'Sunrise', 
                 'Shine']
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)

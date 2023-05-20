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
import numpy as np
def import_and_predict(image_data,model):
    size=(128,128)
    image=ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['Cloudy','Shine','Sunrise','Rain']
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)

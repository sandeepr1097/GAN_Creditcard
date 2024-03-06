# -*- coding: utf-8 -*-
"""app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ii98Q-GdyQYg_77I4zaVz8LSanMNN44O
"""

import pickle
import pandas as pd
import numpy as np
import sklearn
import joblib
import imblearn
import streamlit as st
from PIL import Image


st.title("Credit Card Fraud Detection Model")

st.image("Credit_Card_Fraud_Logo.jpg")
'''
input_df = st.text_input("Please provide all the required feature details: ")
input_df_split = input_df.split(',')

submit = st.button("Submit")
'''
loaded_model = joblib.load('https://github.com/sandeepr1097/GAN_Creditcard/Gan_Final_Shark.sav')
#Gan_Final_Shark_path = pickle.load(open('model.pkl','rb'))
input_df = st.file_uploader("Upload a CSV file", type=["csv"])
#input_df_split = input_df.split(',')
df = pd.read_csv(input_df)
st.write('### Uploaded CSV file:')
st.write(df)
submit = st.button("Submit")

if submit:
    prediction = loaded_model.predict(df)
    if 1 in prediction:
        st.warning('Alert: Fradulant Transaction!')
    else:
        st.warning('Alert: Legitimate Transaction!')



    
''' model = pickle.load(open('model.pkl','rb'))
    features = np.asarray(df,dtype = np.float64)
    st.write(features)
    #features = Arrays.toString(features)
    #prediction = new_model.predict(input_df)
    prediction = model.predict(np.array(features).reshape(1, -1))
    st.write(prediction)
'''
    

''' Gan_Final_Shark_path = "sandeepr1097/GAN_Creditcard/model.pkl" 
with open(Gan_Final_Shark_path, 'rb') as file:
    new_model = pickle.load(file)'''

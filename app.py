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
#input_df = st.text_input("Please provide all the required feature details: ")
#input_df_split = input_df.split(',')

input_df = st.file_uploader("Upload CSV File:", type = 'csv')
df = pd.read_csv(input_df)
st.write(df)

submit = st.button("Submit")


if submit:
    model = joblib.load('Gan_Final_Shark')
    features = np.asarray(input_df_split,dtype = np.float64)
    prediction = model.predict(features.reshape(1,-1))
    if 1 in prediction:
        st.warning('Alert: Fradulant Transaction!')
    else:
        st.warning('Alert: Legitimate Transaction!')


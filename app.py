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
input_df = st.text_input("Please provide all the required feature details: ")
input_df_split = input_df.split(',')

submit = st.button("Submit")


if submit:
    model = pickle.load(('model.pkl')
    features = np.asarray(input_df_split,dtype = np.float64)
    prediction = model.predict(features.reshape(1,-1))
    if 1 in prediction:
        st.warning('Alert: Fradulant Transaction!')
    else:
        st.warning('Alert: Legitimate Transaction!')


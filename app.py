# -*- coding: utf-8 -*-
"""app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ii98Q-GdyQYg_77I4zaVz8LSanMNN44O
"""
import os
import pickle
import pandas as pd
import numpy as np
import sklearn
import joblib
import imblearn
import streamlit as st
from PIL import Image
import subprocess
package_name_http = 'requests'
package_name_twilio_rest = 'twilio.rest'
package_name_twilio = 'twilio'
subprocess.run(f'pip install {package_name_twilio_rest}', shell=True)
subprocess.run(f'pip install {package_name_twilio}', shell=True)
subprocess.run(f'pip install {package_name_http}', shell=True)
from twilio.rest import Client



st.title("Credit Card Fraud Detection Model")

st.image("Credit_Card_Fraud_Logo.jpg")
#input_df = st.text_input("Please provide all the required feature details: ")
#input_df_split = input_df.split(',')

input_df = st.file_uploader("Upload CSV File:", type = 'csv')
if input_df!= None:
    df = pd.read_csv(input_df)
    st.write(df)

    #submit = st.button("Submit")
    
    if st.button("Submit"):
        model = joblib.load('Gan_Final_Shark')
        prediction = model.predict(df)
       #features = np.asarray(input_df_split,dtype = np.float64)
        #prediction = model.predict(features.reshape(1,-1))
        
        if 1 in prediction:
            st.warning(' Alert: Fradulant Transaction!', icon = '⚠️')
        else:
            st.warning(' Alert: Legitimate Transaction!', icon = '✅' )


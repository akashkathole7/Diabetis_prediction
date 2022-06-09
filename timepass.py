# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 21:51:29 2021

@author: akash kathole
"""

import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st

loaded_model = pickle.load(open('H:/New folder/diploit_model/trained_data.sav','rb'))

def diabetis_prediction(input_data):
    input_data = [1,89,66,23,94,28.1,0.167,21]
    in_array_data = np.array(input_data)
    reshape_data = in_array_data.reshape(1,-1) 
    prediction = model.predict(reshape_data)
    if prediction[0]==1:
        return 'patience have a diabetis'
    else:
        return 'patience have a no diabetis'
    
def main():
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
    Pregnancies = st.text_input("enter the no of Pregnancies")
    Glucose = st.text_input("enter the no of glucose")
    BloodPressure = st.text_input("enter the no of Blood Pressure")
    SkinThickness = st.text_input("enter the no of skin thick ness")
    Insulin = st.text_input("enter the no of Insulin")
    BMI= st.text_input("enter the no of BMI")
    DiabetesPedigreeFunction = st.text_input("enter the no of Diabetis pedifree function")
    Age = st.text_input("enter the no of Age")
    
    
    diagnosis = ''
if st.button('diabetis test result'):
    diagnosis = diabetis_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)
   
   
if __name__ == '__main__':
    main()


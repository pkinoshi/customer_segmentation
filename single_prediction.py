# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 20:10:56 2026

@author: DELL
"""

import streamlit as st
import pandas as pd
import numpy as np

def single_prediction_page(model):
    st.title("🧔‍Individual Customer Analysis👩‍🦰")
    st.info("Input customer details to determine their market profile.")
    
    col1, col2 = st.columns(2)
    with col1:
        annual_income = st.number_input("Annual Income(k$)")
        age = st.number_input("Age", 18, 99, 18)
    with col2:
        spending_score = st.number_input("Spending Score (1 - 100)")
        gender = st.selectbox("Gender", ["Male","Female"])
        
    if st.button("Predict Segment"):
        input_data = pd.DataFrame(data=np.array([[annual_income, spending_score]]),
                                  columns=["Annual Income (k$)", "Spending Score (1-100)"])
        
        cluster = model.predict(input_data)[0]
        cluster += 1
        
        st.subheader(f"Result: Cluster {cluster}.")
        st.write(f"This customer has been categorized into **Group {cluster}**.")
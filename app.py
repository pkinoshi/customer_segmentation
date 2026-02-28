# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 20:16:06 2026

@author: DELL
"""

import streamlit as st
from model_loader import load_kmeans_model
from single_prediction import single_prediction_page
from bulk_upload import bulk_upload_page

st.set_page_config(page_icon="🏪", page_title="Customer Segmenter", layout="wide")

@st.cache_resource
def get_model():
    return load_kmeans_model()

model = get_model()

# SIDEBAR NAVIGATION
st.sidebar.title("App Controls")    
page = st.sidebar.radio("Navigation", ["Single Segmentation", "Bulk CSV upload"])

# Reset functionality
st.sidebar.markdown("---")
if st.sidebar.button("Reset App"):
    st.rerun()
    
if page == "Single Segmentation":
    single_prediction_page(model)
else:
    bulk_upload_page(model)
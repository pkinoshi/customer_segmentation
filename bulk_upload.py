# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 20:13:41 2026

@author: DELL
"""

import streamlit as st
import pandas as pd

def bulk_upload_page(model):
    st.title("📂Batch Processing")
    st.write("Upload a CSV file to process multiple records at once.")
    
    st.subheader("Don't have a file?")
    sample_data = pd.DataFrame({
                "Annual Income (k$)": [15, 60, 35, 100, 80, 55],
                "Spending Score (1-100)": [39, 45, 70, 20, 90, 67],
                "Gender": ["Male","Female", "Female","Male","Female", "Male"],
                "Age" : [18, 45, 66, 95, 24, 38]
        })
    sample_csv = sample_data.to_csv(index=False).encode("utf-8")
    st.download_button("Download Sample CSV File", sample_csv, "sample_customers.csv", mime="text/csv")
    
    st.markdown("---")
    
    uploaded_file = st.file_uploader("Upload your CSV file", type=["CSV"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        features = ["Annual Income (k$)", "Spending Score (1-100)"]
        
        if set(features).issubset(df.columns):
            clusters = model.predict(df[features])
            relatable_clusters = [c+1 for c in clusters]
            df["Group"] = relatable_clusters
            
            st.success("Analysis Complete!")
            st.dataframe(df, use_container_width=True)
            
            output_csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("Download Predicted Results", output_csv, 
                               "segmented_customers.csv", mime="text/csv")
        else:
            st.error(f"Error: CSV must contain these exact headers: {features}")
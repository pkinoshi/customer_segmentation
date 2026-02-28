# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 20:09:07 2026

@author: DELL
"""

import joblib

def load_kmeans_model():
    with open("kmeans_model5.pkl", 'rb') as t:
        return joblib.load(t)
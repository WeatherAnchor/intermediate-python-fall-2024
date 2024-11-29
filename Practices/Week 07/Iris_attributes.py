from joblib import load
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

model = load('data/iris_model.joblib')

st.title('Iris Flower-Type Prediction')

col1, col2= st.columns(2)

with col1:
    sepal_length = st.number_input('Sepal length(cm)', min_value = 0.0, max_value = 15.0, step = 0.01)
    sepal_width = st.number_input('Sepal width(cm)', min_value = 0.0, max_value = 15.0, step = 0.01)
    
with col2:
    petal_length = st.number_input('Petal length(cm)', min_value = 0.0, max_value = 15.0, step = 0.01)
    petal_width = st.number_input('Petal width(cm)', min_value = 0.0, max_value = 15.0, step = 0.01)

if st.button("Predict"):
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(input_data)
    flower_types = {0: 'Iris_Setosa', 1: 'Iris_Versicolor', 2: 'Iris_Virginica'}
    result = flower_types.get(prediction[0])
    st.write(f"The predicted flower type is: {result}")
    if result == 'Iris_Setosa':
        st.image("images/iris_setosa.png", caption="Iris Setosa")
    elif result == 'Iris_Versicolor':
        st.image("images/iris_versicolor.png", caption="Iris Versicolor")
    elif result == 'Iris_Virginica':
        st.image("images/iris_virginica.png", caption="Iris Virginica")
























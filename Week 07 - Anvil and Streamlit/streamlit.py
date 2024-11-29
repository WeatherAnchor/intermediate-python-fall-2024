import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
@st.cache
def load_data():
    dataset = pd.read_csv(url, names=names)
    return dataset
dataset = load_data()

st.title("IRIS flower machine learning model")
if st.checkbox('Show dataframe'):
    dataset

fig = px.scatter(dataset, x="sepal-width", y="sepal-length", color="class",
                 size='petal-length', hover_data=['petal-width'],width=800, height=400)
st.plotly_chart(fig)

# Split-out test dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Make predictions on test dataset
model = SVC(gamma='auto')
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Evaluate predictions
acc = accuracy_score(y_test, predictions)
con = confusion_matrix(y_test, predictions)
con_df = pd.DataFrame(con).transpose()
cla_rep = classification_report(y_test, predictions, output_dict=True)
cla_rep_df = pd.DataFrame(cla_rep).transpose()

st.write("Accuracy: ",acc)
st.write("Confusion Matrix: ", con)
st.write("Classification report: ",cla_rep_df)

st.title("IRIS flower Prediction application")
sepal_len = st.slider("Sepal-length: ", 0.0, 10.0)
sepal_width = st.slider("Sepal-width: ", 0.0, 10.0)
petal_len = st.slider("Petal-length: ", 0.0, 10.0)
petal_width = st.slider("Petal-width: ", 0.0, 10.0)

def make_pred(sepal_l, sepal_w, petal_l, petal_w):
    input_array = np.array([sepal_l, sepal_w, petal_l, petal_w]).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    return prediction

if st.button('Make a prediction!'):
    prediction = make_pred(sepal_len, sepal_width, petal_len, petal_width)
    st.write("Predicted flower: ", prediction)
import streamlit as st
import plotly.express as px
import pandas as pd

# Title
st.title("Data Visualization App")

# File upload
uploaded_file = st.file_uploader("Drag and drop a CSV file here", type="csv")

# Read the file
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.write(df)

    # chart type dropdown
    chart_type = st.selectbox("Select chart type:", ["Bar Chart", "Line Chart", "Pie Chart"])

    # columns dropdown
    x_column = st.selectbox("Select X-axis column:", df.columns)
    y_column = st.selectbox("Select Y-axis column:", df.columns)

    # Chart selection
    if st.button("Generate Chart"):
        if chart_type == "Bar Chart":
            fig = px.bar(df, x=x_column, y=y_column, title="Bar Chart")
        elif chart_type == "Line Chart":
            fig = px.line(df, x=x_column, y=y_column, title="Line Chart")
        elif chart_type == "Pie Chart":
            fig = px.pie(df, names=x_column, values=y_column, title="Pie Chart")
        
        # Display the plot
        st.plotly_chart(fig)
else:
    st.info("Please upload a CSV file to get started.")
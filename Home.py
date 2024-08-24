import pandas as pd
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, welcome to my first Streamlit app!")

df=pd.read_csv(r'C:\Users\Baslael\Downloads\Compressed\data\data\benin-malanville.csv')

st.write(df.describe())
# import altair as alt
# print(alt.__version__)
import streamlit as st

st.title('Página 1')


import streamlit as st
import pandas as pd
#from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
 
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    columns=['Temperatura', 'Humedad'])
    st.write(dataframe)
    st.subheader('Estadisticos Básicos')
    st.write(dataframe.describe())

import streamlit as st

st.title('Análisis de Datos')


import streamlit as st
import pandas as pd
#from io import StringIO

uploaded_file = st.file_uploader("Cargue el archivo con los datos.")
column_names=["Humedad","Temperatura"]
if uploaded_file is not None:
 
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file, names=column_names)
  
    st.write(dataframe)
    chart_data = pd.DataFrame(dataframe, columns=['Humedad', 'Temperatura'])
    st.line_chart(chart_data)
    st.subheader('Estadisticos Básicos')
    st.write(dataframe.describe())
    st.write(len(dataframe))

import streamlit as st

st.title('Análisis de Datos')


import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
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

    def generar_dataframe_con_timestamp(longitud):
      inicio = datetime.now()
      timestamps = [inicio + timedelta(seconds=i) for i in range(longitud)]
      df = pd.DataFrame(index=timestamps)
      return df
    #longitud_dataframe = 10
    #dataframe_con_timestamp = generar_dataframe_con_timestamp(longitud_dataframe)
    d = st.date_input("Comienzo de la medición")
    inicio = d #datetime.now()
    indice_tiempo = pd.date_range(start=inicio, periods=len(dataframe), freq='5S')
    dataframe['Datetime'] =indice_tiempo
    dataframe = dataframe.set_index('Datetime')
    st.dataframe(dataframe)


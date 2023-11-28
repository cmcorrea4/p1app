import streamlit as st
from PIL import Image


st.title('Aplicaciones Tecnológicas para el Campo')

st.header("MEJORA DE LA PRODUCTIVIDAD A TRAVÉS DEL USO DE TECNOLOGÍAS")


image = Image.open("Agriculture.png")
st.image(image, caption="Tecnología para Productividad")

st.write("El uso de tecnologías de la Industria 4.0 permitirá mejorar las condiciones'
         'de trabajo en el campo, la calidad de los productos y su productividad.')



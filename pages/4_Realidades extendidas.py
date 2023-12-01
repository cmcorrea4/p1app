import streamlit as st
from PIL import Image

st.title("Realidades extendidas")

st.write("Añadir a la realidad objetos digitales con Realidad Aumentada(AR), Construir Digitalmente cualquier espacio o elemento imaginado con realidad Virtual (V)R")

image = Image.open("Metaverso.png")
new_image = image.resize((600, 400))
st.image(new_image)

#st.write("Para saber más acerca del proyeto, ingresa en el siguiente link")

link_text = "[Metaverso HUBTRADE](https://www.spatial.io/s/HUB-TRADE-2023-647d18b10551fa0adc8060c5?share=0)"
st.markdown(link_text, unsafe_allow_html=True)

import pandas as pd
import utilidades as util
import streamlit as st
from PIL import Image

#para correr streamlit se ejecuta: streamlit run app.py

#Pagina d epresentación o Index
st.set_page_config(
    page_title="Info liga colombiana",
    initial_sidebar_state="auto",
    layout="wide",
    page_icon="😋"
)

#llamamos la funcion utilidades
util.generarMenu()

#Estructura de presentación
left_col,center_col,right_col=st.columns([1,4,1],vertical_alignment="center")

#Edito la columna central
with center_col:
    
    st.title('Informe de la liga colombiana :blue[2024-2] :smile:')
    st.markdown("<h1 style='text-align: center;'>Informe de la liga colombiana 2024-2</h1>", unsafe_allow_html=True)
    st.write("""
    En este espacio puede mostrar cual fue el desempeño de los equipos de futbol durante el segundo semestre del 2024.
                
             En la pagina informe se pueden ver los datos y su analisis
             """)
    imagen3=Image.open("Media\Liga-betplay.jpg")
    st.image(imagen3,use_container_width=False,width=500,caption="Liga")


with left_col:
    st.title('Informe de la liga colombiana :blue[2024-2] :smile:')
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns
import utilidades as util
import numpy as np

#Configuramos encabezados de pagina
st.set_page_config(
    page_title="Informe Liga",
    page_icon="👽",
    initial_sidebar_state="expanded",
    layout="centered"
)

util.generarMenu()
#Visualización
st.title("Datos de la liga colombiana 2024")
ruta="Data\DF.csv"
#ruta2="Data\Los Aprendices_ver1_130225_Depurado (1).csv"
df=pd.read_csv(ruta)
#df2=pd.read_csv(ruta2)
titulo1="Cantidad de goles marcados por cada equipo"
#titulo2="Tabla proyecto"
util.mostrartabla(df,titulo1)
#util.mostrartabla(df2,titulo2)
util.grafBarras(df)

plt.hist('SEXO')
st.pyplot(plt)


import pandas as pd
import streamlit as st
from PIL import Image
from matplotlib import pyplot as plt
import seaborn as sns

#Crear barra lateral
def generarMenu():
    with st.sidebar:
        col1,col2=st.columns(2)
        with col1:
            imagen=Image.open("Media\Torneobetplay.jpeg")
            st.image(imagen,use_container_width=False,width=120)
            st.header("Torneo BetPlay 2024")
        with col2:
            st.header("Liga BetPlay 2024")
            imagen=Image.open("Media\Ligabetplay.png")
            st.image(imagen,use_container_width=False,width=120)
        st.page_link("app.py",label="Home",icon='🏠')
        st.page_link("Pages/informe.py",label="Informe",icon="📃")

def mostrartabla(df,titulo):
    df2=pd.DataFrame(df)
    #Configuramos columnas
    col1,col2,col3=st.columns([0.5,5,0.5],
                            vertical_alignment="top"
                            )
    with col2:
        st.markdown(titulo)
        df2.set_index("CENTRO_ATENCION",inplace=True)
        st.write(df2.head(100),unsafe_allow_html=False)
        
def grafBarras(df): 
    df2=pd.DataFrame(df)
    st.markdown("Grafico de barras")
    sns.set_style("whitegrid")
    total= df2.groupby("NOMBRE_BARRIO")[['EDAD']].mean()
    Edades=pd.DataFrame(total)
    #Edades['AÑO_MES']=pd.DataFrame(df2["AÑO_MES"] )
    Edades =Edades.reset_index()
    resultado = Edades.groupby(['NOMBRE_BARRIO']).mean()
    resultado.plot(kind='bar',figsize=(10,10))
    plt.tight_layout()
    plt.show()
    st.pyplot(plt)
    mostrartabla(Edades,"Edades")


def grafSandBox(df):
    df2=pd.DataFrame(df)
    st.markdown("Grafico de barras")
    sns.set_style("whitegrid")
    total= df2.groupby("CENTRO_ATENCION")[['EDAD']].mean()
    Edades=pd.DataFrame(total)
    #Edades['AÑO_MES']=pd.DataFrame(df2["AÑO_MES"] )
    Edades =Edades.reset_index()
    resultado = Edades.groupby(['CENTRO_ATENCION']).mean()
    resultado.plot(kind='box',figsize=(10,10))
    plt.tight_layout()
    plt.show()
    st.pyplot(plt)
    mostrartabla(Edades,"Edades")




import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

#-----------------------------------------------SETUP-------------------------------------------------#

st.set_page_config(page_title='titanic project', layout='wide', initial_sidebar_state='auto')

st.sidebar.title('Menu')

# Obtener el directorio actual del archivo
current_directory = os.path.dirname(__file__)
data_path = os.path.join(current_directory, '../data/titanic_train2.csv')
df_original = pd.read_csv(data_path)

#-----------------------------------------------CONFIG-------------------------------------------------#

st.image('img/header4.png', use_column_width=True)

col1, col2 = st.columns(2)


with col1:
    st.write("")
    st.subheader('Objetivo del proyecto')
    st.write("""
        Analizar el dataset y sacar las respectivas conclusiones, utilizando las técnicas aprendidas:
    """)
    st.markdown("""
    - Descarga de datos
    - Limpieza y preprocesamiento de datos
    - Análisis Exploratorio de Datos (EDA)
    - Visualización de gráficos. 
    - Conclusiones. 
    """)


with col2:
    st.write("")
    st.subheader('Resultado final')
    st.markdown("""
    - Análisis de la tasa de supervivencia por variable.
    - La Influencia de la Clase Social: Reevaluando el principio de "Primero mujeres y niños".
    - Modelo predictivo de supervivencia.
    """)


# Puedes agregar un margen o estilo extra si deseas
st.markdown("""
    <style>
        .margin {
            margin-top: 20px;
        }
    </style>
    <div class="margin"></div>
""", unsafe_allow_html=True)



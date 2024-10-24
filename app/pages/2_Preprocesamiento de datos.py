import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os


df = pd.read_csv('data/df_imputed2.csv')

#-----------------------------------------------SETUP-------------------------------------------------#



st.image('img/preprocesamiento1.png', use_column_width=True)

st.subheader('Valores Nulos')
st.markdown("""
- <span style='color:yellow'>Sustitución por moda</span>: Embarked. Solo hay 2 nulos. Los reemplazamos con la moda, ya que Southampton es, con mucha diferencia, el más común.

- <span style='color:yellow'>Método KNN</span>. Age. Reemplazamos los valores nulos con el método KNN.

- <span style='color:yellow'>Agrupación de datos</span>. Cabin. Agrupamos los datos en una nueva variable llamada Type of Cabin para valorar opciones. Finalmente, eliminaremos la variable Cabin ya que el porcentaje de nulos es muy alto
""", unsafe_allow_html=True)

st.subheader('Nuevas variables')
st.markdown("""
- <span style='color:yellow'>FamilyGroup</span>: Unimos SibSp y Parch en una sola columna para entender los grupos familiares como uno solo.
- <span style='color:yellow'>AgeGroup</span>: Creamos rangos de edad para una mejor visualización. Crearé esta nueva variable después de reemplazar los valores nulos.
- <span style='color:yellow'>Title</span>: Obtener los títulos de los pasajeros a partir de sus nombres.
- <span style='color:yellow'>Type of Ticket</span>.
""", unsafe_allow_html=True)

st.subheader('Eliminación de Variables')
st.markdown("""
- PassengerID.
- SibSp y Parch
- Cabin
- Ticket
- Name
""")


st.subheader('El nuevo dataframe')
st.dataframe(df)


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os


df = pd.read_csv('data/titanic_train2.csv')

#-----------------------------------------------SETUP-------------------------------------------------#

st.subheader('Dataset original')

st.markdown("""
Dataframe sobre pasajeros del Titanic. 

**Fuente** : Dataset Proyecto Titanic de Kaggle. Proporcionada por Upgrade Hub.

""")

st.subheader('Representación de la muestra')

st.write('La muestra representa un 40% del total de viajeros, por lo que si que puede considerarse una buena muestra para la toma de conclusiones. Contamos con una serie de variables para poder analizar')
st.write('Tamaño del dataset: 891 filas y 12 columnas')
st.subheader('Variables')
st.markdown("""
- PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp: Número de hermanos y cónyuges a bordo
- Parch: Número de padres e hijos a bordo
- Ticket: 
- Fare: Precio del billete
- Cabin
- Embarked: Puerto de embarque siendo S=Southampton, C=Cherbourg, Q=Queenstown
""")

st.subheader('Dataset Original')
st.dataframe(df)
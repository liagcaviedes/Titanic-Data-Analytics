import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
import matplotlib.pyplot as plt



df = pd.read_csv('data/titanic_train2.csv')



#-----------------------------------------------GRAFICO -------------------------------------------------#

categories = ['Pasajeros totales', '1st', '2nd', '3rd', 'Tripulantes', 'Mascotas', 'Mascotas dueño superviviente']
total = [2224, 324, 284, 709, 885, 12, 8]
deaths = [1513, 122, 166, 531, 671, 9, 5]
survival_rate = [31.94, 62.35, 41.55, 25.11, 24.18, 25.00, 38.00]


#-----------------------------------------------SETUP-------------------------------------------------#

st.header('¿Quién viajaba en el Titanic?')

tab1, tab2, tab3 = st.tabs(["Contexto", "Pasajeros", "Comparativa"])
with tab1:

    st.image('img/overgreen.png')
with tab2:
    st.subheader('¿Quién más viajaba en el Titanic?')
    st.markdown("""
- 12 perros
- Gatos
- Pájaros, gallos y gallinas
""")

    st.image('img/perros_titanic.png')
    
    st.write('12 perros de pasajeros de primera clase, algunos de ellos viajaban en bodega, otros en los camarotes con sus dueños')
    
    st.image('img/gato.png')
    
    st.write('Como era comun en la época, en los barcos viajaban gatos para ahuyentar roedores. Además, el Titanic tenia una mascota, llamada Jenny')
    
    st.image('img/perros supervivientes.png')
    
    st.write('Estos tres perros sobrevivieron al hundimiento, todos de la mano de sus dueños de primera clase')       
    st.image('img/anthoy.png')
    
    st.write('Hubo heroes, como John Jacob Astor IV, que murieron salvando la vida de su perro. En la foto le vemos con Kitty. Se dice que Jacob, dejó a su mujer a salvo, rechazando su propio sitio en un bote salvavidas para ir a buscar a Kitty y que fue la persona que liberó a todos los perros de la bodega durante el hundimiento ')
    

with tab3:
    st.image('img/supervivenciagreen.png')
    


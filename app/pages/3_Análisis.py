import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#-----------------------------------------------SETUP--------------------------------------------------------#

st.set_page_config(page_title='titanic project', layout='wide', initial_sidebar_state='auto')

st.title('El impacto de la clase social en la supervivencia del Titanic')
st.subheader('Desmontando el mito de "Mujeres y niños primero"')

st.sidebar.title('menu app')
df_imputed = pd.read_csv('data/df_imputed2.csv')


#------------------------------------ FORMULA PARA GRAFICO COMBINADO DE VARIABLES-------------------------------# 


def plot_combo_chart(column, df_imputed):
    survived = df_imputed[df_imputed['Survived'] == 1][column].value_counts()
    dead = df_imputed[df_imputed['Survived'] == 0][column].value_counts()

    combined_df = pd.DataFrame({'Survived': survived, 'Dead': dead})
    
    combined_df = combined_df.fillna(0)
    
    combined_df['Total'] = combined_df['Survived'] + combined_df['Dead']
    combined_df['Survival Rate (%)'] = (combined_df['Survived'] / combined_df['Total']) * 100
    

    fig = go.Figure()


    fig.add_trace(go.Bar(
        x=combined_df.index,
        y=combined_df['Survived'],
        name='Survived',
        marker_color='#275921'
    ))

    fig.add_trace(go.Bar(
        x=combined_df.index,
        y=combined_df['Dead'],
        name='Dead',
        marker_color='#b3b3b3'
    ))

    fig.add_trace(go.Scatter(
        x=combined_df.index,
        y=combined_df['Survival Rate (%)'],
        name='Survival Rate (%)',
        mode='lines+markers+text',  
        text=[f'{rate:.1f}%' for rate in combined_df['Survival Rate (%)']],  
        textposition='top center',  
        marker=dict(color='#439e39'),
        yaxis='y2'  
    ))


    fig.update_layout(
        yaxis_title='Count',
        yaxis2=dict(
            title='Survival Rate (%)',
            overlaying='y', 
            side='right',
            range=[0, 100]  
        ),
        barmode='stack', 
        legend=dict(x=0.01, y=0.99),
        height=600,
        width=800
    )
    
    st.plotly_chart(fig)



#-----------------------------------------------SURVIVAL RATE POR VARIABLE-------------------------------------------------#

# Crear las pestañas principales
tab1, tab2 = st.tabs(["Por Variable", "Correlación",])


#-----------------------------------------------tab1-------------------------------------------------#
with tab1:

    subtab1, subtab2, subtab3, subtab4, subtab5 = st.tabs(['Clase', 'Sexo', 'Edad', 'FamilyGroup', 'Puerto de embarque'])
    
#-----------------------------------------------subtab1-------------------------------------------------#

    with subtab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader('Clase Social')
            plot_combo_chart('Pclass', df_imputed)
        
        with col2:
            st.subheader('Comentarios:')
            st.markdown("""
                        
- Grandes diferencias entre los tipos de clase. 
- POSH en inglés: Port Out, Starboard Home. 
- Además de su status social, los pasajeros de 1st y 2nd class viajaban en la parte superior del barco, mientras que la 3rd class viajaba en la parte inferior.
- Tuvieron además información más rapida de la situación y acceso a los botes salvavidas.
- Veamos el impacto de la clase social con cada una de las variables. 
- Vamos a ver el impacto 
- POSH en inglés: Port Out, Starboard Home. 

""")   
#-----------------------------------------------subtab2-------------------------------------------------#
    with subtab2:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader('Sexo')
            plot_combo_chart('Sex', df_imputed)
            st.subheader('Sexo Vs Clase')
            st.image('img/Sexvsclaseblack.png', width=700)
            st.subheader('Mujeres por rango de edad')
            st.image('img/mujeresedad2.png', width=700)
        
        with col2:
            st.subheader('Comentarios:')
            st.write("")
            st.write("")
            st.write("")
            st.markdown("""
- La tasa de supervivencia de las mujeres es mucho mayor que la de los hombres.
- Puede darnos a entender que se siguió la norma de "Mujeres y niños primero"
- Solo el 19% de los hombres sobrevivieron.
""")
            st.write("")  
            st.write("") 
            st.write("")  
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            st.subheader('Sexo Vs Clase')
            st.markdown("""
- MUJERES: 
    - Casi la totalidad de mujeres de primera y segunda clase sobrevivieron
    - Solo el 50% de las mujeres de tercera clase sobrevivieron

- HOMBRES: 
    - Aquí, aunque el porcentaje es mucho menor con respecto a mujeres, tambien se ve la diferencia de clases
    
- RESUMEN
    - Mujeres primero si, pero dependiendo de su estatus social.
""")
            st.write("")  
            st.write("") 
            st.write("")  
            st.write("")
            st.write("")
            st.write("")
            st.subheader('Mujeres por edad')
            st.markdown("""
- Centrandonos en las mujeres, el rango de edad de primera clase es mayor y tambien la edad de supervivencia. 

""")
#-----------------------------------------------subtab3-------------------------------------------------#
    with subtab3:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader('Grupos de Edad')
            plot_combo_chart('AgeGroup', df_imputed)
            st.subheader('Niños y Clases Sociales')
            st.image('img/nensyclases.png', width=700)
        
        with col2:
            st.subheader('Grupos de Edad:')
            st.markdown("""
                        
- Grupos de Edad: 
    - Child: De 0 a 10 años

    - Teen: de 10 a 18 años.

    - Adult: de 18 a 30 años.

    - Middle-Age: De 30 a 50 años. 

    - Senior: +50 años. 

- Comentarios: 
    - Los niños y adolescentes tuvieron una tasa de supervivencia más alta que los adultos.
    - Aquí también podriamos pensar en la norma de "Mujeres y niños primero".
""")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.subheader('Niños y Clase Social')
            st.markdown("""
                        
- Si unimos la variable edad a la clase social, vemos claramente que los niños y adolescentes de primera clase tuvieron una tasa de supervivencia mayor.
""")
#-----------------------------------------------subtab4-------------------------------------------------#       
    with subtab4:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader('Grupos Familiares')
            plot_combo_chart('FamilyGroup', df_imputed)
            st.subheader('Grupos Familiares y Clases Sociales')
            st.image('img/familyvsclase.png')
        
        with col2:
            st.subheader('Grupos Familiares:')
            st.markdown("""

- La lógica nos diría que los pasajeros solos tendrían mas posibilidades de sobrevivir, al no tener que esperar a sus familiares. 
- Por la época podemos deducir que era hombres en su mayoría los que viajaban solos, buscando trabajo en América.
- Esta variable aislada no es concluyente.                      
""")
#-----------------------------------------------subtab5-------------------------------------------------#
    with subtab5:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader('Puertos de Embarque')
            plot_combo_chart('Embarked', df_imputed)
            st.subheader('Puertos de Embarque y Clases Sociales')
            st.image('img/embarkedclass.png')
        
        with col2:
            st.subheader('Puertos de Embarque:')
            st.markdown("""
                        
                        
- S: Southampton

- C: Cherbourg

- Q: Queenstown

""")
            
#------------------------------------------TAB2-------------------------------------------------#            

with tab2:
    st.subheader('Correlación entre variables')
    col1, col2 = st.columns([2, 1])
        
    with col1:
        st.image('img/corrmatrix.png')
        
    with col2:
        st.subheader('Correlación entre variables:')
        st.markdown("""
- No hay correlaciones fuertes entre las variables. 
- Sex sería la variable con mayor correlación con la supervivencia, pero hemos visto que depende de la clase social.
""")
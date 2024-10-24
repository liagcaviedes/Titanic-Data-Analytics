import streamlit as st
from pycaret.classification import load_model, predict_model
import pandas as pd
import os

# Definir la ruta del modelo
model_path = os.path.join('model', 'ada_model')  # Asegúrate de que la ruta sea correcta

# Intentar cargar el modelo y manejar errores
try:
    if os.path.exists(model_path + '.pkl'):
        model = load_model(model_path)
        st.sidebar.success('Modelo cargado correctamente.')
    else:
        st.sidebar.error(f'Error: El archivo no se encuentra en la ruta {model_path}.pkl')
except Exception as e:
    st.sidebar.error(f'Error al cargar el modelo: {e}')

# Carga del dataset
try:
    df = pd.read_csv('data/df_imputed2.csv')
    st.sidebar.success('Dataset cargado correctamente.')
except FileNotFoundError:
    st.sidebar.error('No se encontró el dataset. Verifica la ruta.')
    df = pd.DataFrame()  # Crear un dataframe vacío para evitar errores posteriores

# Configuración de la app
st.title('Predicción de Supervivencia del Titanic ⛴️')
st.write('En esta aplicación puedes predecir si una persona habría sobrevivido al desastre del Titanic utilizando un modelo de machine learning entrenado con datos históricos.')
st.markdown("""
- Modelo Utilizado: AdaBoost Classifier entrenado con el dataset del Titanic. 
- Accuracy: 82.5%.

""")

# Formulario de predicción en la página principal
st.subheader('🔮 Predicción de Datos')

# Verificar si el dataframe tiene datos y el modelo está definido
if not df.empty and 'model' in locals():
    with st.form(key='unique_prediction_form'):
        # Entradas del usuario basadas en las columnas requeridas
        Pclass = st.selectbox('Pclass', options=df['Pclass'].unique())
        Sex = st.selectbox('Sex', options=df['Sex'].unique())
        Age = st.number_input('Age', min_value=0, max_value=100, step=1, value=30)
        Embarked = st.selectbox('Embarked', options=df['Embarked'].unique())  # Asegúrate de que exista
        
        # Botón de envío
        submit_button = st.form_submit_button(label='Enviar')

    # Procesar la predicción si se hace clic en el botón
    if submit_button:
        input_data = pd.DataFrame({
            'Pclass': [Pclass],
            'Sex': [Sex],
            'Age': [Age],
            'Embarked': [Embarked],
        })

        # Realizar la predicción
        try:
            prediction = predict_model(model, data=input_data)

            # Usar la columna "prediction_label" como "Survived" y mostrar el resultado con un mensaje
            if 'prediction_label' in prediction.columns and 'prediction_score' in prediction.columns:
                survived = prediction['prediction_label'][0]  # 0 o 1
                score = prediction['prediction_score'][0]     # Score de la predicción

                # Mostrar el resultado
                if survived == 1:
                    st.success(f"🔵 Según este modelo predictivo, **esta persona sobrevivió**. "
                               f"El modelo tiene un score de **{score:.2f}** para esta predicción.")
                else:
                    st.warning(f"🔴 Según este modelo predictivo, **esta persona no sobrevivió**. "
                               f"El modelo tiene un score de **{score:.2f}** para esta predicción.")

            else:
                st.error('❌ No se encontraron las columnas "prediction_label" o "prediction_score".')

        except ValueError as e:
            st.error(f'Error al realizar la predicción: {e}.')
            st.info('Verifica que las columnas categóricas estén correctamente procesadas.')
else:
    if not df.empty:
        st.error('❌ El modelo no está disponible. No se puede completar la predicción.')




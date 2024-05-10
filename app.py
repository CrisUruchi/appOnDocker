import streamlit as st
import joblib

# Cargar el modelo entrenado
modelo = joblib.load('modelo_entrenado.pkl')

st.title('Interfaz de Predicción')

#normaliza los datos de Saturacion y Brillo
def escalar_datos(brillo, saturacion):
    # rango brillo y saturación
    brillo_min, brillo_max = 10, 70
    saturacion_min, saturacion_max = 10, 90

    # brillo y saturación normalizado
    brillo_esc = (brillo - brillo_min)/(brillo_max - brillo_min)
    saturacion_esc = (saturacion - saturacion_min)/(saturacion_max - saturacion_min)

    return brillo_esc, saturacion_esc


#define el color de salida dependiendo de la prediccion
def etiqueta_prediccion(prediccion):
    if prediccion == 0:
        return "Rojo"
    elif prediccion == 1:
        return "Azul"
    else:
        return "Etiqueta no reconocida"

# campos de entrada para los parámetros
brillo = st.number_input('Brillo:', min_value=10, max_value=70, step=1, value=40)
saturacion = st.number_input('Saturación:', min_value=10, max_value=90, step=1, value=20)

# Agregar un botón para realizar la predicción
if st.button('Realizar Predicción'):
    # Escalar los datos
    brillo_esc, saturacion_esc = escalar_datos(brillo, saturacion)
    # predicción
    resultado_prediccion = modelo.predict([[brillo_esc, saturacion_esc]])
    # etiqueta
    etiqueta_resultado = etiqueta_prediccion(resultado_prediccion[0])
    # Mostrar el resultado de la predicción
    st.write(f'Color predicho: {etiqueta_resultado}')
    st.write(f'datos: {brillo_esc}, {saturacion_esc},{etiqueta_resultado}')
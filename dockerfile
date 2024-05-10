# Python como base
FROM python:3.11.4

# carpeta /app
WORKDIR /app

# Copia los archivos de la aplicación a carpeta
COPY app.py modelo_entrenado.pkl /app/

# Instala las dependencias de la aplicación
RUN pip install streamlit joblib scikit-learn

# Exponer el puerto 8501 para Streamlit
#EXPOSE 8501

# Ejecutar la aplicación cuando se inicie el contenedor
CMD ["streamlit", "run", "app.py"]
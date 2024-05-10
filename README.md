Ejemplo simple de la dockerizacion de un proyecto de ML
1. El modelo es entrenado en el archivo M14T3.ipynb
2. El dataset utilizado es super reducido.
3. Se exporta el modelo para ser utilizado en la interfaz llamada app.py
4. La interfaz esta hecha en streamlit, llama al modelo y muestra la respuesta.
   Para poderlo probar antes de dockerizarlo, se debe ejecutar asi:
   streamlit run app.py
6. El archivo dockerfile tiene las librerias necesarias para que el modelo funcione.
7. la imagen se encuentra en https://hub.docker.com/repository/docker/crisuruchi/repocris/tags
8. Me divertí con esta práctica :D

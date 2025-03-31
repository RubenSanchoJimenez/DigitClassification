import streamlit as st
from PIL import Image
import numpy as np
import cv2
import pickle
from streamlit_drawable_canvas import st_canvas

# Configuración de la página
st.set_page_config(page_title="Clasificador de Dígitos con SVM", page_icon="💯", layout="wide")
st.title("💯 Clasificador de Dígitos con SVM")

# Estilos personalizados
st.markdown(
    """
    <style>
    .big-header {
        font-size: 36px;
        font-weight: bold;
        color: #4B0082;
        text-align: center;
        margin-top: 20px;
    }
    .section-title {
        font-size: 24px;
        color: #006400;
        margin-top: 30px;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .info-box {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4B0082;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Explicación de la actividad
st.write("""
En esta actividad, desarrollarás una aplicación interactiva que permite:
✅ Dibujar un número manuscrito.
✅ Subir una imagen con un número.
✅ Obtener la predicción de un modelo entrenado mediante **SVM**.
""")

st.markdown("<div class='section-title'>📂 Archivos proporcionados</div>", unsafe_allow_html=True)
st.markdown("""
- `svm_digits_model.pkl`: Contiene el modelo SVM y el `StandardScaler`.
- Base de código de la aplicación.
""")

# Sección de implementación
st.markdown("<div class='section-title'>🛠️ Implementación</div>", unsafe_allow_html=True)
st.markdown("#### 1️⃣ Interfaz con Streamlit")
st.write("""
- Un **lienzo interactivo** para dibujar un número.
- Un **botón para predecir** el número dibujado.
- Un **cargador de imágenes** para hacer predicciones con archivos JPG o PNG.
""")

st.markdown("#### 2️⃣ Preprocesamiento de imágenes")
st.write("""
Para que el modelo pueda interpretar la imagen, se debe:
🔹 Convertir la imagen a **escala de grises**.
🔹 Redimensionarla a **8x8 píxeles**.
🔹 Escalar los valores de color a **0-16**.
🔹 Normalizar con `StandardScaler`.
""")

with st.expander("ℹ️ ¿Por qué 8x8 y valores de 0 a 16?"):
    st.write("""
    El modelo fue entrenado con imágenes de **8x8 píxeles** del dataset `digits` de Scikit-learn.
    Los valores de los píxeles deben estar entre **0 y 16** para ser correctamente interpretados.
    """)

st.markdown("#### 3️⃣ Predicción con SVM")
st.write("""
📌 Una vez preprocesada la imagen, el modelo realiza la predicción del número manuscrito.
El archivo `.pkl` contiene:
- **El modelo SVM (`clf`)**.
- **El `scaler` para transformar las imágenes**.
""")

st.markdown("<div class='section-title'>📌 Requisitos técnicos</div>", unsafe_allow_html=True)
st.code("pip install streamlit numpy pillow opencv-python matplotlib scikit-learn streamlit-drawable-canvas", language="bash")

st.markdown("<div class='section-title'>💡 Recomendaciones</div>", unsafe_allow_html=True)
st.write("""
✅ Organiza tu código en funciones.
✅ Controla errores si no hay imagen.
✅ Muestra el resultado de forma clara.
✅ Comenta el código para explicar cada paso.
""")

st.markdown("<div class='section-title'>🏆 Criterios de evaluación</div>", unsafe_allow_html=True)
st.markdown("""
| Criterio                                      | Puntos |
|----------------------------------------------|--------|
| Interfaz funcional y clara                    | 2.0    |
| Preprocesamiento correcto de imágenes         | 2.5    |
| Uso correcto del modelo SVM                   | 2.5    |
| Manejo de errores y funcionalidades extra     | 1.5    |
| Claridad del código y buenas prácticas        | 1.5    |
| **Total**                                     | **10** |
""")

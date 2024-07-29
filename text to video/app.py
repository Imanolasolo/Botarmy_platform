import streamlit as st
from gtts import gTTS
import os

# Función para generar el archivo de audio
def text_to_audio(text, lang='es'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")

st.title("Texto a Audio con Streamlit")

# Entrada de texto
user_text = st.text_area("Escribe el texto que deseas convertir a audio:")

# Botón para generar el audio
if st.button("Generar Audio"):
    if user_text:
        text_to_audio(user_text)
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
        st.success("¡El audio ha sido generado con éxito!")
    else:
        st.error("Por favor, escribe algo de texto.")

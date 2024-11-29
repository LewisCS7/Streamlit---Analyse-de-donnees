import streamlit as st
import pandas as pd

st.title("Application Multi-Pages avec Streamlit")

# Initialiser une variable dans la session si elle n'existe pas
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
    st.session_state.data = None

st.write("Bienvenue dans l'application multi-pages.")
st.write("Téléversez un fichier CSV pour commencer à explorer les données.")

uploaded_file = st.file_uploader("Téléversez un fichier CSV", type=["csv"])

if uploaded_file:
    # Charger le fichier dans la session
    st.session_state.uploaded_file = uploaded_file
    st.session_state.data = pd.read_csv(uploaded_file)
    st.success("Fichier téléversé avec succès!")
else:
    st.warning("Aucun fichier téléversé, veuillez téléversez un fichier pour activer les fonctionnalités des pages.")

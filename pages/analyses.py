import streamlit as st

st.title("Analyse des Données")

# Vérifier si un fichier a été téléversé
if st.session_state.uploaded_file:
    data = st.session_state.data

    st.write("Aperçu des données :")
    st.dataframe(data)

    st.write("Statistiques descriptives :")
    st.write(data.describe())
else:
    st.error("Aucun fichier téléversé. Veuillez revenir à la page principale pour téléverser un fichier.")

import streamlit as st

st.title("Graphiques des Données")

# Vérifier si un fichier a été téléversé
if st.session_state.uploaded_file:
    data = st.session_state.data

    st.write("Sélectionnez les colonnes à afficher :")
    
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_columns) >= 2:
        col1 = st.selectbox("Sélectionnez la première colonne :", numeric_columns, index=0)
        col2 = st.selectbox("Sélectionnez la deuxième colonne :", numeric_columns, index=1)
        
        # Graphique avec deux colonnes
        graph_data = data[[col1, col2]].dropna()
        st.line_chart(graph_data)
    else:
        st.warning("Pas assez de colonnes numériques pour afficher un graphique.")
else:
    st.error("Aucun fichier téléversé. Veuillez revenir à la page principale pour téléverser un fichier.")

import streamlit as st  # Streamlit pour l'interface web
from app.doc_reader import detect_type_and_extract  # Extraction du texte
from app.ner import detecter_entites  # Détection d'entités
from app.anonymiser import anonymiser_texte  # Anonymisation

def afficher_interface():
    st.set_page_config(page_title="DocAnon", page_icon="🕵️", layout="centered")
    st.title("🕵️ DocAnon - Anonymisation intelligente de documents")

    # Upload d’un fichier PDF ou Word
    fichier = st.file_uploader("📁 Déposez un fichier (.pdf ou .docx)", type=["pdf", "docx"])

    if fichier:
        st.info("🔍 Extraction du texte en cours...")
        texte = detect_type_and_extract(fichier)

        if not texte.strip():
            st.error("Aucun texte détecté.")
            return

        # Affiche le texte brut
        st.subheader("📄 Texte extrait")
        st.text_area("Texte brut", texte, height=300)

        # Détection des entités et anonymisation
        entites = detecter_entites(texte)
        texte_anonyme = anonymiser_texte(texte, entites)

        # Affiche le texte anonymisé
        st.subheader("🔒 Texte anonymisé")
        st.text_area("Texte anonymisé", texte_anonyme, height=300)

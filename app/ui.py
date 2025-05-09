# app/ui.py

import streamlit as st
from app.ocr import extraire_texte
from app.ner import detecter_entites
from app.anonymiser import anonymiser_texte

def afficher_interface():
    st.set_page_config(page_title="DocAnon – Anonymisation OCR", layout="wide")
    st.title("🔐 DocAnon — Anonymiseur intelligent de documents")

    fichier = st.file_uploader("📄 Déposez un fichier PDF ou une image", type=["pdf", "png", "jpg", "jpeg"])

    if fichier:
        texte = extraire_texte(fichier)
        st.subheader("1. Texte extrait (OCR)")
        st.text_area("Texte brut :", texte, height=200)

        st.subheader("2. Entités détectées")
        entites = detecter_entites(texte)

        if entites:
            for ent, label in entites:
                st.write(f"🔹 `{ent}` → {label}")
        else:
            st.warning("Aucune entité détectée.")

        st.subheader("3. Anonymisation automatique")
        texte_anonymise = anonymiser_texte(texte, entites)

        st.text_area("Texte anonymisé :", texte_anonymise, height=200)

        st.download_button(
            label="📥 Télécharger le texte anonymisé",
            data=texte_anonymise,
            file_name="document_anonymise.txt",
            mime="text/plain"
        )

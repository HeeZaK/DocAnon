import streamlit as st
from app.doc_reader import detect_type_and_extract
from app.anonymisation import detect_entities_with_offsets, anonymiser_texte

def highlight_entities(text, entities):
    """
    Surligne les entités détectées dans le texte avec une couleur.
    """
    sorted_ents = sorted(entities, key=lambda x: x[1])  # Tri par position
    result = ""
    last_idx = 0
    for label, start, end in sorted_ents:
        result += text[last_idx:start]
        result += f'<span style="background-color: #ffd54f; font-weight:bold;" title="{label}">{text[start:end]}</span>'
        last_idx = end
    result += text[last_idx:]
    return result

def afficher_interface():
    st.set_page_config(page_title="DocAnon", layout="wide")
    st.title("🕵️ DocAnon - Anonymisation de documents")

    uploaded_file = st.file_uploader("📄 Déposez un fichier (PDF ou DOCX)", type=["pdf", "docx"])

    if uploaded_file:
        texte = detect_type_and_extract(uploaded_file)

        if texte.strip():
            st.subheader("🔍 Aperçu des entités détectées")
            entities = detect_entities_with_offsets(texte)
            html_text = highlight_entities(texte, entities)
            st.markdown(html_text, unsafe_allow_html=True)

            st.subheader("📝 Modifier le texte (si besoin)")
            user_text = st.text_area("Texte à anonymiser", value=texte, height=300)

            if st.button("Anonymiser le texte validé"):
                texte_anonyme = anonymiser_texte(user_text)
                st.subheader("✅ Résultat anonymisé")
                st.text_area("Texte anonymisé", value=texte_anonyme, height=300)
        else:
            st.warning("❌ Le texte n'a pas pu être extrait du fichier.")

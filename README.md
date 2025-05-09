# 🕵️ DocAnon

DocAnon est une application Streamlit permettant d'extraire et d'anonymiser automatiquement des documents PDF et Word (DOCX). Elle est conçue pour les professionnels du droit, de l'immobilier et de la conformité.

## ✅ Fonctionnalités

- Téléversement de fichiers PDF ou DOCX
- Extraction du texte (OCR si besoin)
- Détection automatique des entités (nom, date, email, téléphone…)
- Mise en surbrillance des données sensibles
- Edition manuelle du texte par l'utilisateur
- Anonymisation automatique

## 🚀 Exécution locale

```bash
pip install -r requirements.txt
python -m spacy download fr_core_news_sm
streamlit run main.py

# 🕵️‍♂️ DocAnon – Anonymisation de documents juridiques

DocAnon est une application web qui permet d'analyser et d'anonymiser des documents PDF ou DOCX à l'aide de l'IA (spaCy + OCR). Elle s’adresse aux notaires, avocats, agents immobiliers, etc.

---

## 🚀 Lancer l'application

👉 Cliquez ici pour utiliser l’application en ligne : [https://nom-de-ton-app.streamlit.app]

## ⚙️ Fonctionnalités

- 📄 Téléversement de documents PDF ou Word
- 🔍 Extraction du texte même depuis des PDF scannés (OCR)
- 🤖 Détection automatique des entités (noms, adresses, numéros, etc.)
- 🫥 Anonymisation en un clic
- 💾 Export du document anonymisé

---

## 🧠 Technologies

- Python 3.10
- Streamlit
- spaCy (modèle `fr_core_news_md`)
- pdf2image + pytesseract (pour les PDF scannés)
- python-docx

---

## 👩‍💼 Public cible

Notaires, avocats, agences immobilières, directions juridiques, collectivités...

---

## 📦 Déploiement (développeurs)

Pour exécuter en local :
```bash
git clone https://github.com/ton-compte/docanon.git
cd docanon
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run main.py

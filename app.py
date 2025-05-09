import gradio as gr
from app.doc_reader import detect_type_and_extract
from app.anonymisation import detect_entities_with_offsets, anonymiser_texte

def process_file(file):
    if file is None:
        return "", "", ""
    
    texte = detect_type_and_extract(file)
    entities = detect_entities_with_offsets(texte)

    # Surlignage HTML
    highlighted = ""
    last_idx = 0
    for label, start, end in sorted(entities, key=lambda x: x[1]):
        highlighted += texte[last_idx:start]
        highlighted += f'<span style="background-color: #ffd54f;" title="{label}">{texte[start:end]}</span>'
        last_idx = end
    highlighted += texte[last_idx:]

    return texte, highlighted, anonymiser_texte(texte)

with gr.Blocks() as demo:
    gr.Markdown("## 🕵️ DocAnon - Anonymisation de documents")

    with gr.Row():
        input_file = gr.File(label="📄 Charger un fichier PDF ou DOCX")
    
    with gr.Row():
        raw_text = gr.Textbox(label="📝 Texte extrait", lines=10)
        highlighted_text = gr.HTML(label="🔍 Entités détectées")
        anonymized_text = gr.Textbox(label="✅ Texte anonymisé", lines=10)

    input_file.change(fn=process_file, inputs=input_file, outputs=[raw_text, highlighted_text, anonymized_text])

demo.launch()

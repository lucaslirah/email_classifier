import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import pdfplumber
from utils import preprocess_text
import google.generativeai as genai

load_dotenv()


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def extract_text_from_pdf(file_path):
    """
    Esta função extrai o texto de um arquivo PDF.

    Args:
        file_path (str): Caminho para o arquivo PDF.


    Returns:
        str: Texto extraído do PDF.
    """
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def extract_text_from_txt(file_path):
    """
    Esta função extrai o texto de um arquivo TXT.

    Args:
        file_path (str): Caminho para o arquivo TXT.


    Returns:
        str: Texto extraído do TXT.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_email():
    email_text = request.form.get('email_text', '').strip()
    file = request.files.get('file')

    if file and file.filename != '':
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        if file.filename.endswith('.pdf'):
            email_text = extract_text_from_pdf(file_path)
        elif file.filename.endswith('.txt'):
            email_text = extract_text_from_txt(file_path)
        else:
            return "Formato de arquivo não suportado."

    if not email_text:
        return "Nenhum conteúdo de email foi fornecido."

    # Aqui vamos aplicar NLP e AI depois
    # Chamar a função de pré-processamento
    email_text = preprocess_text(email_text)
    ai_response = classify_and_respond(email_text)

    return render_template("result.html", original=email_text, response=ai_response)

    # return f"<h2>Texto extraído:</h2><p>{email_text}</p>", email_text


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def classify_and_respond(text):
    prompt = f"""
    Você é um assistente que classifica emails como 'Produtivo' ou 'Improdutivo' em um contexto de trabalho e sugere uma resposta automática.
    Considere como Emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema).
    Considere como improdutivos Emails que não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos).

    Email recebido:
    \"\"\"{text}\"\"\"

    Classifique o email e gere uma resposta automática. Retorne apenas a responsta sugerida.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)

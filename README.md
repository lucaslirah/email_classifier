# 📧 Classificador de Emails com IA

Aplicação web desenvolvida para automatizar a leitura e classificação de emails recebidos por uma empresa do setor financeiro. Utiliza inteligência artificial para identificar se um email é **Produtivo** ou **Improdutivo**, e sugere uma resposta automática adequada.

---

## 🚀 Funcionalidades

- Upload de arquivos `.pdf` ou `.txt`, ou inserção direta de texto
- Classificação automática do conteúdo do email
- Geração de resposta automática com base na categoria
- Interface web simples e intuitiva
- Deploy em nuvem via Render

---

## 🧠 Tecnologias Utilizadas

- **Flask** — Framework web em Python
- **Gemini Flash 1.5** — API de IA para classificação e geração de resposta
- **NLTK** — Processamento de linguagem natural (tokenização, stopwords, lematização)
- **pdfplumber** — Extração de texto de arquivos PDF
- **Render** — Hospedagem da aplicação

---

## 📦 Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/email-classifier.git
   cd email-classifier
   ```
- Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
- Instale as dependências:
pip install -r requirements.txt
- Crie um arquivo .env com sua chave da API:
GOOGLE_API_KEY=sua-chave-aqui
- Execute o app:
python app.py


- Acesse em http://localhost:5000

## 🌐 Deploy
A aplicação está disponível online via Render:
🔗 Acesse aqui
(substitua pelo seu link real)

## 📹 Demonstração em Vídeo
Assista à apresentação completa da solução:
### 🎥 Link para o vídeo no YouTube
(substitua pelo seu link real)

## 📁 Estrutura do Projeto
```
email-classifier/
│
├── app.py
├── requirements.txt
├── render.yaml
├── .env (não incluído no repositório)
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── uploads/
```

## 🧠 Classificação de Emails
- Produtivo: solicitações, dúvidas técnicas, pedidos de atualização
- Improdutivo: mensagens de agradecimento, felicitações, conteúdo irrelevante
A IA analisa o conteúdo e retorna:
- A categoria do email
- Uma resposta automática sugerida

## 📌 Observações
- A chave da API Gemini deve ser obtida via Google AI Studio
- O modelo utilizado é o gemini-1.5-flash
- O projeto foi desenvolvido como parte de um desafio técnico

## 👨‍💻 Autor
Lucas Lira <br>
Desenvolvedor Python | Inteligência Artificial | Soluções Web <br>
[LinkedIn](https://www.linkedin.com/in/lucas-lira-411618119/) • [GitHub](https://github.com/lucaslirah)



# VLibras + Python (Flask Demo)

Este projeto é uma **demonstração simples** de como integrar o **VLibras Widget** em uma aplicação Python usando **Flask**.  
O sistema permite digitar um texto em português, exibir esse texto na página web, e então utilizar o **avatar do VLibras** (Ícaro/Hozana) para traduzir o conteúdo para Libras.

---

## 🚀 Como rodar o projeto

### 1. Pré-requisitos
- Python 3.8+ (testado no Windows 11 e Linux)
- Pip instalado

### 2. Instalação
Clone ou copie os arquivos para uma pasta local e instale as dependências:

```bash
pip install -r requirements.txt
```

### 3. Executar o servidor Flask
```bash
python app.py
```

O servidor estará disponível em:  
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖥️ Uso
1. Abra a aplicação no navegador.  
2. Digite um texto no campo de entrada e clique em **Atualizar texto**.  
3. O texto digitado aparecerá no corpo da página.  
4. Clique no botão flutuante do **VLibras** (no canto direito da tela) e escolha **Traduzir**.  
5. O avatar (Ícaro/Hozana) exibirá os sinais correspondentes em Libras.

---

## 📂 Estrutura do projeto
```
/vlibras-flask-demo
│── app.py                # Código principal Flask
│── requirements.txt      # Dependências Python
│── README.md             # Este arquivo
└── templates/
    └── index.html        # Página HTML com o Widget VLibras
```

---

## 📦 Dependências
- **Flask** → Framework web em Python

---

## 🔗 Referências
- [VLibras - Gov.br](https://www.gov.br/governodigital/pt-br/vlibras)  
- [Documentação do Widget VLibras](https://www.gov.br/governodigital/pt-br/vlibras/desenvolvedores)  

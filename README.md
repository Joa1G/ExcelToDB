# 📦 ExcelToDB – Guia de Instalação e Execução

Este projeto lê uma planilha `.xlsx`, cria uma tabela no MySQL com base na estrutura da planilha e insere os dados automaticamente no banco de dados. O banco é executado em um container Docker.

---

## ✅ Pré-requisitos

Certifique-se de ter os seguintes itens instalados:

- [Docker](https://www.docker.com/)
- Python 3.11+
- pip

---

## 🚀 Passo a passo para rodar o projeto

### 1. Entre no repositório
```bash
cd .../ExcelToDB
```

### 2. Suba o container MySQL com Docker Compose
```bash
docker-compose up -d
```

Isso criará e iniciará um container MySQL com as configurações definidas no arquivo `docker-compose.yml`.

### 3. Crie e ative um ambiente virtual

#### Windows:
```bash
python -m venv venv

.\env\Scripts\activate
```
### 4. Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o script

Após realizar os passos acima, execute:

```bash
python main.py
```

O script irá:
- Conectar ao banco de dados do container MySQL;
- Ler a planilha `./resources/arquivo.xlsx`;
**A planilha deve conter uma coluna de MATRICULA que será o PK do DB**
- Criar a tabela com base na planilha (caso não exista);
- Inserir todos os dados da planilha na tabela.

---

## 🐳 Acesso ao banco de dados

Você pode acessar o banco via [DBeaver](https://dbeaver.io/) ou qualquer cliente MySQL utilizando:

- **Host**: `localhost`
- **Porta**: `3306`
- **Usuário**: `root`
- **Senha**: `123`
- **Database**: `mydatabase`

---

## 🛑 Encerrando o container

Para parar e remover o container:

```bash
docker-compose down
```

---

## 🤖 BotCity

Este projeto pode ser facilmente integrado com BotCity Desktop Automation. Basta envolver o processo no método `action()` do bot.

---

Feito com 💻 por João Gabriel Gomes.

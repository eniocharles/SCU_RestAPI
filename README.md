# 🚀 Sistema de Cadastro de Usuário

Hi guys! 😃 Bem-vindo ao **Sistema de Cadastro de Usuário**, uma API RESTful desenvolvida com Django e Django REST Framework para gerenciar usuários, incluindo autenticação via JWT.

🔗 Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/enio-charles-j-r-694655256/)!

## 🛠️ Tecnologias Utilizadas
- 🐍 Python 3
- 🎯 Django
- 🔗 Django REST Framework (DRF)
- 🗄️ PostgreSQL (ou outro banco de dados relacional)
- 🔑 JWT para autenticação
- 🔒 bcrypt para hashing de senhas

## ✨ Funcionalidades
- ✅ Cadastro de usuários
- 📜 Listagem de usuários
- 🔍 Busca de usuário por ID
- ✏️ Atualização de dados do usuário
- 🗑️ Exclusão de usuário
- 🔐 Autenticação via JWT

## 📥 Instalação

Clone o repositório e instale as dependências:

```bash
# Clone o repositório
git clone https://github.com/eniocharles/SCU_RestAPI
cd SCU_RestAPI

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 🗃️ Configuração do Banco de Dados

Edite o arquivo `settings.py` para configurar o banco de dados desejado. O padrão é SQLite, mas você pode usar PostgreSQL ou MySQL.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Ou outro banco de dados
        'NAME': 'seu_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Aplique as migrações:
```bash
python manage.py migrate
```

Crie um superusuário para acessar o painel administrativo:
```bash
python manage.py createsuperuser
```

## 🚀 Execução

Para iniciar o servidor local:
```bash
python manage.py runserver
```
A API estará disponível em `http://127.0.0.1:8000/`

## 🔗 Endpoints

### **1. Cadastro de Usuário**
**POST /users/**
```json
{
  "nome": "João Silva",
  "email": "joao@example.com",
  "senha": "123456"
}
```
**Resposta:** 201 Created
```json
{
  "id": 1,
  "nome": "João Silva",
  "email": "joao@example.com"
}
```

### **2. Listagem de Usuários**
**GET /users/**
**Resposta:** 200 OK
```json
[
  {
    "id": 1,
    "nome": "João Silva",
    "email": "joao@example.com"
  }
]
```

### **3. Buscar Usuário por ID**
**GET /users/{id}/**
**Resposta:** 200 OK
```json
{
  "id": 1,
  "nome": "João Silva",
  "email": "joao@example.com"
}
```

### **4. Atualizar Usuário**
**PUT /users/{id}/**
```json
{
  "nome": "João da Silva",
  "email": "joao.silva@example.com"
}
```
**Resposta:** 200 OK
```json
{
  "id": 1,
  "nome": "João da Silva",
  "email": "joao.silva@example.com"
}
```

### **5. Excluir Usuário**
**DELETE /users/{id}/**
**Resposta:** 204 No Content

### **6. 🔑 Login**
**POST /auth/login/**
```json
{
  "email": "joao@example.com",
  "senha": "123456"
}
```
**Resposta:** 200 OK
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

## 🔒 Autenticação e Segurança
- O login gera um **token JWT**, que deve ser enviado no cabeçalho das requisições autenticadas:
  ```
  Authorization: Bearer SEU_TOKEN_AQUI
  ```
- Senhas são armazenadas usando **bcrypt** para maior segurança.
- Apenas usuários autenticados podem modificar seus dados ou excluir sua conta.

## 🧪 Testes Automatizados
Para rodar os testes:
```bash
python manage.py test
```

Os testes cobrem os principais endpoints para garantir a qualidade da API.

## 📜 Documentação da API
A API é documentada com Swagger. Acesse `http://127.0.0.1:8000/docs/` para visualizar a documentação interativa.

## 🤝 Contribuição
Contribuições são bem-vindas! Para sugerir melhorias ou corrigir problemas, abra uma issue ou envie um pull request.

## 📄 Licença
Este projeto está licenciado sob a [MIT License](LICENSE).


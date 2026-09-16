# Segurança em Aplicações — Guia Completo

## Sumário
1. [Por que segurança importa desde o início](#1-por-que-segurança-importa-desde-o-início)
2. [Hash de senhas](#2-hash-de-senhas)
3. [Autenticação](#3-autenticação)
4. [Tokens](#4-tokens)
5. [JWT (JSON Web Token)](#5-jwt-json-web-token)
6. [Sessões](#6-sessões)
7. [Tokens vs Sessões — qual usar](#7-tokens-vs-sessões--qual-usar)
8. [CORS](#8-cors)
9. [SQL Injection](#9-sql-injection)
10. [Validação de entrada](#10-validação-de-entrada)
11. [Variáveis secretas e .env](#11-variáveis-secretas-e-env)
12. [Checklist final de boas práticas](#12-checklist-final-de-boas-práticas)

---

## 1. Por que segurança importa desde o início

Segurança não é algo para "adicionar depois" — várias vulnerabilidades vêm de decisões tomadas (ou negligenciadas) desde as primeiras linhas de código: como senhas são guardadas, como dados de entrada são tratados, o que fica exposto publicamente. Este guia cobre os fundamentos que toda aplicação que lida com usuários deveria ter.

---

## 2. Hash de senhas

**Nunca** guarde senhas em texto puro no banco de dados. Se o banco vazar, todas as senhas ficam expostas imediatamente. A solução é guardar um **hash** da senha — uma transformação de mão única: fácil de calcular, praticamente impossível de reverter.

```python
# NUNCA faça isso:
senha_no_banco = "minhasenha123"  # texto puro — péssima ideia
```

```python
# Usando bcrypt (biblioteca recomendada para senhas)
# pip install bcrypt
import bcrypt

senha = b"minhasenha123"  # bcrypt trabalha com bytes

# Gerar o hash (ao cadastrar o usuário)
hash_senha = bcrypt.hashpw(senha, bcrypt.gensalt())
# guarda "hash_senha" no banco — nunca a senha original

# Verificar (ao fazer login)
senha_digitada = b"minhasenha123"
if bcrypt.checkpw(senha_digitada, hash_senha):
    print("Senha correta")
else:
    print("Senha incorreta")
```

Por que não usar algo como `md5` ou `sha256` puro? Esses algoritmos são rápidos demais — ótimos para verificar integridade de arquivos, péssimos para senhas, porque permitem tentar bilhões de combinações por segundo em um ataque de força bruta. `bcrypt` (e similares como `argon2`, `scrypt`) são **propositalmente lentos** e usam um **salt** (valor aleatório único por senha) automaticamente, o que impede o uso de tabelas pré-computadas (*rainbow tables*) e torna ataques em massa inviáveis.

---

## 3. Autenticação

**Autenticação** é o processo de confirmar **quem** é o usuário (diferente de **autorização**, que é decidir **o que** esse usuário pode fazer).

Fluxo básico de autenticação por senha:

```python
def autenticar(email, senha_digitada):
    usuario = buscar_usuario_por_email(email)
    if usuario is None:
        return None  # não revele se foi "email não existe" ou "senha errada"

    if bcrypt.checkpw(senha_digitada.encode(), usuario["hash_senha"]):
        return usuario
    return None
```

> Detalhe importante: a mensagem de erro para "email não existe" e "senha errada" deveria ser a mesma ("credenciais inválidas") — diferenciar as duas ajuda um atacante a descobrir quais e-mails estão cadastrados.

Depois de autenticado, o sistema precisa **lembrar** que aquele usuário está logado nas próximas requisições — é aí que entram sessões e tokens.

---

## 4. Tokens

Um **token** é uma credencial temporária, gerada após o login, que o cliente passa a enviar em cada requisição para provar que já está autenticado — sem precisar reenviar usuário e senha toda vez.

```python
import secrets

token = secrets.token_urlsafe(32)  # gera um token aleatório seguro
# guardar esse token associado ao usuário (no banco, ou em cache como Redis)
```

O cliente então envia esse token em requisições futuras, geralmente no header:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## 5. JWT (JSON Web Token)

**JWT** é um formato específico e muito usado de token, que carrega informações (chamadas *claims*) dentro dele mesmo — como o id do usuário e uma data de expiração — de forma que o servidor consiga validar o token **sem precisar consultar o banco de dados** a cada requisição.

Um JWT tem três partes, separadas por ponto: `header.payload.assinatura`

```python
# pip install pyjwt
import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "chave-super-secreta"  # nunca deixe isso no código — ver seção de .env

# Gerar o token (no login)
payload = {
    "usuario_id": 5,
    "exp": datetime.now(timezone.utc) + timedelta(hours=1)  # expiração
}
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Validar o token (em cada requisição autenticada)
try:
    dados = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print(dados["usuario_id"])
except jwt.ExpiredSignatureError:
    print("Token expirado")
except jwt.InvalidTokenError:
    print("Token inválido")
```

**Importante**: o conteúdo de um JWT (o `payload`) **não é criptografado**, apenas assinado — qualquer um pode decodificar e ler o conteúdo (ex: em jwt.io), só não consegue **alterar** sem invalidar a assinatura. Por isso, nunca coloque dados sensíveis (senha, dados privados) dentro do payload de um JWT.

---

## 6. Sessões

**Sessão** é outra forma de manter o usuário autenticado, com uma diferença fundamental em relação a um JWT: o estado (quem é o usuário, o que ele pode fazer) fica guardado **no servidor**, e o cliente recebe apenas um identificador (geralmente em um cookie).

```python
from flask import Flask, session

app = Flask(__name__)
app.secret_key = "chave-super-secreta"  # necessária para assinar o cookie de sessão

@app.route("/login", methods=["POST"])
def login():
    usuario = autenticar(...)
    session["usuario_id"] = usuario["id"]  # guarda na sessão
    return "Login feito"

@app.route("/perfil")
def perfil():
    usuario_id = session.get("usuario_id")
    if usuario_id is None:
        return "Não autenticado", 401
    return f"Usuário logado: {usuario_id}"
```

O navegador guarda um cookie com o id da sessão, e o envia automaticamente em cada requisição — diferente do JWT, que costuma ser enviado manualmente no header `Authorization`.

---

## 7. Tokens vs Sessões — qual usar

| | Sessão | Token (JWT) |
|---|---|---|
| Onde fica o estado | No servidor | No próprio token (client-side) |
| Escala em múltiplos servidores | Precisa de armazenamento compartilhado (ex: Redis) | Mais simples, qualquer servidor consegue validar sozinho |
| Revogar acesso antes de expirar | Fácil (apaga a sessão no servidor) | Mais difícil (o token continua "válido" até expirar, a menos que se implemente uma lista de bloqueio) |
| Uso típico | Aplicações web tradicionais (server-rendered) | APIs, aplicações mobile, sistemas distribuídos |

---

## 8. CORS

**CORS** (Cross-Origin Resource Sharing) é o mecanismo do navegador que controla se um site rodando em um domínio (`meusite.com`) pode fazer requisições para uma API em **outro** domínio (`api.outrosite.com`). Por padrão, navegadores bloqueiam esse tipo de requisição entre origens diferentes, por segurança — o servidor precisa explicitamente permitir.

```python
# pip install flask-cors
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://meufrontend.com"])  # só permite esse domínio
```

⚠️ **Cuidado**: liberar CORS para `*` (qualquer origem) em uma API que lida com dados sensíveis ou autenticação é uma prática arriscada — só use `*` em APIs verdadeiramente públicas e sem dados sensíveis.

---

## 9. SQL Injection

SQL Injection é uma das vulnerabilidades mais clássicas: acontece quando dados vindos do usuário são inseridos diretamente em uma query SQL sem tratamento, permitindo que alguém manipule a query original.

```python
# VULNERÁVEL — nunca faça isso
email = input("Email: ")  # usuário digita: ' OR '1'='1
query = f"SELECT * FROM usuarios WHERE email = '{email}'"
cursor.execute(query)
# a query final vira: SELECT * FROM usuarios WHERE email = '' OR '1'='1'
# isso retorna TODOS os usuários, ignorando o filtro
```

```python
# SEGURO — sempre use parâmetros (?), nunca concatenação/f-string com dados do usuário
query = "SELECT * FROM usuarios WHERE email = ?"
cursor.execute(query, (email,))
```

O banco de dados trata o valor do parâmetro como **dado puro**, nunca como parte do comando SQL — isso elimina a vulnerabilidade completamente. A mesma regra vale para PostgreSQL (com `%s` no lugar de `?`, dependendo da biblioteca) e para qualquer ORM (SQLAlchemy, Django ORM), que já protege contra isso por padrão.

---

## 10. Validação de entrada

**Nunca confie em dados vindos de fora** — de formulários, APIs, uploads, parâmetros de URL. Tudo que vem do cliente deve ser validado antes de ser usado.

```python
def cadastrar_usuario(dados):
    if "email" not in dados or "@" not in dados["email"]:
        raise ValueError("Email inválido")
    if "idade" not in dados or not isinstance(dados["idade"], int):
        raise ValueError("Idade inválida")
    if dados["idade"] < 0 or dados["idade"] > 120:
        raise ValueError("Idade fora do intervalo esperado")
    # só agora, com os dados validados, prosseguir
```

Para projetos maiores, validar campo por campo manualmente fica repetitivo — bibliotecas como **Pydantic** (mencionada no tutorial de JSON) automatizam isso de forma declarativa:

```python
from pydantic import BaseModel, EmailStr, conint

class NovoUsuario(BaseModel):
    email: EmailStr
    idade: conint(ge=0, le=120)  # inteiro entre 0 e 120

# Se os dados não baterem com o formato, o Pydantic já lança erro automaticamente
usuario = NovoUsuario(email="ana@email.com", idade=28)
```

Validação de entrada também protege contra outros ataques além de SQL Injection — como XSS (injeção de scripts maliciosos em páginas HTML) e uploads de arquivos maliciosos disfarçados.

---

## 11. Variáveis secretas e .env

**Segredos** (senhas de banco, chaves de API, `SECRET_KEY` de JWT/sessão) nunca devem estar escritos diretamente no código-fonte — principalmente porque o código costuma ir para um repositório Git, que pode ser público ou, mesmo privado, acessado por mais pessoas do que deveria ter acesso ao segredo.

```python
# NUNCA faça isso
SECRET_KEY = "abc123"
DATABASE_URL = "postgresql://usuario:senha123@localhost/banco"
```

A prática correta é guardar esses valores em um arquivo `.env`, que **nunca** é enviado ao controle de versão:

```
# .env
SECRET_KEY=uma-chave-bem-aleatoria-e-longa
DATABASE_URL=postgresql://usuario:senha123@localhost/banco
```

```python
# pip install python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()  # lê o arquivo .env e carrega como variáveis de ambiente

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
```

```
# .gitignore
.env
```

Para que outras pessoas saibam quais variáveis o projeto precisa, sem expor os valores reais, é comum manter um `.env.example` versionado (com nomes de variáveis, mas sem os valores reais), como mencionado no tutorial de estrutura de projeto.

Em produção (deploy), essas variáveis geralmente são configuradas diretamente no painel da plataforma de hospedagem (Render, Railway, etc.), não em um arquivo `.env` no servidor.

---

## 12. Checklist final de boas práticas

- [ ] Senhas sempre com hash (`bcrypt`/`argon2`), nunca texto puro.
- [ ] Mensagens de erro de login genéricas ("credenciais inválidas"), sem revelar se o e-mail existe.
- [ ] Tokens/sessões com expiração definida.
- [ ] `SECRET_KEY` forte, aleatória, fora do código-fonte.
- [ ] CORS configurado para as origens específicas necessárias, não `*`, em APIs sensíveis.
- [ ] Toda query SQL usando parâmetros (`?`/`%s`), nunca concatenação de string.
- [ ] Toda entrada de usuário validada antes de ser usada (tipo, formato, limites).
- [ ] `.env` no `.gitignore`, nunca commitado.
- [ ] HTTPS habilitado em produção (ver tutorial de Internet/HTTP).
- [ ] Dependências do projeto atualizadas (vulnerabilidades conhecidas costumam ser corrigidas em versões novas de bibliotecas).

# Internet, HTTP e APIs — Como Tudo se Conecta

## Sumário
1. [Cliente e servidor](#1-cliente-e-servidor)
2. [IP — o endereço de cada máquina](#2-ip--o-endereço-de-cada-máquina)
3. [DNS — traduzindo nomes em endereços](#3-dns--traduzindo-nomes-em-endereços)
4. [Portas](#4-portas)
5. [TCP/IP — visão geral](#5-tcpip--visão-geral)
6. [HTTP](#6-http)
7. [HTTPS](#7-https)
8. [Request e Response](#8-request-e-response)
9. [Headers](#9-headers)
10. [Status codes](#10-status-codes)
11. [O que é uma API](#11-o-que-é-uma-api)
12. [Resumo rápido (cheat sheet)](#12-resumo-rápido-cheat-sheet)

---

## 1. Cliente e servidor

A internet, no fundo, funciona majoritariamente no modelo **cliente-servidor**:

- **Cliente**: quem faz o pedido (seu navegador, um app no celular, um script Python).
- **Servidor**: quem responde ao pedido (uma máquina rodando um programa que fica esperando requisições — como vimos no tutorial de "do script ao programa de verdade").

```
Cliente (navegador) ──── pedido ────▶ Servidor (site)
Cliente (navegador) ◀─── resposta ─── Servidor (site)
```

---

## 2. IP — o endereço de cada máquina

Todo dispositivo conectado à internet tem um **endereço IP**, único naquela rede — como um endereço postal, para que os dados saibam para onde ir.

```
192.168.0.10      → IPv4, formato mais comum (4 números de 0 a 255)
2001:0db8::1       → IPv6, formato mais novo, criado por escassez de IPs IPv4
127.0.0.1          → sempre aponta para a própria máquina (localhost)
```

---

## 3. DNS — traduzindo nomes em endereços

Ninguém decora endereços IP para acessar sites — usamos nomes (`google.com`). O **DNS** (Domain Name System) é o sistema que traduz esses nomes em endereços IP.

```
Você digita: google.com
DNS traduz para: 142.250.218.14
O navegador então se conecta a esse IP
```

```bash
nslookup google.com   # consulta manual de DNS pelo terminal
```

---

## 4. Portas

Como vimos no tutorial de Linux/localhost, uma porta identifica **qual programa**, entre vários rodando na mesma máquina, deve receber a conexão.

| Porta | Uso comum |
|---|---|
| 80 | HTTP |
| 443 | HTTPS |
| 22 | SSH |
| 5432 | PostgreSQL |
| 3306 | MySQL |

```
http://meusite.com:8000
              │        │
           endereço   porta
```

Quando a porta não é especificada em uma URL, o navegador assume 80 (HTTP) ou 443 (HTTPS) por padrão.

---

## 5. TCP/IP — visão geral

TCP/IP é o conjunto de regras (protocolos) que faz os dados viajarem de forma confiável entre duas máquinas na internet.

- **IP**: cuida do **endereçamento** — para onde os dados devem ir.
- **TCP**: cuida da **entrega confiável** — garante que os dados cheguem completos, na ordem certa, reenviando pedaços perdidos se necessário.

Analogia: o IP é como o endereço escrito no envelope; o TCP é como o serviço de correio garantindo que a carta chegue inteira e na ordem certa, mesmo que seja enviada em várias partes.

HTTP (próxima seção) é construído **em cima** do TCP/IP — ou seja, quando você acessa um site, por trás dos panos o TCP/IP já está cuidando de toda a entrega dos dados.

---

## 6. HTTP

**HTTP** (HyperText Transfer Protocol) é o protocolo usado para comunicação entre cliente e servidor na web — o conjunto de regras que define como um pedido e uma resposta devem ser formatados.

Principais métodos (verbos):

| Método | Uso |
|---|---|
| `GET` | Buscar/ler dados (ex: abrir uma página, listar itens) |
| `POST` | Criar algo novo (ex: enviar um formulário, cadastrar um usuário) |
| `PUT` | Atualizar/substituir um recurso inteiro |
| `PATCH` | Atualizar parcialmente um recurso |
| `DELETE` | Remover um recurso |

```
GET /usuarios/5        → buscar o usuário de id 5
POST /usuarios          → criar um novo usuário
PUT /usuarios/5          → substituir os dados do usuário 5
DELETE /usuarios/5        → remover o usuário 5
```

---

## 7. HTTPS

HTTPS é o HTTP com uma camada extra de **criptografia** (TLS/SSL) — os dados trocados entre cliente e servidor ficam embaralhados de forma que ninguém no meio do caminho (ex: alguém na mesma rede Wi-Fi) consiga ler o conteúdo, mesmo interceptando o tráfego.

- Sites com HTTPS mostram um cadeado no navegador.
- Hoje é considerado padrão obrigatório para qualquer site real, especialmente os que lidam com login, dados pessoais ou pagamentos.
- Na prática, ao fazer deploy (tutorial anterior), a própria plataforma de hospedagem geralmente já configura HTTPS automaticamente.

---

## 8. Request e Response

Toda comunicação HTTP tem duas partes: a **requisição** (o que o cliente pede) e a **resposta** (o que o servidor devolve).

**Requisição (Request):**

```
GET /usuarios/5 HTTP/1.1
Host: meusite.com
Accept: application/json
```

**Resposta (Response):**

```
HTTP/1.1 200 OK
Content-Type: application/json

{"id": 5, "nome": "Ana", "email": "ana@email.com"}
```

---

## 9. Headers

**Headers** são metadados enviados junto com a requisição ou a resposta — informações sobre a mensagem, sem fazer parte do conteúdo principal.

| Header | Uso |
|---|---|
| `Content-Type` | Formato do conteúdo (ex: `application/json`, `text/html`) |
| `Authorization` | Credenciais de autenticação (ex: `Bearer <token>`) |
| `Accept` | Formato que o cliente aceita receber de volta |
| `User-Agent` | Identifica o programa/navegador que fez a requisição |
| `Cache-Control` | Regras de cache |

```python
import requests

resposta = requests.get(
    "https://api.exemplo.com/usuarios",
    headers={"Authorization": "Bearer meu_token_aqui"}
)
```

---

## 10. Status codes

O **status code** é um número que indica o resultado da requisição, na resposta do servidor.

| Faixa | Significado geral |
|---|---|
| 1xx | Informacional (raro no dia a dia) |
| 2xx | Sucesso |
| 3xx | Redirecionamento |
| 4xx | Erro do cliente (o pedido está errado) |
| 5xx | Erro do servidor (o servidor falhou ao processar) |

Os mais comuns na prática:

| Código | Significado |
|---|---|
| `200 OK` | Sucesso |
| `201 Created` | Recurso criado com sucesso (comum após um `POST`) |
| `204 No Content` | Sucesso, sem conteúdo para devolver (comum após um `DELETE`) |
| `301 Moved Permanently` | Recurso mudou de endereço permanentemente |
| `400 Bad Request` | O pedido está mal formado |
| `401 Unauthorized` | Falta autenticação (não informou quem é) |
| `403 Forbidden` | Está autenticado, mas não tem permissão |
| `404 Not Found` | Recurso não existe |
| `429 Too Many Requests` | Cliente fez requisições demais (limite de taxa) |
| `500 Internal Server Error` | Erro genérico no servidor |
| `503 Service Unavailable` | Servidor temporariamente indisponível |

---

## 11. O que é uma API

**API** (Application Programming Interface) é uma forma padronizada de dois programas conversarem entre si. Uma **API web** (a mais comum hoje) usa HTTP como meio de comunicação — em vez de um site devolver HTML para um navegador mostrar, ela devolve dados (geralmente em JSON) para outro programa consumir.

```python
import requests

resposta = requests.get("https://api.exemplo.com/usuarios/5")
print(resposta.status_code)  # 200
dados = resposta.json()       # converte o JSON da resposta em dict/list Python
print(dados["nome"])
```

Isso conecta diretamente com o tutorial "do script ao programa de verdade": quando você cria uma rota Flask como `/soma`, você já está construindo uma API simples — outro programa (não só o navegador) pode chamar essa mesma URL e receber uma resposta.

---

## 12. Resumo rápido (cheat sheet)

```
Cliente ──requisição (GET/POST/PUT/DELETE)──▶ Servidor
Cliente ◀──resposta (status code + dados)──── Servidor

IP        → endereço da máquina
DNS       → traduz nomes em IP
Porta     → identifica qual programa na máquina
TCP/IP    → entrega confiável dos dados
HTTP      → regras da conversa cliente-servidor
HTTPS     → HTTP + criptografia

200 OK · 201 Created · 400 Bad Request
401 Unauthorized · 403 Forbidden · 404 Not Found
500 Internal Server Error
```

```python
import requests
r = requests.get("https://api.exemplo.com/dados", headers={"Authorization": "Bearer TOKEN"})
r.status_code
r.json()
```

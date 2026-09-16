# Python + JSON — Guia Completo

## Sumário
1. [O que é JSON](#1-o-que-é-json)
2. [Tipos JSON vs tipos Python](#2-tipos-json-vs-tipos-python)
3. [json.dumps e json.loads](#3-jsondumps-e-jsonloads)
4. [json.dump e json.load (arquivos)](#4-jsondump-e-jsonload-arquivos)
5. [Formatando a saída (indent, sort_keys)](#5-formatando-a-saída-indent-sort_keys)
6. [Trabalhando com estruturas aninhadas](#6-trabalhando-com-estruturas-aninhadas)
7. [Serializando objetos personalizados](#7-serializando-objetos-personalizados)
8. [Desserializando para objetos personalizados](#8-desserializando-para-objetos-personalizados)
9. [Tratando erros de JSON inválido](#9-tratando-erros-de-json-inválido)
10. [JSON e APIs (requests)](#10-json-e-apis-requests)
11. [JSON Lines (.jsonl)](#11-json-lines-jsonl)
12. [Validando estrutura de JSON](#12-validando-estrutura-de-json)
13. [Boas práticas](#13-boas-práticas)
14. [Erros comuns](#14-erros-comuns)

---

## 1. O que é JSON

**JSON** (JavaScript Object Notation) é um formato de texto para representar dados estruturados — hoje o padrão mais usado para troca de dados entre programas, especialmente em APIs web.

```json
{
    "nome": "Ana",
    "idade": 28,
    "ativo": true,
    "cursos": ["Python", "SQL"],
    "endereco": {
        "cidade": "São Paulo",
        "cep": "01000-000"
    },
    "telefone": null
}
```

Em Python, o módulo `json` (da biblioteca padrão, não precisa instalar nada) converte entre JSON (texto) e estruturas Python (dict, list, etc).

---

## 2. Tipos JSON vs tipos Python

| JSON | Python |
|---|---|
| `object` (`{}`) | `dict` |
| `array` (`[]`) | `list` |
| `string` | `str` |
| `number` (int) | `int` |
| `number` (float) | `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

A conversão entre esses tipos acontece automaticamente ao usar as funções do módulo `json`.

---

## 3. json.dumps e json.loads

`dumps` (dump **s**tring) converte um objeto Python em uma **string** JSON. `loads` (load **s**tring) faz o inverso.

```python
import json

dados = {"nome": "Ana", "idade": 28, "ativo": True}

texto_json = json.dumps(dados)
print(texto_json)
print(type(texto_json))  # <class 'str'>
# {"nome": "Ana", "idade": 28, "ativo": true}

dados_de_volta = json.loads(texto_json)
print(dados_de_volta)
print(type(dados_de_volta))  # <class 'dict'>
```

> Truque para lembrar: as funções que terminam com **"s"** (`dumps`, `loads`) trabalham com **s**tring. As sem "s" (próxima seção) trabalham com **arquivo**.

---

## 4. json.dump e json.load (arquivos)

`dump` escreve JSON diretamente em um **arquivo**. `load` lê JSON diretamente de um arquivo.

```python
import json

dados = {"nome": "Ana", "idade": 28}

# Escrever em arquivo
with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f)

# Ler de arquivo
with open("dados.json", "r", encoding="utf-8") as f:
    dados_lidos = json.load(f)

print(dados_lidos)
```

---

## 5. Formatando a saída (indent, sort_keys)

Por padrão, `dumps`/`dump` geram o JSON "compactado", numa linha só. Para gerar algo legível (ex: salvar um arquivo de configuração):

```python
import json

dados = {"b": 2, "a": 1, "c": {"nome": "Ana"}}

texto = json.dumps(dados, indent=4, sort_keys=True, ensure_ascii=False)
print(texto)
```

```json
{
    "a": 1,
    "b": 2,
    "c": {
        "nome": "Ana"
    }
}
```

- `indent=4`: identação de 4 espaços, deixa o JSON legível.
- `sort_keys=True`: ordena as chaves alfabeticamente.
- `ensure_ascii=False`: mantém acentos como estão (ex: "São Paulo"), em vez de escapá-los (`\u00e3o`).

---

## 6. Trabalhando com estruturas aninhadas

JSON frequentemente vem com listas dentro de dicionários, dicionários dentro de listas, etc. Acessar segue a mesma lógica de dicionários/listas normais do Python.

```python
dados = {
    "usuarios": [
        {"nome": "Ana", "idade": 28},
        {"nome": "Bruno", "idade": 34},
    ]
}

for usuario in dados["usuarios"]:
    print(usuario["nome"])

# Acesso seguro (evita KeyError se o campo não existir)
idade = dados["usuarios"][0].get("idade", "não informado")
```

---

## 7. Serializando objetos personalizados

O `json` sabe converter os tipos básicos (dict, list, str, int, etc), mas **não** sabe, por padrão, como converter um objeto de uma classe sua. Duas formas comuns de resolver:

**Convertendo para dict antes:**

```python
class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

usuario = Usuario("Ana", 28)

texto = json.dumps(usuario.__dict__)
# {"nome": "Ana", "idade": 28}
```

**Usando um parâmetro `default` (para casos mais controlados):**

```python
def converter_usuario(obj):
    if isinstance(obj, Usuario):
        return {"nome": obj.nome, "idade": obj.idade}
    raise TypeError(f"Objeto do tipo {type(obj)} não é serializável")

texto = json.dumps(usuario, default=converter_usuario)
```

Isso é especialmente útil com `datetime`, que também não é serializável por padrão:

```python
from datetime import datetime

def converter(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Tipo não serializável: {type(obj)}")

dados = {"criado_em": datetime.now()}
texto = json.dumps(dados, default=converter)
```

---

## 8. Desserializando para objetos personalizados

Para transformar o JSON lido de volta em um objeto da sua classe (em vez de só um dict), use o parâmetro `object_hook`:

```python
class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Usuario({self.nome}, {self.idade})"

def para_usuario(d):
    if "nome" in d and "idade" in d:
        return Usuario(d["nome"], d["idade"])
    return d

texto = '{"nome": "Ana", "idade": 28}'
usuario = json.loads(texto, object_hook=para_usuario)
print(usuario)  # Usuario(Ana, 28)
```

---

## 9. Tratando erros de JSON inválido

Nem todo texto é um JSON válido — sempre trate esse erro ao ler dados externos (arquivos, respostas de API).

```python
import json

texto_invalido = "{nome: Ana}"  # JSON inválido (chaves precisam de aspas)

try:
    dados = json.loads(texto_invalido)
except json.JSONDecodeError as e:
    print(f"JSON inválido: {e}")
```

---

## 10. JSON e APIs (requests)

Na prática, JSON aparece o tempo todo ao consumir ou criar APIs web (ver tutorial de HTTP/APIs).

```python
import requests

# Consumindo uma API que devolve JSON
resposta = requests.get("https://api.exemplo.com/usuarios/5")
dados = resposta.json()  # já faz o json.loads por trás dos panos
print(dados["nome"])

# Enviando JSON em uma requisição POST
novo_usuario = {"nome": "Carla", "idade": 22}
resposta = requests.post("https://api.exemplo.com/usuarios", json=novo_usuario)
# o parâmetro "json=" já serializa o dict e define o header Content-Type certo
```

Em uma aplicação Flask (ver tutorial "do script ao programa de verdade"), o caminho inverso — devolver JSON como resposta:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/usuarios/<int:id>")
def obter_usuario(id):
    usuario = {"id": id, "nome": "Ana"}
    return jsonify(usuario)  # converte o dict em JSON e define os headers corretos
```

---

## 11. JSON Lines (.jsonl)

Formato onde cada **linha** do arquivo é um objeto JSON independente — muito usado para logs e grandes volumes de dados, porque permite processar linha por linha sem carregar o arquivo inteiro na memória.

```
{"nome": "Ana", "idade": 28}
{"nome": "Bruno", "idade": 34}
```

```python
import json

# Escrever
with open("dados.jsonl", "w", encoding="utf-8") as f:
    for usuario in [{"nome": "Ana"}, {"nome": "Bruno"}]:
        f.write(json.dumps(usuario) + "\n")

# Ler
with open("dados.jsonl", "r", encoding="utf-8") as f:
    for linha in f:
        usuario = json.loads(linha)
        print(usuario)
```

---

## 12. Validando estrutura de JSON

Em aplicações reais, especialmente ao receber dados de fora (APIs, formulários), é importante validar se o JSON tem os campos esperados, com os tipos certos — não confiar cegamente na estrutura.

```python
def validar_usuario(dados):
    campos_obrigatorios = ["nome", "idade"]
    for campo in campos_obrigatorios:
        if campo not in dados:
            raise ValueError(f"Campo obrigatório ausente: {campo}")
    if not isinstance(dados["idade"], int):
        raise ValueError("idade deve ser um número inteiro")
    return True
```

Para validações mais robustas em projetos maiores, bibliotecas como **Pydantic** fazem isso de forma declarativa e são muito usadas junto com FastAPI:

```python
from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str
    idade: int

usuario = Usuario(**{"nome": "Ana", "idade": 28})  # valida automaticamente
```

---

## 13. Boas práticas

- Sempre use `encoding="utf-8"` ao abrir arquivos JSON, para lidar corretamente com acentuação.
- Use `ensure_ascii=False` ao salvar arquivos legíveis por humanos com texto em português.
- Trate `json.JSONDecodeError` sempre que ler JSON de uma fonte externa (arquivo, API, input do usuário).
- Valide a estrutura dos dados recebidos antes de usá-los — nunca assuma que um campo existe.
- Para dados grandes/streaming, considere JSON Lines em vez de um único JSON gigante.

---

## 14. Erros comuns

1. **Confundir `dumps`/`loads` (string) com `dump`/`load` (arquivo)**.
2. **Esquecer que JSON usa aspas duplas**, não aspas simples — `'{"nome": "Ana"}'` é válido, `"{'nome': 'Ana'}"` não é.
3. **Tentar serializar objetos não suportados** (datetime, classes próprias) sem usar `default`.
4. **Não tratar `JSONDecodeError`** ao ler dados de fontes externas, deixando o programa quebrar.
5. **Confiar cegamente na estrutura do JSON recebido**, sem checar se os campos esperados realmente existem.

---

## Resumo rápido (cheat sheet)

```python
import json

# String <-> Python
texto = json.dumps(dados, indent=4, ensure_ascii=False, sort_keys=True)
dados = json.loads(texto)

# Arquivo <-> Python
with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)

with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# Tratamento de erro
try:
    dados = json.loads(texto)
except json.JSONDecodeError as e:
    print(f"JSON inválido: {e}")

# Com requests
resposta = requests.get(url)
dados = resposta.json()
requests.post(url, json=novo_dado)
```

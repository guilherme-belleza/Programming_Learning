# SQLite3 — Guia Completo (com Python)

## Sumário
1. [O que é SQLite](#1-o-que-é-sqlite)
2. [Criando um banco e uma tabela](#2-criando-um-banco-e-uma-tabela)
3. [Inserindo dados](#3-inserindo-dados)
4. [Consultando dados (SELECT)](#4-consultando-dados-select)
5. [Atualizando dados (UPDATE)](#5-atualizando-dados-update)
6. [Excluindo dados (DELETE)](#6-excluindo-dados-delete)
7. [Transações](#7-transações)
8. [Python + SQLite (módulo sqlite3)](#8-python--sqlite-módulo-sqlite3)
9. [Boas práticas](#9-boas-práticas)
10. [Erros comuns](#10-erros-comuns)

---

## 1. O que é SQLite

SQLite é um banco de dados relacional leve, que guarda **tudo em um único arquivo** (ex: `banco.db`), sem precisar instalar ou configurar um servidor separado. É ótimo para estudar SQL, prototipar, aplicações pequenas/médias, e para uso local (ex: um app desktop).

Vantagens: simples, sem instalação, vem embutido no Python (`sqlite3`).
Limitações: não é ideal para muitos acessos simultâneos (escrita concorrente) nem para sistemas muito grandes — nesses casos, algo como PostgreSQL é mais indicado (próximo tutorial).

---

## 2. Criando um banco e uma tabela

Pelo terminal (usando o cliente `sqlite3`, se instalado):

```bash
sqlite3 banco.db
```

```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    idade INTEGER,
    criado_em TEXT DEFAULT CURRENT_TIMESTAMP
);
```

- `PRIMARY KEY AUTOINCREMENT`: identificador único, gerado automaticamente.
- `NOT NULL`: campo obrigatório.
- `UNIQUE`: não permite valores repetidos.
- `DEFAULT`: valor usado quando nada é informado.

---

## 3. Inserindo dados

```sql
INSERT INTO usuarios (nome, email, idade) VALUES ("Ana", "ana@email.com", 28);
INSERT INTO usuarios (nome, email, idade) VALUES ("Bruno", "bruno@email.com", 34);
```

---

## 4. Consultando dados (SELECT)

```sql
SELECT * FROM usuarios;                        -- todos os campos, todas as linhas
SELECT nome, email FROM usuarios;               -- só campos específicos
SELECT * FROM usuarios WHERE idade > 30;        -- filtro
SELECT * FROM usuarios ORDER BY nome ASC;       -- ordenação
SELECT * FROM usuarios LIMIT 5;                 -- limita quantidade de resultados
SELECT COUNT(*) FROM usuarios;                  -- conta linhas
SELECT * FROM usuarios WHERE nome LIKE "A%";    -- nomes que começam com "A"
```

---

## 5. Atualizando dados (UPDATE)

```sql
UPDATE usuarios SET idade = 29 WHERE nome = "Ana";
```

⚠️ **Sempre use `WHERE`** — um `UPDATE` sem `WHERE` atualiza **todas** as linhas da tabela.

---

## 6. Excluindo dados (DELETE)

```sql
DELETE FROM usuarios WHERE nome = "Bruno";
```

⚠️ Mesma regra: `DELETE` sem `WHERE` apaga **todas** as linhas da tabela.

---

## 7. Transações

Uma transação agrupa várias operações para que **todas aconteçam, ou nenhuma aconteça** — importante quando várias mudanças precisam ser consistentes entre si (ex: transferir saldo entre duas contas).

```sql
BEGIN TRANSACTION;

UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;

COMMIT;   -- confirma as mudanças
-- ou, se algo der errado:
ROLLBACK; -- desfaz tudo desde o BEGIN
```

Se o programa travar no meio de um `UPDATE` sem transação, o banco pode ficar em um estado inconsistente (dinheiro "sumindo" de uma conta sem entrar na outra). Transações evitam exatamente isso.

---

## 8. Python + SQLite (módulo sqlite3)

O módulo `sqlite3` já vem embutido no Python — não precisa instalar nada.

```python
import sqlite3

# Conectar (cria o arquivo se não existir)
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# Criar tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        idade INTEGER
    )
""")

# Inserir dados — SEMPRE use parâmetros (?), nunca f-string/concatenação
cursor.execute(
    "INSERT INTO usuarios (nome, email, idade) VALUES (?, ?, ?)",
    ("Ana", "ana@email.com", 28)
)
conexao.commit()  # confirma a escrita no banco

# Inserir vários de uma vez
usuarios = [
    ("Bruno", "bruno@email.com", 34),
    ("Carla", "carla@email.com", 22),
]
cursor.executemany(
    "INSERT INTO usuarios (nome, email, idade) VALUES (?, ?, ?)",
    usuarios
)
conexao.commit()

# Consultar
cursor.execute("SELECT * FROM usuarios WHERE idade > ?", (25,))
resultados = cursor.fetchall()   # todas as linhas
for linha in resultados:
    print(linha)

uma_linha = cursor.execute("SELECT * FROM usuarios WHERE id = ?", (1,)).fetchone()

# Atualizar
cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (29, "Ana"))
conexao.commit()

# Excluir
cursor.execute("DELETE FROM usuarios WHERE nome = ?", ("Bruno",))
conexao.commit()

# Fechar conexão
conexao.close()
```

### Usando `with` (fecha e trata erros automaticamente)

```python
import sqlite3

with sqlite3.connect("banco.db") as conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    for linha in cursor.fetchall():
        print(linha)
# a conexão é fechada automaticamente ao sair do bloco
```

### Retornando resultados como dicionário (mais legível)

```python
conexao = sqlite3.connect("banco.db")
conexao.row_factory = sqlite3.Row  # faz as linhas se comportarem como dicionário
cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")
for linha in cursor.fetchall():
    print(linha["nome"], linha["email"])  # acesso por nome da coluna
```

### Transação em Python

```python
try:
    cursor.execute("UPDATE contas SET saldo = saldo - 100 WHERE id = 1")
    cursor.execute("UPDATE contas SET saldo = saldo + 100 WHERE id = 2")
    conexao.commit()
except Exception as e:
    conexao.rollback()
    print(f"Erro na transação, desfazendo tudo: {e}")
```

---

## 9. Boas práticas

- **Sempre** use parâmetros (`?`) nas queries — nunca monte SQL concatenando strings com dados do usuário (risco de SQL Injection — assunto do tutorial de segurança).
- Feche a conexão (ou use `with`) para não deixar o arquivo do banco "preso".
- Use transações para operações que precisam ser consistentes entre si.
- Defina `NOT NULL` e `UNIQUE` nos campos certos desde a criação da tabela — corrigir depois é mais trabalhoso.
- Faça backup do arquivo `.db` regularmente — é um único arquivo, fácil de copiar.

---

## 10. Erros comuns

1. **Esquecer `conexao.commit()`** — as mudanças de `INSERT`/`UPDATE`/`DELETE` não são salvas até isso ser chamado.
2. **Concatenar valores direto na query** (`f"SELECT * FROM usuarios WHERE nome = '{nome}'"`) — abre brecha de SQL Injection.
3. **`UPDATE`/`DELETE` sem `WHERE`** — afeta a tabela inteira.
4. **Não fechar a conexão** em scripts longos, deixando o arquivo bloqueado para outros acessos.
5. **Usar SQLite para aplicações com muitos usuários escrevendo ao mesmo tempo** — SQLite trava a escrita para um acesso por vez; para esse cenário, PostgreSQL é mais adequado.

---

## Resumo rápido (cheat sheet)

```python
import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, nome TEXT)")
cursor.execute("INSERT INTO t (nome) VALUES (?)", ("Ana",))
cursor.execute("SELECT * FROM t WHERE nome = ?", ("Ana",))
cursor.fetchall()
cursor.execute("UPDATE t SET nome = ? WHERE id = ?", ("Ana Paula", 1))
cursor.execute("DELETE FROM t WHERE id = ?", (1,))

conexao.commit()
conexao.close()
```

```sql
CREATE TABLE t (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL);
INSERT INTO t (nome) VALUES ("Ana");
SELECT * FROM t WHERE nome LIKE "A%";
UPDATE t SET nome = "Ana Paula" WHERE id = 1;
DELETE FROM t WHERE id = 1;
BEGIN TRANSACTION; ... COMMIT; / ROLLBACK;
```

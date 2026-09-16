# PostgreSQL — Índices, Modelagem e Migrações

## Sumário
1. [PostgreSQL vs SQLite](#1-postgresql-vs-sqlite)
2. [Modelagem de banco de dados](#2-modelagem-de-banco-de-dados)
3. [Chaves primárias e estrangeiras](#3-chaves-primárias-e-estrangeiras)
4. [Normalização (visão geral)](#4-normalização-visão-geral)
5. [Índices](#5-índices)
6. [Tipos de índice](#6-tipos-de-índice)
7. [Quando um índice NÃO ajuda](#7-quando-um-índice-não-ajuda)
8. [Migrações](#8-migrações)
9. [Boas práticas](#9-boas-práticas)
10. [Erros comuns](#10-erros-comuns)

---

## 1. PostgreSQL vs SQLite

PostgreSQL é um banco de dados relacional completo, rodando como um **servidor** separado (diferente do SQLite, que é um arquivo único lido diretamente). Isso o torna adequado para aplicações reais, com múltiplos usuários acessando e escrevendo ao mesmo tempo, mais recursos (tipos de dados avançados, controle de acesso, performance em grande escala).

| | SQLite | PostgreSQL |
|---|---|---|
| Instalação | Nenhuma (arquivo único) | Servidor dedicado |
| Acesso simultâneo | Limitado | Robusto |
| Uso típico | Protótipos, apps locais, estudo | Aplicações em produção |
| Recursos avançados | Básicos | Extensos (índices avançados, funções, extensões) |

---

## 2. Modelagem de banco de dados

Modelar um banco é decidir **quais tabelas existem, quais campos cada uma tem, e como elas se relacionam entre si** — antes de escrever qualquer SQL.

Exemplo: um sistema de blog.

```
usuarios
├── id (PK)
├── nome
└── email

posts
├── id (PK)
├── titulo
├── conteudo
├── usuario_id (FK -> usuarios.id)   -- quem escreveu
└── criado_em

comentarios
├── id (PK)
├── texto
├── post_id (FK -> posts.id)         -- em qual post
├── usuario_id (FK -> usuarios.id)   -- quem comentou
└── criado_em
```

- **PK** (Primary Key): identifica cada linha de forma única.
- **FK** (Foreign Key): aponta para a PK de outra tabela, criando o relacionamento.

**Tipos de relacionamento:**

| Tipo | Exemplo |
|---|---|
| 1 para muitos (1:N) | Um usuário tem vários posts |
| Muitos para muitos (N:N) | Posts têm várias tags, e uma tag está em vários posts (precisa de uma tabela intermediária) |
| 1 para 1 (1:1) | Um usuário tem um único perfil estendido |

Exemplo de tabela intermediária para N:N:

```sql
CREATE TABLE posts_tags (
    post_id INTEGER REFERENCES posts(id),
    tag_id INTEGER REFERENCES tags(id),
    PRIMARY KEY (post_id, tag_id)
);
```

---

## 3. Chaves primárias e estrangeiras

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    titulo TEXT NOT NULL,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE
);
```

- `SERIAL`: gera um número incremental automaticamente (equivalente ao `AUTOINCREMENT`).
- `REFERENCES usuarios(id)`: declara a chave estrangeira, garantindo que `usuario_id` só possa referenciar um `id` que realmente existe em `usuarios`.
- `ON DELETE CASCADE`: se o usuário for excluído, seus posts são excluídos automaticamente junto. Outras opções: `ON DELETE SET NULL`, `ON DELETE RESTRICT` (impede a exclusão do usuário se ele tiver posts).

---

## 4. Normalização (visão geral)

Normalizar é organizar os dados para **evitar repetição e inconsistência**. Ideia central: cada informação deve existir em um único lugar.

```sql
-- Ruim: nome do autor repetido em cada post, risco de inconsistência
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    titulo TEXT,
    autor_nome TEXT,
    autor_email TEXT
);

-- Melhor: autor é uma referência a uma tabela própria
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    titulo TEXT,
    usuario_id INTEGER REFERENCES usuarios(id)
);
```

Assim, se o e-mail do usuário mudar, é uma atualização em um único lugar (`usuarios`), não em cada post que ele escreveu.

> Na prática, às vezes se aceita alguma repetição de propósito (desnormalização) em troca de performance de leitura — mas isso é uma decisão consciente, feita depois de entender o modelo normalizado primeiro.

---

## 5. Índices

Um índice é uma estrutura auxiliar que acelera buscas em uma tabela — parecido com o índice de um livro: em vez de ler página por página, você vai direto ao ponto.

```sql
CREATE INDEX idx_posts_usuario_id ON posts(usuario_id);
CREATE INDEX idx_usuarios_email ON usuarios(email);
```

Sem índice, uma busca como `SELECT * FROM usuarios WHERE email = 'ana@email.com'` precisa examinar **todas** as linhas da tabela (*table scan*). Com índice, o banco consegue localizar a linha diretamente, muito mais rápido — a diferença fica enorme conforme a tabela cresce.

Colunas usadas com frequência em `WHERE`, `JOIN` ou `ORDER BY` são boas candidatas a índice. Chaves primárias já ganham índice automaticamente; chaves estrangeiras, **não** — geralmente vale criar um índice nelas manualmente.

---

## 6. Tipos de índice

| Tipo | Uso típico |
|---|---|
| **B-tree** (padrão) | Igualdade e comparação (`=`, `<`, `>`, `BETWEEN`), a maioria dos casos |
| **Hash** | Só igualdade (`=`), mais raro de usar diretamente |
| **GIN** | Campos JSON, arrays, busca de texto completo |
| **Unique index** | Garante que os valores da coluna sejam únicos (criado automaticamente com `UNIQUE`) |

```sql
CREATE INDEX idx_posts_titulo ON posts USING GIN (to_tsvector('portuguese', titulo));
-- exemplo de índice para busca de texto completo
```

Ver quais índices existem em uma tabela:

```sql
\d posts   -- no psql (cliente de terminal do Postgres)
```

---

## 7. Quando um índice NÃO ajuda

- Em tabelas pequenas, o ganho é insignificante (o banco pode até ignorar o índice e ler a tabela toda, por ser mais rápido nesse caso).
- Índices deixam a **escrita** (`INSERT`/`UPDATE`/`DELETE`) um pouco mais lenta, porque o índice também precisa ser atualizado.
- Criar índice em toda coluna "por garantia" é contraproducente — deve-se indexar o que realmente é consultado com frequência.

---

## 8. Migrações

Uma **migração** é um arquivo que descreve uma mudança na estrutura do banco (criar tabela, adicionar coluna, criar índice) de forma **versionada e reproduzível** — em vez de alterar o banco manualmente, você escreve o que mudou, e essa mudança pode ser aplicada em qualquer ambiente (sua máquina, a de um colega, o servidor de produção) de forma idêntica.

Sem migrações, cada pessoa (ou servidor) pode acabar com uma estrutura de banco ligeiramente diferente — uma fonte clássica de bugs difíceis de rastrear.

Em Python, a ferramenta mais comum para isso é o **Alembic** (frequentemente usado com SQLAlchemy):

```bash
pip install alembic
alembic init migrations
```

```python
# migrations/versions/xxxx_criar_tabela_usuarios.py
def upgrade():
    op.create_table(
        "usuarios",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nome", sa.String, nullable=False),
        sa.Column("email", sa.String, unique=True, nullable=False),
    )

def downgrade():
    op.drop_table("usuarios")
```

```bash
alembic upgrade head     # aplica todas as migrações pendentes
alembic downgrade -1     # desfaz a última migração
```

- `upgrade()`: o que fazer para aplicar a mudança.
- `downgrade()`: como desfazer, caso necessário.

Frameworks como Django já têm um sistema de migrações embutido (`makemigrations` / `migrate`), funcionando de forma parecida.

---

## 9. Boas práticas

- Sempre defina chaves estrangeiras explicitamente — o banco garante a integridade dos dados por você.
- Crie índices para colunas usadas em `WHERE`/`JOIN` com frequência, especialmente chaves estrangeiras.
- Nunca altere a estrutura do banco de produção manualmente — sempre por migração, para manter todos os ambientes sincronizados.
- Teste migrações em um ambiente de desenvolvimento antes de aplicar em produção.
- Modele pensando no relacionamento real entre os dados, não apenas em "como vou usar agora" — mudanças de modelo depois costumam ser mais trabalhosas.

---

## 10. Erros comuns

1. **Não usar `ON DELETE`/`ON UPDATE`** e deixar registros "órfãos" (referenciando algo que não existe mais).
2. **Criar índice em toda coluna** sem necessidade, prejudicando performance de escrita.
3. **Alterar a estrutura do banco direto em produção**, sem migração, perdendo rastreabilidade do que mudou e quando.
4. **Duplicar dados** (desnormalizar) sem necessidade real, gerando inconsistência.
5. **Esquecer de indexar chaves estrangeiras**, deixando `JOIN`s lentos conforme a tabela cresce.

---

## Resumo rápido (cheat sheet)

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE INDEX idx_posts_usuario_id ON posts(usuario_id);
```

```bash
alembic init migrations
alembic upgrade head
alembic downgrade -1
```

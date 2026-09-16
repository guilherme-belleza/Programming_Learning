# Pathlib, Diretórios e Caminhos — Guia Completo

## Sumário
1. [Por que usar pathlib](#1-por-que-usar-pathlib)
2. [Criando objetos Path](#2-criando-objetos-path)
3. [Caminhos absolutos vs relativos](#3-caminhos-absolutos-vs-relativos)
4. [Navegando pela árvore de diretórios](#4-navegando-pela-árvore-de-diretórios)
5. [Verificando existência e tipo](#5-verificando-existência-e-tipo)
6. [Criando e removendo diretórios](#6-criando-e-removendo-diretórios)
7. [Listando conteúdo (iterdir, glob, rglob)](#7-listando-conteúdo-iterdir-glob-rglob)
8. [Lendo e escrevendo arquivos](#8-lendo-e-escrevendo-arquivos)
9. [Manipulando nomes e extensões](#9-manipulando-nomes-e-extensões)
10. [Copiando, movendo e removendo arquivos](#10-copiando-movendo-e-removendo-arquivos)
11. [Compatibilidade entre sistemas operacionais](#11-compatibilidade-entre-sistemas-operacionais)
12. [Boas práticas](#12-boas-práticas)
13. [Erros comuns](#13-erros-comuns)

---

## 1. Por que usar pathlib

Antes do `pathlib`, a forma padrão de trabalhar com arquivos e diretórios era o módulo `os.path`, que manipula caminhos como **strings puras**. Isso funciona, mas é propenso a erros (barras erradas, concatenação manual) e menos legível.

O `pathlib` (desde o Python 3.4) trata caminhos como **objetos**, com métodos e operadores próprios.

```python
# Jeito antigo (os.path)
import os
caminho = os.path.join("pasta", "subpasta", "arquivo.txt")

# Jeito moderno (pathlib)
from pathlib import Path
caminho = Path("pasta") / "subpasta" / "arquivo.txt"
```

Repare no uso do operador `/` para juntar partes do caminho — é uma das grandes vantagens do pathlib: legibilidade e menos chance de erro.

---

## 2. Criando objetos Path

```python
from pathlib import Path

# A partir de uma string
p = Path("dados/relatorio.csv")

# Caminho do diretório atual (onde o script está sendo executado)
atual = Path.cwd()

# Caminho da pasta do usuário (home)
home = Path.home()

# Caminho do próprio arquivo que está sendo executado
# (útil para localizar arquivos relativos ao script, não ao terminal)
arquivo_atual = Path(__file__).resolve()
```

> `Path(__file__)` é extremamente útil quando você quer que o script encontre arquivos vizinhos a ele, independente de onde o usuário rodou o comando no terminal.

---

## 3. Caminhos absolutos vs relativos

- **Caminho absoluto**: começa da raiz do sistema de arquivos, aponta sempre para o mesmo lugar, não importa de onde você execute o programa.
  - Windows: `C:\Users\joao\projeto\dados.csv`
  - Linux/Mac: `/home/joao/projeto/dados.csv`
- **Caminho relativo**: depende do diretório atual de onde o comando foi executado (o "diretório de trabalho", ou *working directory*).
  - `dados/relatorio.csv` só funciona se você estiver na pasta certa quando rodar o script.

```python
from pathlib import Path

relativo = Path("dados/relatorio.csv")
print(relativo.is_absolute())  # False

absoluto = relativo.resolve()
print(absoluto)               # /home/joao/projeto/dados/relatorio.csv
print(absoluto.is_absolute()) # True
```

`resolve()` converte um caminho relativo em absoluto, calculando a partir do diretório atual — e também resolve `..` e `.` no caminho.

⚠️ **Armadilha clássica**: um script que usa caminhos relativos funciona quando você roda de dentro da pasta do projeto, mas quebra quando é executado de outro lugar (ex: um agendador de tarefas, ou outro script chamando o seu). Por isso, é comum usar `Path(__file__).resolve().parent` como base para montar caminhos relativos **ao próprio script**, não ao terminal.

```python
# Base segura: pasta onde o script está, não onde o terminal está
BASE_DIR = Path(__file__).resolve().parent
arquivo_config = BASE_DIR / "config.json"
```

---

## 4. Navegando pela árvore de diretórios

```python
p = Path("/home/joao/projeto/dados/relatorio.csv")

p.parent        # /home/joao/projeto/dados  (pasta que contém o arquivo)
p.parent.parent # /home/joao/projeto        (sobe mais um nível)
p.parents[0]    # mesmo que p.parent
p.parents[1]    # mesmo que p.parent.parent

list(p.parents)  # lista de TODOS os diretórios acima, até a raiz

p.name    # "relatorio.csv"  (nome do arquivo com extensão)
p.stem    # "relatorio"      (nome sem extensão)
p.suffix  # ".csv"           (extensão)
p.parts   # ('/', 'home', 'joao', 'projeto', 'dados', 'relatorio.csv')
```

---

## 5. Verificando existência e tipo

```python
p = Path("dados/relatorio.csv")

p.exists()    # True se o caminho existe (arquivo OU pasta)
p.is_file()   # True se existe e é um arquivo
p.is_dir()    # True se existe e é um diretório
p.is_symlink()  # True se for um link simbólico
```

Sempre verifique antes de tentar ler/escrever, para evitar exceções desnecessárias:

```python
if p.exists() and p.is_file():
    conteudo = p.read_text()
else:
    print("Arquivo não encontrado.")
```

---

## 6. Criando e removendo diretórios

```python
pasta = Path("dados/processados")

# Cria a pasta (falha se o pai não existir e se já existir)
pasta.mkdir()

# parents=True: cria também as pastas intermediárias que faltarem
# exist_ok=True: não gera erro se a pasta já existir
pasta.mkdir(parents=True, exist_ok=True)

# Remove uma pasta VAZIA
pasta.rmdir()

# Para remover uma pasta com conteúdo, use shutil
import shutil
shutil.rmtree(pasta)  # cuidado: remove tudo, sem confirmação
```

---

## 7. Listando conteúdo (iterdir, glob, rglob)

```python
pasta = Path("dados")

# Lista tudo (arquivos e pastas) dentro da pasta, sem entrar em subpastas
for item in pasta.iterdir():
    print(item)

# glob: busca por padrão, também só no nível atual
for csv in pasta.glob("*.csv"):
    print(csv)

# rglob: igual ao glob, mas busca recursivamente em TODAS as subpastas
for csv in pasta.rglob("*.csv"):
    print(csv)

# Combinando com list comprehension para filtrar
arquivos_csv = [f for f in pasta.iterdir() if f.suffix == ".csv"]
```

| Método | Entra em subpastas? | Uso típico |
|---|---|---|
| `iterdir()` | Não | Listar tudo de um nível |
| `glob("padrao")` | Não | Buscar por padrão em um nível |
| `rglob("padrao")` | Sim | Buscar por padrão em toda a árvore |

---

## 8. Lendo e escrevendo arquivos

O pathlib tem atalhos que dispensam o `open()` tradicional para casos simples:

```python
p = Path("dados/nota.txt")

# Escrever texto (cria o arquivo se não existir, sobrescreve se existir)
p.write_text("Olá, mundo!", encoding="utf-8")

# Ler texto
conteudo = p.read_text(encoding="utf-8")

# Escrever/ler bytes (ex: imagens, arquivos binários)
p.write_bytes(b"dados binarios")
dados = p.read_bytes()
```

Para casos mais complexos (leitura linha a linha, append, controle fino), use `open()` normalmente — o `Path` funciona direto como argumento:

```python
with p.open("a", encoding="utf-8") as f:  # "a" = append, adiciona ao final
    f.write("\nnova linha")
```

---

## 9. Manipulando nomes e extensões

```python
p = Path("relatorio_2024.csv")

p.with_suffix(".json")       # relatorio_2024.json  (troca a extensão)
p.with_name("novo_nome.csv") # novo_nome.csv          (troca o nome inteiro)
p.with_stem("relatorio_2025") # relatorio_2025.csv     (troca só o nome, mantém extensão)

# Montando um novo caminho a partir de partes
novo = p.parent / f"{p.stem}_backup{p.suffix}"
# relatorio_2024_backup.csv
```

---

## 10. Copiando, movendo e removendo arquivos

O `pathlib` cuida de caminhos, mas operações de cópia/movimentação de arquivos ficam no módulo `shutil`:

```python
import shutil
from pathlib import Path

origem = Path("dados/relatorio.csv")
destino = Path("backup/relatorio.csv")

shutil.copy(origem, destino)       # copia o arquivo (mantém o original)
shutil.copytree("pasta_a", "pasta_b")  # copia uma pasta inteira

origem.rename(destino)             # move/renomeia (cuidado: sobrescreve sem avisar em alguns SOs)
shutil.move(str(origem), str(destino))  # mover é mais seguro entre discos/SOs diferentes

origem.unlink()          # remove um arquivo
origem.unlink(missing_ok=True)  # não gera erro se o arquivo não existir
```

---

## 11. Compatibilidade entre sistemas operacionais

Windows usa `\` como separador de caminho, enquanto Linux e macOS usam `/`. O `pathlib` resolve isso automaticamente:

```python
from pathlib import Path

p = Path("dados") / "relatorio.csv"
print(p)
# Linux/Mac: dados/relatorio.csv
# Windows:   dados\relatorio.csv
```

Você nunca deveria escrever `"dados\\relatorio.csv"` manualmente — deixe o pathlib decidir o separador certo para o sistema em que o código está rodando.

Se precisar forçar um formato específico (ex: gerar uma URL, que sempre usa `/`), use `as_posix()`:

```python
p.as_posix()  # sempre retorna com "/", independente do SO
```

---

## 12. Boas práticas

- Prefira `pathlib` a `os.path` em código novo — é mais legível e menos propenso a erro.
- Use `Path(__file__).resolve().parent` como âncora para caminhos relativos a recursos do próprio projeto (configs, templates, dados de exemplo).
- Sempre verifique `exists()` antes de operações que podem falhar.
- Use `mkdir(parents=True, exist_ok=True)` como padrão — evita erros bobos em criação de pastas.
- Para remover pastas com conteúdo, tenha certeza absoluta do caminho antes de usar `shutil.rmtree` — não tem como desfazer.

---

## 13. Erros comuns

1. **Misturar strings e Path sem converter** — algumas funções antigas exigem `str(caminho)`.
2. **Depender do diretório de execução** — usar caminho relativo sem uma base seguros faz o script quebrar dependendo de onde é chamado.
3. **Esquecer `encoding="utf-8"`** — pode gerar problemas com acentuação em textos.
4. **Usar `rmdir()` em pasta não vazia** — gera erro; o método certo para isso é `shutil.rmtree`.
5. **Concatenar caminhos com `+` em vez de `/`** — funciona com strings, mas perde a vantagem do pathlib e é mais sujeito a erro.

---

## Resumo rápido (cheat sheet)

```python
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent

p = BASE_DIR / "dados" / "arquivo.csv"

p.exists(); p.is_file(); p.is_dir()
p.parent; p.name; p.stem; p.suffix
p.resolve(); p.is_absolute()

p.parent.mkdir(parents=True, exist_ok=True)
list(p.parent.iterdir())
list(p.parent.glob("*.csv"))
list(p.parent.rglob("*.csv"))

p.write_text("texto", encoding="utf-8")
texto = p.read_text(encoding="utf-8")

shutil.copy(p, BASE_DIR / "backup.csv")
p.unlink(missing_ok=True)
```

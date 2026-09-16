from pathlib import Path

caminho_atual = Path.cwd()
print(f"Conteudo dentro do diretório ({caminho_atual})")

# .iterdir() --> Lista tudo (arquivos e pastas) dentro da pasta, sem entrar em subpastas
for n, itens in enumerate(caminho_atual.iterdir()):
    print(f"{n+1}º) = {itens}\n", end='')

# BONUS (teste)
# rglob: igual ao glob, mas busca recursivamente em TODAS as subpastas
print(f'Exibindo TODO O DIRETÓRIO + SUB-PASTAS + TODOS OS ARQUIVOS com o rglob("*")') 

# "*" -> para qlqer coisa até arquivos q n mostram a extensao 'texto.txt'       
# "*.*" -> pra qlqer coisa antes do . e qlqer coisa depois . (qlqer nome de arquivo e qlqer extensão)                                                                          #

for tudo in caminho_atual.rglob("*.*"):
    print(tudo)


# TESTE DO Path.walker() ?

# ============================================================
# 2 — Explorando arquivos e diretórios com pathlib
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

from pathlib import Path


# Caminho do diretório atual.
caminho_atual = Path.cwd()
print(f"Conteudo dentro do diretório ({caminho_atual})")


# .iterdir() percorre os itens existentes diretamente dentro
# do diretório informado.
#
# Ele encontra arquivos e pastas, mas não entra automaticamente
# nas subpastas.
for n, itens in enumerate(caminho_atual.iterdir()):
    print(f"{n+1}º) = {itens}\n", end='')


# (teste)
# rglob() funciona de forma recursiva, permitindo pesquisar
# também dentro das subpastas.
#
# Aqui o padrão "*.*" foi utilizado para testar a busca por
# arquivos que possuem ponto na estrutura do nome.
print(f'Exibindo TODO O DIRETÓRIO + SUB-PASTAS + TODOS OS ARQUIVOS com o rglob("*.*")')

for tudo in caminho_atual.rglob("*.*"):
    print(tudo)



#Documentação do exercício
#region DOCUMENTAÇÃO

# ============================================================
# OBJETIVO DO EXERCÍCIO
# ============================================================
#
# Neste exercício o objetivo foi começar a utilizar pathlib
# para investigar o conteúdo de um diretório.
#
# Depois de aprender a representar caminhos com Path, o próximo
# passo foi descobrir como percorrer os arquivos e pastas
# existentes dentro desses caminhos.
#
# Foram explorados principalmente:
#
# - Path.cwd()
# - Path.iterdir()
# - Path.rglob()
# - enumerate()
# - padrões de busca com glob
#
#
# ============================================================
# PATH.CWD()
# ============================================================
#
# caminho_atual = Path.cwd()
#
# Path.cwd() retorna o diretório de trabalho atual.
#
# O resultado é armazenado em caminho_atual para que o mesmo
# caminho possa ser utilizado nas operações seguintes.
#
# Exemplo:
#
# /home/usuario/projeto
#
#
# ============================================================
# PATH.ITERDIR()
# ============================================================
#
# caminho_atual.iterdir()
#
# iterdir() permite percorrer os itens existentes diretamente
# dentro de um diretório.
#
# Esses itens podem ser:
#
# - arquivos
# - pastas
#
# Uma característica importante é que o iterdir() não percorre
# automaticamente o conteúdo das subpastas.
#
# Por exemplo, considerando:
#
# projeto/
# ├── arquivo.py
# ├── texto.txt
# └── documentos/
#     └── estudo.pdf
#
# O iterdir() do diretório projeto encontra:
#
# - arquivo.py
# - texto.txt
# - documentos
#
# Mas não entra dentro de documentos para encontrar estudo.pdf.
#
#
# ============================================================
# PERCORRENDO OS ITENS
# ============================================================
#
# for n, itens in enumerate(caminho_atual.iterdir()):
#
# O for percorre cada item encontrado pelo iterdir().
#
# O enumerate() foi utilizado para obter também uma numeração.
#
# n     -> índice da repetição
# itens -> item encontrado
#
# Como o índice começa em 0, foi utilizado:
#
# n + 1
#
# para apresentar a contagem começando em 1.
#
#
# ============================================================
# R.GLOB()
# ============================================================
#
# caminho_atual.rglob("*.*")
#
# rglob() realiza uma busca recursiva.
#
# Diferentemente do iterdir(), ele pode entrar nas subpastas
# e continuar procurando dentro delas.
#
# O "r" de rglob está relacionado justamente à ideia de
# busca recursiva.
#
#
# ============================================================
# O PADRÃO "*.*"
# ============================================================
#
# rglob("*.*")
#
# O argumento passado para rglob() é um padrão de busca.
#
# O primeiro * representa uma sequência de caracteres.
#
# O segundo * também representa uma sequência de caracteres.
#
# O ponto entre eles representa literalmente o ponto existente
# no nome.
#
# Dessa forma, o padrão:
#
# *.*
#
# é utilizado para encontrar itens que correspondam a esse
# formato, como:
#
# arquivo.py
# texto.txt
# imagem.png
#
# A utilização de padrões é uma parte importante da exploração
# do módulo pathlib.
#
#
# ============================================================
# TESTE COM R.GLOB()
# ============================================================
#
# for tudo in caminho_atual.rglob("*.*"):
#     print(tudo)
#
# Aqui cada resultado encontrado pela busca é armazenado
# temporariamente na variável tudo.
#
# Depois o caminho encontrado é exibido com print().
#
# Como o rglob() é recursivo, os resultados podem incluir
# arquivos existentes dentro de subpastas.
#
#
# ============================================================
# DIFERENÇA ENTRE ITERDIR() E RGLOB()
# ============================================================
#
# iterdir()
#
# Percorre os itens diretamente dentro de um diretório.
#
# Não entra automaticamente nas subpastas.
#
#
# rglob()
#
# Faz uma busca recursiva.
#
# Pode encontrar itens dentro do diretório atual e também
# dentro de suas subpastas.
#
#
# Uma forma simples de visualizar:
#
# iterdir()
#     ↓
# pasta atual
#
# rglob()
#     ↓
# pasta atual
#     ↓
# subpastas
#     ↓
# subpastas das subpastas
#     ↓
# e assim por diante
#
# ============================================================
# CONCEITOS PRATICADOS
# ============================================================
#
# Neste exercício foram praticados:
#
# - Path.cwd()
# - Path.iterdir()
# - Path.rglob()
# - busca recursiva
# - padrões de busca
# - enumerate()
# - percorrer arquivos e diretórios
#
# Este exercício representa o passo seguinte ao estudo inicial
# de caminhos: agora o caminho não é apenas exibido, mas usado
# para investigar o conteúdo do sistema de arquivos.
#
#endregion


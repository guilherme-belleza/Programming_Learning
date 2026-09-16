# ============================================================
# 3 — Diferenciando arquivos e diretórios com pathlib
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

from pathlib import Path


# Contadores utilizados para armazenar a quantidade de pastas
# e arquivos encontrados durante o percurso.
cont_arq = cont_dir = 0

# Lista contendo duas listas internas:
#
# lista[0] -> nomes das pastas
# lista[1] -> nomes dos arquivos
lista = [[], []]

# Obtém o diretório de trabalho atual.
dir_atual = Path.cwd()

# Percorre todos os itens encontrados diretamente dentro
# do diretório atual.
for item in dir_atual.iterdir():

    # Verifica se o item encontrado é um diretório/pasta.
    if item.is_dir():
        cont_dir += 1
        lista[0].append(item.name)
        print(f'PASTA --> {item.name}.')

    # Se não for uma pasta, verifica se é um arquivo.
    elif item.is_file():
        cont_arq += 1
        lista[1].append(item.name)
        print(f'DIRETÓRIO/ARQUIVO --> {item}.')


# Testando uma exibição diferente.
print(f"{cont_dir} PASTAS ENCONTRADOS --> {lista[0]}")
print(f"{cont_arq} ARQUIVOS/DIRETÓRIOS ENCONTRADOS. NOMES DOS ARQUIVOS -->{lista[1]}")


#Documentação do exercício
#region DOCUMENTAÇÃO

# ============================================================
# OBJETIVO DO EXERCÍCIO
# ============================================================
#
# Este exercício utiliza os conhecimentos dos exercícios
# anteriores para investigar o conteúdo de um diretório.
#
# O objetivo principal foi aprender a diferenciar:
#
# - arquivos
# - diretórios/pastas
#
# Também foi praticada uma pequena contagem dos dois tipos
# de itens encontrados.
#
# Recursos principais utilizados:
#
# - Path.cwd()
# - Path.iterdir()
# - Path.is_dir()
# - Path.is_file()
# - .name
# - append()
# - contadores
# - listas
#
#
# ============================================================
# IMPORTANDO PATH
# ============================================================
#
# from pathlib import Path
#
# Path é importado da biblioteca pathlib para trabalhar com
# caminhos de arquivos e diretórios.
#
#
# ============================================================
# CONTADORES
# ============================================================
#
# cont_arq = cont_dir = 0
#
# São criadas duas variáveis para controlar a quantidade
# de arquivos e diretórios encontrados.
#
# cont_arq -> contador de arquivos
# cont_dir -> contador de diretórios
#
# As duas recebem inicialmente o valor 0.
#
# A atribuição:
#
# cont_arq = cont_dir = 0
#
# permite atribuir o mesmo valor inicial às duas variáveis.
#
#
# ============================================================
# LISTA PARA ORGANIZAR OS RESULTADOS
# ============================================================
#
# lista = [[], []]
#
# Aqui foi criada uma lista contendo duas listas vazias.
#
# A ideia utilizada no exercício foi separar os resultados:
#
# lista[0] -> armazenará as pastas
# lista[1] -> armazenará os arquivos
#
# Inicialmente:
#
# lista = [[], []]
#
# Depois, conforme os itens são encontrados, os nomes são
# adicionados às listas correspondentes.
#
#
# ============================================================
# PATH.CWD()
# ============================================================
#
# dir_atual = Path.cwd()
#
# Obtém o diretório de trabalho atual e armazena o resultado
# na variável dir_atual.
#
# Esse caminho será utilizado pelo iterdir().
#
#
# ============================================================
# PERCORRENDO O DIRETÓRIO
# ============================================================
#
# for item in dir_atual.iterdir():
#
# O iterdir() percorre os itens existentes diretamente dentro
# do diretório atual.
#
# A cada repetição, a variável item representa um dos elementos
# encontrados.
#
# Esse elemento pode ser:
#
# - um arquivo
# - uma pasta
#
# É justamente a partir dessa variável que o programa consegue
# verificar qual é o tipo do item.
#
#
# ============================================================
# VERIFICANDO SE É UMA PASTA
# ============================================================
#
# if item.is_dir():
#
# is_dir() verifica se o caminho representa um diretório.
#
# O resultado é um valor booleano:
#
# True  -> é um diretório
# False -> não é um diretório
#
# Quando a condição é verdadeira, o contador de diretórios
# é incrementado:
#
# cont_dir += 1
#
#
# ============================================================
# ARMAZENANDO O NOME DA PASTA
# ============================================================
#
# lista[0].append(item.name)
#
# A propriedade .name retorna somente o nome final do caminho.
#
# Por exemplo:
#
# Se item representar:
#
# /home/usuario/projeto/documentos
#
# item.name retornará:
#
# documentos
#
# O append() adiciona esse nome à primeira lista.
#
#
# ============================================================
# VERIFICANDO SE É UM ARQUIVO
# ============================================================
#
# elif item.is_file():
#
# is_file() verifica se o caminho representa um arquivo.
#
# Assim como is_dir(), o resultado é booleano:
#
# True  -> é um arquivo
# False -> não é um arquivo
#
# Quando a condição é verdadeira, o contador de arquivos
# é incrementado:
#
# cont_arq += 1
#
#
# ============================================================
# ARMAZENANDO O NOME DO ARQUIVO
# ============================================================
#
# lista[1].append(item.name)
#
# O nome do arquivo é obtido através de .name e armazenado
# na segunda lista.
#
# Dessa forma, ao final do percurso:
#
# lista[0] contém as pastas
#
# lista[1] contém os arquivos
#
#
# ============================================================
# ITEM.NAME x ITEM
# ============================================================
#
# Existe uma diferença entre:
#
# item
#
# e:
#
# item.name
#
# item representa o caminho completo do elemento.
#
# Exemplo:
#
# /home/usuario/projeto/teste.py
#
# Já:
#
# item.name
#
# retorna somente:
#
# teste.py
#
# Neste exercício os dois foram utilizados para observar
# essa diferença.
#
#
# ============================================================
# CONTAGEM
# ============================================================
#
# Os contadores são atualizados durante o percurso:
#
# cont_dir += 1
#
# aumenta a quantidade de diretórios.
#
#
# cont_arq += 1
#
# aumenta a quantidade de arquivos.
#
# Ao terminar o for, os contadores representam a quantidade
# encontrada no diretório analisado.
#
#
# ============================================================
# EXIBINDO OS RESULTADOS
# ============================================================
#
# print(f"{cont_dir} PASTAS ENCONTRADOS --> {lista[0]}")
#
# Exibe:
#
# - quantidade de pastas encontradas
# - lista contendo os nomes das pastas
#
#
# print(f"{cont_arq} ARQUIVOS/DIRETÓRIOS ENCONTRADOS. NOMES DOS ARQUIVOS -->{lista[1]}")
#
# Exibe:
#
# - quantidade de arquivos encontrados
# - lista contendo os nomes dos arquivos
#
#
# ============================================================
# FLUXO DO PROGRAMA
# ============================================================
#
# O funcionamento pode ser resumido assim:
#
# Path.cwd()
#     ↓
# Obtém o diretório atual
#     ↓
# iterdir()
#     ↓
# Percorre cada item
#     ↓
# is_dir()  → é pasta?
#     ↓
# Sim → conta e adiciona na lista de pastas
#
# Caso contrário:
#
# is_file() → é arquivo?
#     ↓
# Sim → conta e adiciona na lista de arquivos
#
#     ↓
# Exibe os resultados
#
#
# ============================================================
# CONCEITOS PRATICADOS
# ============================================================
#
# Neste exercício foram praticados:
#
# - Path
# - Path.cwd()
# - Path.iterdir()
# - Path.is_dir()
# - Path.is_file()
# - propriedade .name
# - listas
# - listas dentro de listas
# - append()
# - contadores
# - estruturas if / elif
# - f-strings
#
# Este exercício fecha a sequência inicial de exploração
# do pathlib.
#
# Primeiro foram estudados os caminhos, depois a exploração
# do conteúdo de diretórios e, por fim, a diferenciação
# entre arquivos e pastas.
#
#endregion


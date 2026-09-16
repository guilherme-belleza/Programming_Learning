# ============================================================
# 1 — Conhecendo caminhos com pathlib
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

from pathlib import Path, PurePath


# Caminho do diretório atual (onde o script está sendo executado)
# Path.cwd() retorna um objeto Path representando o diretório atual.
caminho_atual = Path.cwd()
print(f"DIRETÓRIO ATUAL = (onde o script está sendo executado) ---> {caminho_atual}")

# .parent retorna o diretório pai do caminho atual.
print(f'Exibe o diretório/caminho até a pasta que contém o arquivo. -> {caminho_atual.parent}')


# Caminho da pasta do usuário (HOME)
# Path.home() retorna o diretório HOME do usuário atual.
pasta_usuario = Path.home()
print(f'DIRETÓRIO = (da pasta do usuário HOME)--->{pasta_usuario}')


# Documentação da lib.
# Para acessar as “partes” individuais (componentes ou pastas)
# de um caminho, podemos utilizar a propriedade PurePath.parts.
#
# PurePath.parts retorna uma tupla contendo os componentes
# individuais de um caminho.
#
# Exemplo:
#
# p = PurePath('/usr/bin/python3')
# p.parts
#
# Resultado:
#
# ('/', 'usr', 'bin', 'python3')


# Separando todos os componentes ou pastas de um caminho
# utilizando PurePath().
partes = PurePath(caminho_atual)
print(f"Tentando imprimir as partes -> {partes.parts}")


# Exibindo cada pasta/componente do diretório de forma formatada.
print("Partes Individuais do caminho atual.")
for i, pasta in enumerate(partes.parts):
    print(f"{i+1}º) --> {pasta}\n", end='')


# Diretório PAI
pai = caminho_atual.parent
print(f"DIRETÓRIO PAI ---> {pai}")


#Documentação do exercício
#region DOCUMENTAÇÃO

# ============================================================
# OBJETIVO DO EXERCÍCIO
# ============================================================
#
# Este exercício é uma introdução à biblioteca pathlib.
#
# O objetivo foi começar a trabalhar com caminhos do sistema
# operacional utilizando objetos Path, em vez de manipular
# caminhos apenas como strings.
#
# Foram praticados principalmente:
#
# - Path.cwd()
# - Path.home()
# - .parent
# - PurePath()
# - .parts
# - enumerate()
#
#
# ============================================================
# IMPORTANDO PATHLIB
# ============================================================
#
# from pathlib import Path, PurePath
#
# pathlib é uma biblioteca da própria linguagem Python utilizada
# para trabalhar com caminhos de arquivos e diretórios.
#
# Path representa caminhos e fornece diversos métodos e
# propriedades para trabalhar com o sistema de arquivos.
#
# PurePath também trabalha com a estrutura de caminhos, mas sem
# realizar operações diretamente no sistema de arquivos.
#
#
# ============================================================
# PATH.CWD()
# ============================================================
#
# caminho_atual = Path.cwd()
#
# cwd significa "Current Working Directory".
#
# Path.cwd() retorna o diretório de trabalho atual do programa.
#
# O resultado é um objeto Path.
#
# Exemplo de resultado:
#
# /home/usuario/projeto
#
# Uma característica importante do Path é que ele permite
# utilizar métodos e propriedades próprios para trabalhar
# com esse caminho.
#
#
# ============================================================
# .PARENT
# ============================================================
#
# caminho_atual.parent
#
# A propriedade .parent retorna o diretório pai do caminho.
#
# Por exemplo, considerando:
#
# /home/usuario/projeto
#
# O .parent será:
#
# /home/usuario
#
# Portanto, .parent permite subir um nível na estrutura
# de diretórios.
#
#
# ============================================================
# PATH.HOME()
# ============================================================
#
# pasta_usuario = Path.home()
#
# Path.home() retorna o diretório HOME do usuário atual.
#
# No Linux, por exemplo, pode retornar algo semelhante a:
#
# /home/usuario
#
# No Windows, o caminho seria diferente de acordo com
# o usuário e o sistema.
#
# Isso torna o código mais independente do sistema operacional.
#
#
# ============================================================
# PUREPATH.PARTS
# ============================================================
#
# partes = PurePath(caminho_atual)
#
# Aqui o caminho atual é utilizado para criar um objeto
# PurePath.
#
# A propriedade .parts permite acessar os componentes
# individuais do caminho.
#
# Exemplo:
#
# PurePath('/usr/bin/python3').parts
#
# Resultado:
#
# ('/', 'usr', 'bin', 'python3')
#
# O resultado é uma tupla.
#
# Cada elemento representa uma parte do caminho.
#
#
# ============================================================
# PERCORRENDO .PARTS
# ============================================================
#
# for i, pasta in enumerate(partes.parts):
#
# partes.parts contém todos os componentes do caminho.
#
# O for percorre cada componente individualmente.
#
# O enumerate() permite obter duas informações durante
# a repetição:
#
# i     -> índice/número da posição
# pasta -> componente atual do caminho
#
# Como os índices do Python começam em 0, foi utilizado:
#
# i + 1
#
# para apresentar a numeração começando em 1 para o usuário.
#
#
# ============================================================
# DIFERENÇA ENTRE PATH E PUREPATH NESTE EXERCÍCIO
# ============================================================
#
# Path é utilizado para representar caminhos e também permite
# realizar operações relacionadas ao sistema de arquivos.
#
# PurePath trabalha com a estrutura do caminho sem acessar
# diretamente o sistema de arquivos.
#
# Neste exercício, PurePath foi utilizado especificamente para
# explorar a propriedade .parts.
#
#
# ============================================================
# CONCEITOS PRATICADOS
# ============================================================
#
# Neste exercício foram praticados:
#
# - importação de classes da biblioteca pathlib
# - criação de objetos Path
# - Path.cwd()
# - Path.home()
# - propriedade .parent
# - PurePath()
# - propriedade .parts
# - tuplas
# - enumerate()
# - percorrer componentes de um caminho
#
# Este exercício serve como base para os próximos estudos de
# pathlib, nos quais os caminhos serão utilizados para investigar
# e manipular arquivos e diretórios.
#
#endregion
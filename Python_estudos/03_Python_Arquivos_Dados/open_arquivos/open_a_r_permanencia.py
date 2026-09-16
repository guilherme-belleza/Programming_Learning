# ============================================================
# Exercício: Leitura e escrita de arquivos com open()
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

from datetime import date


def entradas():
    txt = []
    data = 'DATA: ' + date.today().strftime('%d/%m/%Y') # Usando o .strftime -> dia/mes/ano
    assunto = input("Qual foi o assunto do estudo: ").strip()
    resumo = input(f"Informe um breve resumo sobre {assunto}: ").strip()
    txt.append(data)
    txt.append(assunto)
    txt.append(resumo)
    return txt


# Menu
while True:
    print(f"-"*30)
    print(f'{"<MENU>":^30}')
    print(f"-"*30)

    print(
        f"1- Registrar estudo.\n"
        f"2- Ver estudos registrados.\n"
        f"0- SAIR."
    )
    print(f"-"*30)

    opc = int(input(f"Escolha uma opção: "))

    # Registrar estudo
    if opc == 1:
        txt = ''
        lista = entradas()
        for i in lista:
            txt += (f"{i}\n")
        with open("registro_estudos.txt", "a", encoding='utf-8') as arquivo:
            arquivo.write(f"{txt}\n")

    elif opc == 2:
        print(f"Registro de estudos.")
        print()
        with open("registro_estudos.txt", "r", encoding='utf-8') as arquivo:
            conteudo = arquivo
            for linha in conteudo:
                print('*'*30)
                print(linha)


#Documentação do exercício
#region DOCUMENTAÇÃO

# ============================================================
# OBJETIVO DO EXERCÍCIO
# ============================================================
#
# Este exercício foi desenvolvido para praticar leitura e escrita
# de arquivos utilizando a função open().
#
# O programa permite:
#
# 1 - Registrar um estudo realizado.
# 2 - Salvar o registro em um arquivo .txt.
# 3 - Ler os estudos que já foram registrados.
#
# Além disso, o exercício utiliza:
#
# - datetime.date
# - strftime()
# - listas
# - funções
# - while
# - if / elif
# - for
# - with
# - open()
# - modos "a" e "r"
# - encoding
# - métodos append(), strip() e write()
#
#
# ============================================================
# IMPORTAÇÃO DO datetime
# ============================================================
#
# from datetime import date
#
# A classe date é importada do módulo datetime.
#
# Ela permite trabalhar com datas.
#
# Neste exercício ela é utilizada para obter a data atual:
#
# date.today()
#
# O resultado representa a data atual do sistema.
#
#
# ============================================================
# FORMATANDO A DATA
# ============================================================
#
# data = 'DATA: ' + date.today().strftime('%d/%m/%Y')
#
# O método strftime() transforma uma data em uma string
# utilizando o formato informado.
#
# %d -> dia
# %m -> mês
# %Y -> ano com quatro dígitos
#
# Exemplo:
#
# 16/09/2026
#
# O texto "DATA: " é concatenado antes da data para deixar
# o registro mais fácil de identificar.
#
#
# ============================================================
# FUNÇÃO entradas()
# ============================================================
#
# def entradas():
#
# A função é responsável por coletar as informações que serão
# registradas no arquivo.
#
# Em vez de deixar todas as entradas diretamente no menu,
# elas foram agrupadas dentro de uma função.
#
#
# ------------------------------------------------------------
# CRIAÇÃO DA LISTA
# ------------------------------------------------------------
#
# txt = []
#
# É criada uma lista vazia para armazenar temporariamente:
#
# - a data
# - o assunto
# - o resumo
#
#
# ------------------------------------------------------------
# OBTENDO O ASSUNTO
# ------------------------------------------------------------
#
# assunto = input("Qual foi o assunto do estudo: ").strip()
#
# input() recebe o texto digitado pelo usuário.
#
# O método strip() remove espaços em branco que estejam
# no início ou no final do texto.
#
#
# ------------------------------------------------------------
# OBTENDO O RESUMO
# ------------------------------------------------------------
#
# resumo = input(f"Informe um breve resumo sobre {assunto}: ").strip()
#
# Aqui é utilizada uma f-string para inserir o conteúdo da
# variável assunto dentro da mensagem apresentada ao usuário.
#
# Exemplo:
#
# Se assunto = "Python"
#
# A mensagem será:
#
# Informe um breve resumo sobre Python:
#
#
# ------------------------------------------------------------
# ADICIONANDO OS DADOS À LISTA
# ------------------------------------------------------------
#
# txt.append(data)
# txt.append(assunto)
# txt.append(resumo)
#
# append() adiciona um novo elemento ao final da lista.
#
# Ao final da função, a lista possui três elementos:
#
# [data, assunto, resumo]
#
#
# ------------------------------------------------------------
# RETORNANDO A LISTA
# ------------------------------------------------------------
#
# return txt
#
# O return devolve a lista para o ponto onde a função foi
# chamada.
#
# Dessa forma:
#
# lista = entradas()
#
# recebe a lista criada dentro da função.
#
#
# ============================================================
# ESTRUTURA DO MENU
# ============================================================
#
# while True:
#
# O while True cria um laço que continua executando
# indefinidamente.
#
# O menu pode ser exibido novamente após uma operação.
#
# Neste código ainda não existe uma condição de saída
# implementada para a opção 0.
#
#
# ============================================================
# REGISTRANDO UM ESTUDO
# ============================================================
#
# if opc == 1:
#
# Quando o usuário escolhe a opção 1, o programa chama
# a função entradas().
#
# lista = entradas()
#
# A lista retornada pela função é armazenada na variável lista.
#
#
# ============================================================
# TRANSFORMANDO A LISTA EM TEXTO
# ============================================================
#
# txt = ''
#
# Aqui é criada uma string vazia.
#
# Ela será utilizada para montar o conteúdo que será gravado
# no arquivo.
#
#
# for i in lista:
#     txt += (f"{i}\n")
#
# O for percorre cada elemento da lista.
#
# O conteúdo de cada elemento é acrescentado à string txt.
#
# O \n adiciona uma quebra de linha entre as informações.
#
# Assim, uma lista como:
#
# ['DATA: 16/09/2026', 'Python', 'Estudei arquivos']
#
# será transformada em algo semelhante a:
#
# DATA: 16/09/2026
# Python
# Estudei arquivos
#
#
# ============================================================
# OPEN() - MODO "a"
# ============================================================
#
# with open("registro_estudos.txt", "a", encoding='utf-8') as arquivo:
#
# open() é utilizada para abrir ou criar um arquivo.
#
# O primeiro argumento informa o nome do arquivo:
#
# "registro_estudos.txt"
#
# O segundo argumento informa o modo de abertura:
#
# "a" -> append
#
# O modo "a" permite adicionar conteúdo ao final do arquivo.
#
# Isso é importante neste exercício porque cada novo estudo
# deve ser acrescentado aos registros anteriores.
#
# Se fosse utilizado o modo "w", o conteúdo anterior seria
# sobrescrito.
#
#
# ============================================================
# ENCODING
# ============================================================
#
# encoding='utf-8'
#
# Define a codificação utilizada para trabalhar com o arquivo.
#
# O UTF-8 permite trabalhar corretamente com diversos caracteres,
# incluindo caracteres comuns na língua portuguesa:
#
# ç, ã, é, ê, ô, etc.
#
#
# ============================================================
# WITH
# ============================================================
#
# with open(...) as arquivo:
#
# O with é utilizado para trabalhar com o arquivo dentro de
# um contexto controlado.
#
# Ao sair desse bloco, o arquivo é fechado automaticamente.
#
# Isso evita a necessidade de chamar manualmente:
#
# arquivo.close()
#
#
# ============================================================
# ESCREVENDO NO ARQUIVO
# ============================================================
#
# arquivo.write(f"{txt}\n")
#
# O método write() escreve uma string dentro do arquivo.
#
# Neste caso, a string armazenada em txt é gravada e depois
# é adicionada mais uma quebra de linha.
#
# Como o arquivo foi aberto no modo "a", esse conteúdo será
# colocado depois do conteúdo que já existe.
#
#
# ============================================================
# LENDO OS ESTUDOS
# ============================================================
#
# elif opc == 2:
#
# Quando o usuário escolhe a opção 2, o programa abre o arquivo
# para leitura.
#
#
# with open("registro_estudos.txt", "r", encoding='utf-8') as arquivo:
#
# O modo utilizado agora é:
#
# "r" -> read
#
# Esse modo é utilizado para leitura do arquivo.
#
#
# ============================================================
# PERCORRENDO O ARQUIVO
# ============================================================
#
# conteudo = arquivo
#
# Aqui a variável conteudo passa a referenciar o próprio objeto
# arquivo.
#
#
# for linha in conteudo:
#     print('*'*30)
#     print(linha)
#
# O arquivo pode ser percorrido com um for.
#
# A cada repetição, a variável linha recebe uma linha do arquivo.
#
# Dessa forma, o programa consegue ler o conteúdo linha por linha.
#
#
# ============================================================
# RESUMO DOS MODOS UTILIZADOS
# ============================================================
#
# open("arquivo.txt", "a")
#
# "a" -> append
# Adiciona conteúdo ao final do arquivo.
#
#
# open("arquivo.txt", "r")
#
# "r" -> read
# Abre o arquivo para leitura.
#
#
# Existe também o modo:
#
# "w" -> write
#
# Ele é utilizado para escrita, porém sobrescreve o conteúdo
# existente do arquivo.
#
# Por isso, neste exercício foi utilizado "a" para registrar
# novos estudos sem apagar os anteriores.
#
#
# ============================================================
# CONCEITOS PRATICADOS
# ============================================================
#
# Este exercício serviu principalmente para praticar:
#
# - criação e chamada de funções
# - retorno de valores com return
# - manipulação de listas
# - entrada de dados com input()
# - tratamento de strings
# - obtenção da data atual
# - formatação de datas com strftime()
# - abertura de arquivos com open()
# - leitura de arquivos
# - escrita em arquivos
# - modo "r"
# - modo "a"
# - uso de with
# - encoding UTF-8
# - leitura linha por linha com for
#
# O exercício representa uma aplicação prática simples de
# persistência de dados utilizando arquivos de texto.
#
#endregion


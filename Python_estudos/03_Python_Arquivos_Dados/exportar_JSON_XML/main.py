
# ============================================================
# Exercício de Arquivos e Dados
#
# Este arquivo é o ponto de entrada do programa. Ele cria os
# objetos, organiza os dados e solicita suas exportações.
# ============================================================

from classes import *


def main():

    lista_usuarios = [
        Usuario('Jose', 'jose@gmail.com'),
        Usuario('Osvaldo', 'osval@outlook.com')
    ]

    lista_alunos = [
        Aluno('Maria', 'ADS', '1º ano'),
        Aluno('Jose', 'Matemática', '2º semestre')
    ]

    print(f"Formatp XML")
    exportar_dados(XML(), lista_usuarios)
    print()

    print(f"Formato JSON")
    exportar_dados(JSON(), lista_alunos)
    print()


if __name__ == "__main__":
    main()


# region Documentação do exercício

# ============================================================
# 1. IMPORTAÇÃO
# ============================================================
# from classes import *:
# Importa os nomes disponíveis no módulo classes.
#
# O caractere * permite importar vários nomes de uma vez.
# Em projetos maiores, importar explicitamente as classes e
# funções utilizadas costuma deixar o código mais claro.
#
# ============================================================
# 2. FUNÇÃO main()
# ============================================================
# Centraliza a execução principal do programa.
#
# lista_usuarios:
# Armazena objetos Usuario em uma lista.
#
# lista_alunos:
# Armazena objetos Aluno em outra lista.
#
# As listas permitem trabalhar com vários objetos do mesmo
# tipo e enviá-los juntos para o método de exportação.
#
# ============================================================
# 3. EXPORTAÇÃO DOS DADOS
# ============================================================
# XML() e JSON() criam instâncias das classes responsáveis
# por cada formato de exportação.
#
# exportar_dados(XML(), lista_usuarios):
# Envia os usuários para a função, utilizando XML como formato.
#
# exportar_dados(JSON(), lista_alunos):
# Envia os alunos para a função, utilizando JSON como formato.
#
# A função não precisa conhecer os detalhes internos de cada
# formato: ela chama o método exportar do objeto recebido.
#
# ============================================================
# 4. PONTO DE ENTRADA
# ============================================================
# if __name__ == "__main__":
# Verifica se este arquivo está sendo executado diretamente.
#
# Quando a condição é verdadeira, main() é chamada.
# Isso permite importar o módulo sem executar automaticamente
# a rotina principal.
#
# endregion

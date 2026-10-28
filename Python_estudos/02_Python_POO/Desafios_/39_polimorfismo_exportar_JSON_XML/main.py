from classes import *

def main():

    lista_usuarios = [Usuario('Jose', 'jose@gmail.com'), Usuario('Osvaldo', 'osval@outlook.com')]
    lista_alunos = [Aluno('Maria', 'ADS', '1º ano'), Aluno('Jose', 'Matemática', '2º semestre')]

    print(f"Formatp XML")
    exportar_dados(XML(), lista_usuarios)
    print()

    print(f"Formato JSON")
    exportar_dados(JSON(), lista_alunos)
    print()

if __name__ == "__main__":
    main()


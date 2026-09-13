from Gerenciador_arq import *

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():

    a1 = PDF("teste", 1200000)
    a2 = DOC("Tabela", 50000000)
    a1.abrir()

    # Método Polimórfico - TIPO PATO
    abrir_arquivo(a2)
if __name__ == "__main__":
    main()
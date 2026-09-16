from classes import *

def main():
    try:
        p1 = Pessoa("Teste", 944)
        print(f"{p1.nome} possui {p1.idade}")
        # Add uma nova idade
        p1.idade = 50
    except IdadeInvalidaError as erro:
        print(f"<ERRO> -> {erro}")

    # else do try:-> Só dispara se caso try tiver sucesso.   
    else:
        print(f"{p1.nome} possui {p1.idade} anos.")
    finally:
        print(f"Fim !")
    

if __name__ == "__main__":
    main()

# ============================================================
# Exercício de POO + Exceções Personalizadas
#
# Este arquivo é responsável pela execução do exercício.
# A classe Pessoa e a exceção personalizada são importadas
# do arquivo "classes.py".
# ============================================================

# Importa as classes disponíveis no módulo "classes".
from classes import *


# Função principal: organiza a execução do programa
# e realiza os testes com a classe Pessoa.
def main():
    # O bloco "try" contém o código que pode gerar uma exceção.
    try:
        # Cria um objeto da classe Pessoa.
        #
        # Neste exemplo, a idade 944 será rejeitada pelo setter,
        # pois a regra permite somente valores entre 1 e 99.
        p1 = Pessoa("Teste", 944)

        # Esta linha só será executada caso a criação da pessoa
        # tenha sido realizada sem gerar uma exceção.
        print(f"{p1.nome} possui {p1.idade}")

        # Altera a idade da pessoa.
        #
        # Como "idade" possui um setter, essa atribuição também
        # passa pela validação definida na classe Pessoa.
        p1.idade = 50

    # Captura especificamente a exceção personalizada
    # criada no arquivo "classes.py".
    except IdadeInvalidaError as erro:
        # Exibe a mensagem armazenada na exceção.
        print(f"<ERRO> -> {erro}")

    # O "else" é executado somente quando o bloco "try"
    # termina sem gerar nenhuma exceção.
    else:
        print(f"{p1.nome} possui {p1.idade} anos.")

    # O "finally" é executado independentemente de ocorrer
    # ou não uma exceção.
    finally:
        print("Fim !")


# Garante que a função main() seja executada somente quando
# este arquivo for executado diretamente, e não quando for importado.
if __name__ == "__main__":
    main()
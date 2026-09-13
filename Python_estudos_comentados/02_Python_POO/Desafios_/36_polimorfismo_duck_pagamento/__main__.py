
# Importa todas as classes e funções disponíveis no módulo "Classes".
from Classes import *


# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():

    # Cria um objeto da classe Boleto.
    p1 = Boleto()

    # Executa o método "pagar()" passando o valor do pagamento.
    print(p1.pagar(9000))
    
    # Utilizando o método 'duck'
    # A função "finalizar_compra()" recebe o objeto e utiliza o método "pagar()"
    # sem precisar saber qual é o tipo específico do objeto.
    finalizar_compra(Boleto(), 98_1233)
    finalizar_compra(Pix(), 3444)


# Garante que a função main() seja executada somente quando este arquivo
# for executado diretamente, e não quando for importado por outro arquivo.
if __name__ == "__main__":
    main()


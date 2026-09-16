# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
from Funcionario import *

def main():
    f = Desenvolvedor("José", 5_000)
    g = Gerente("Maria", 11_000)

    # Tentando modificar o salário
    try:
        g.salario = 11_500 # -> ok
        f.salario = 4_500 # -> erro
    except Exception as error:
        print(error)

    print(f)
    print(g)


    # lista_funcionarios = [

    #     Desenvolvedor("Noah", 5_000),
    #     Gerente("Arthur", 12_000),
    #     Designer("Ana", 14_500)
    # ]

    # for f in lista_funcionarios:
    #     print(f)
if __name__ == "__main__":
    main()


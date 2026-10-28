# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from carteira_property import *

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():

    c1 = Carteira(100)
    c2 = Carteira(100)

    # Operadores subistituidos com método mágico __metodo__

    # __eq__ igual 
    print(c1==c2) 

    
    # p1.__iadd__(p2) +=
    c1 += 6 
    print(c1)

    # p1.__isub__(p2) -=
    c2 -= 10
    print(c2)



if __name__ == "__main__":
    main()
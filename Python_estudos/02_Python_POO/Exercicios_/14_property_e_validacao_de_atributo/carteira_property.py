# ============================================================

# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

from functools import singledispatchmethod


# A classe Carteira representa uma carteira que possui um saldo.
# O saldo será armazenado de forma privada através de __saldo.

class Carteira:

    # O método __init__ inicializa o objeto.
    # O valor recebido pode ser int ou float e, caso nenhum valor
    # seja informado, o saldo será iniciado em 0.

    def __init__(self, valor: int | float = 0):

        self.__saldo = valor


    # O método __str__ define o que será exibido quando o objeto
    # Carteira for passado para print().
    #
    # A property saldo é utilizada para consultar o saldo.

    def __str__(self):

        return f"Você tem R${self.saldo:,.2f} na Carteira."


    # A @property transforma o método saldo() em uma propriedade.
    # Dessa forma, podemos consultar o saldo utilizando:
    #
    # carteira.saldo
    #
    # sem precisar utilizar:
    #
    # carteira.saldo()

    @property

    def saldo(self):

        return self.__saldo


    # O @saldo.setter define o comportamento quando alguém tenta
    # alterar diretamente a propriedade saldo.
    #
    # Neste exercício, a alteração direta não é permitida e um
    # PermissionError será lançado.

    @saldo.setter

    def saldo(self, valor):

        raise PermissionError(f"Você não tem permissão para alterar o saldo.")


    # Métodos Mágicos de operadores
    #
    # Os métodos mágicos permitem definir como os operadores do
    # Python irão funcionar quando utilizados com objetos da classe.


    # __eq__ representa o operador ==.
    #
    # carteira1 == carteira2
    #
    # é equivalente a:
    #
    # carteira1.__eq__(carteira2)
    #
    # Neste exercício, a comparação é feita através do saldo.

    def __eq__(self, other):

        # Testando igualdade pelo valor do saldo

        if self.__saldo == other.__saldo:

            return True

        else:

            return False


    # __iadd__ representa o operador +=.
    #
    # carteira += valor
    #
    # é equivalente a:
    #
    # carteira.__iadd__(valor)
    #
    # O saldo é aumentado pelo valor recebido.

    def __iadd__(self, valor: int | float):

        self.__saldo = self.__saldo + valor

        return self


    # __isub__ representa o operador -=.
    #
    # carteira -= valor
    #
    # é equivalente a:
    #
    # carteira.__isub__(valor)
    #
    # O saldo é diminuído pelo valor recebido.

    def __isub__(self, other: int | float):

        self.__saldo = self.__saldo - other

        return self


    # __le__ representa o operador <=.
    #
    # carteira1 <= carteira2
    #
    # é equivalente a:
    #
    # carteira1.__le__(carteira2)
    #
    # Neste exercício, a comparação é feita utilizando o saldo
    # das duas carteiras.

    def __le__(self, other):

        if self.__saldo <= other.__saldo:

            return True

        else:

            False


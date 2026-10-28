# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

# As classes abaixo possuem um método chamado abrir().
# Mesmo sendo classes diferentes e tendo comportamentos diferentes,
# todas possuem o mesmo método que poderá ser utilizado pelo Duck Typing.


class Porta:

    # O método abrir() define o comportamento da classe Porta
    # quando tentamos "abrir" um objeto desse tipo.

    def abrir(self):

        print('Girar a maçaneta e empurrar/puxar a porta.')


# A classe Empresa também possui um método abrir().
# O comportamento é diferente da classe Porta, mas o nome do método
# é o mesmo, permitindo que ela seja utilizada pelo Duck Typing.

class Empresa:

    def abrir(self):

        print('Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ.')


# A classe Ovo também possui um método abrir().
# Novamente, o comportamento é diferente, mas a interface utilizada
# pela função será a mesma: objeto.abrir().

class Ovo:

    def abrir(self):

        print('Quebre a casca com um garfo e mecha.')


# A classe Pedra não possui o método abrir().
# Ela será utilizada para demonstrar o que acontece quando um objeto
# não possui o comportamento esperado pela função.

class Pedra:

    pass


# Método Duck Typing
# A função recebe qualquer objeto como argumento.
# Ela não exige que o objeto pertença a uma classe específica.
#
# A função simplesmente tenta utilizar o método abrir() do objeto.
# Se o objeto possuir esse método, seu comportamento será executado.

def tentar_abrir(objeto):

    try:

        objeto.abrir()

    except:

        # __class__ permite acessar a classe à qual o objeto pertence.
        # __name__ retorna o nome dessa classe como uma string.
        #
        # Exemplo:
        # objeto.__class__.__name__ -> 'Pedra'
        #
        # Dessa forma, conseguimos informar qual foi o tipo de objeto
        # que apresentou problema ao tentar utilizar o método abrir().

        print(f'Problemas ao abrir um objeto tipo {objeto.__class__.__name__}')


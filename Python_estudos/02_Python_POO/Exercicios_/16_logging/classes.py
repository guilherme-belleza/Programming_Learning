# Exceção personalizada para representar uma idade inválida.
#
# Ela herda de Exception, que é a classe base das exceções 
# que podemos criar e tratar no Python.
class IdadeInvalidaError(Exception):
    pass


class Pessoa:

    def __init__(self, nome: str, idade: int):

        # Armazena o nome da pessoa.
        self.nome = nome

        # Inicializa o atributo interno que realmente armazenará a idade.
        #
        # O "_" indica que esse atributo é de uso interno/protegido por convenção.
        self._idade = None

        # Aqui utilizamos a propriedade "idade", 
        # e não diretamente o atributo "_idade".
        #
        # Por isso, essa atribuição passa pelo setter:
        #
        #     @idade.setter
        #
        # Dessa forma, a idade recebida será validada antes de ser
        # armazenada em _idade.
        self.idade = idade

    @property
    def idade(self):

        # Retorna o valor armazenado internamente em _idade.
        return self._idade

    @idade.setter
    def idade(self, valor):

        # Verifica se o valor é um inteiro e se está
        # dentro do intervalo permitido.
        #
        # Exemplo válido:
        #     25
        #
        # Exemplos inválidos:
        #     -10
        #     0
        #     100
        #     "25"
        if isinstance(valor, int) and 1 <= valor <= 99:

            # Se passou pela validação, armazenamos o valor.
            self._idade = valor

        else:

            # Se o valor for inválido, interrompemos o fluxo
            # lançando nossa exceção personalizada.
            #
            # Essa exceção será capturada no main.py pelo:
            #
            #     except IdadeInvalidaError as erro
            #
            # A mensagem abaixo poderá ser acessada através
            # da variável "erro".
            raise IdadeInvalidaError(
                f"Idade {valor} inválida! informe uma idade coerente (positivo e menor que 99)."
            )
         

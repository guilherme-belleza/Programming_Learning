#Nível 2 — Mini sistema: Caixa Eletrônico

# Importamos locale para trabalhar com a formatação de valores
# de acordo com a localização/região definida no sistema.
import locale


# ============================================================
# EXCEÇÕES PERSONALIZADAS
# ============================================================

# Exceção utilizada quando o saldo disponível não é suficiente
# para realizar uma operação de saque.
#
# Ela herda de Exception, que é a classe base das exceções
# que podemos criar no Python.
class SaldoInsuficienteError(Exception):
    pass


# Exceção utilizada quando um valor informado para uma
# operação não é considerado válido.
class ValorInvalidoError(Exception):
    pass


# ============================================================
# CLASSE CONTA
# ============================================================

class Conta:

    def __init__(self, titular: str, saldo: float | int):

        # Armazena o nome do titular da conta.
        self.titular = titular

        # Inicializa o atributo interno que realmente armazenará
        # o saldo.
        #
        # O "_" indica que esse atributo é de uso interno/protegido
        # por convenção.
        #
        # Inicializamos como None antes de atribuir o valor recebido
        # porque o valor será passado pela property "saldo".
        self._saldo = None

        # Aqui não atribuímos diretamente:
        #
        #     self._saldo = saldo
        #
        # Utilizamos a property:
        #
        #     self.saldo = saldo
        #
        # Dessa forma, a atribuição passa pelo setter de "saldo",
        # permitindo que o valor seja validado antes de ser armazenado.
        self.saldo = saldo


    # ========================================================
    # PROPERTY SALDO
    # ========================================================

    @property
    def saldo(self):
        # Getter da property "saldo".
        #
        # Quando acessarmos:
        #
        #     conta.saldo
        #
        # este método será executado e retornará o valor armazenado
        # no atributo interno "_saldo".
        return self._saldo


    @saldo.setter
    def saldo(self, valor: float | int):

        # Verifica se o valor recebido é do tipo float ou int.
        #
        # O segundo argumento do isinstance() recebe uma tupla
        # contendo os tipos que serão aceitos.
        if isinstance(valor, (float, int)):

            # Verifica se o valor é maior que zero.
            #
            # Somente valores positivos serão aceitos como saldo
            # inicial da conta.
            if valor > 0:

                # Se o valor for válido, ele é armazenado
                # no atributo interno "_saldo".
                self._saldo = valor

            else:

                # Se o valor for zero ou negativo, levantamos
                # nossa exceção personalizada.
                raise ValorInvalidoError(
                    f"ERRO '{valor}' -> Não é permitido aceitar valores negativos para saldo"
                )

        else:

            # Caso o valor não seja int nem float,
            # também levantamos a exceção personalizada.
            raise ValorInvalidoError(
                f"ERRO '{valor}' -> inválido para saldo."
            )


    # ========================================================
    # PROPERTY F_SALDO
    # ========================================================

    @property
    def f_saldo(self):

        # Define a localização utilizada pelo locale como
        # português do Brasil.
        #
        # Isso permite utilizar a formatação monetária brasileira.
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        # Formata o saldo atual da conta como moeda brasileira.
        #
        # grouping=True permite utilizar separadores para valores
        # maiores.
        f_saldo = locale.currency(self.saldo, grouping=True)

        # Retorna o valor formatado.
        return f_saldo


    # ========================================================
    # MÉTODO SACAR
    # ========================================================

    def sacar(self, valor: float | int):

        # Verifica se o valor que será sacado é menor ou igual
        # ao saldo disponível.
        if valor <= self.saldo:

            # Diminui o valor do saque do saldo atual.
            #
            # Como "saldo" possui setter, a atribuição passa
            # novamente pela property.
            self.saldo -= valor

            # Define a localização como português do Brasil
            # para utilizar a formatação monetária.
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

            # Retorna uma mensagem informando que o saque
            # foi realizado e mostrando o saldo atualizado.
            return (
                f'Saque de {locale.currency(valor, grouping=True)}. '
                f'Realizado com sucesso\n'
                f'SALDO atual de {locale.currency(self.saldo, grouping=True)}'
            )

        else:

            # Caso o valor do saque seja maior que o saldo,
            # levantamos nossa exceção personalizada.
            raise SaldoInsuficienteError(
                f"SAQUE de {valor} não realizado.\n"
                f"SALDO insuficiente"
            )


    # ========================================================
    # MÉTODO DEPOSITAR
    # ========================================================

    def depositar(self, valor: float | int):

        # Verifica se o valor informado é do tipo float ou int.
        if isinstance(valor, (float, int)):

            # O depósito precisa ser de pelo menos 1.
            if valor >= 1:

                # Define o novo saldo através da property.
                #
                # A atribuição passará pelo setter de "saldo".
                self.saldo = valor

            else:

                # Caso o valor seja menor que 1,
                # levantamos a exceção personalizada.
                raise ValorInvalidoError(
                    f"Valor {valor} inválido para depósito, "
                    f"informe um valor positivo."
                )

        else:

            # Caso seja informado algo que não seja int ou float,
            # também levantamos a exceção personalizada.
            raise ValorInvalidoError(
                f"Valor {valor} inválido para depósito, "
                f"informe ápenas números"
            )


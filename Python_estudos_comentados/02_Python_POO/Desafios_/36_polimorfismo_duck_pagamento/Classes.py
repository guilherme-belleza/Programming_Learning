# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

# PAGAMENTO
# Classe abstrata que serve como estrutura base para os diferentes tipos de pagamento.
# As subclasses deverão implementar o método "pagar()".

# Importamos ABC para criar uma classe abstrata e abstractmethod
# para definir métodos que deverão ser implementados pelas subclasses.
from abc import ABC, abstractmethod

# Importamos locale para trabalhar com a formatação de valores
# de acordo com a localização/região definida no sistema.
import locale


# A classe `Pagamento` representa uma entidade/estrutura do exercício
# e reúne dados e comportamentos comuns aos tipos de pagamento.
class Pagamento(ABC):
    def __init__(self):
        # Atributo privado responsável por armazenar o valor do pagamento.
        self.__valor = None

        
    # @property permite acessar o atributo através de "obj.valor"
    # sem acessar diretamente o atributo privado "__valor".
    @property
    def valor(self):
        return self.__valor


    # O setter permite controlar o momento em que "valor" recebe um novo valor.
    # Aqui ele também realiza uma validação antes de armazená-lo.
    @valor.setter
    def valor(self, valor: float|int):
        # O valor precisa ser maior que zero para ser aceito.
        if valor > 0:
            self.__valor = valor
        else:
            raise ValueError (
                f'O valor precisa ser positivo.'
            )


    # Property responsável por fornecer o valor formatado como moeda.
    @property
    def fvalor(self):
        #return f"R${self.__valor:,.2f}"

        # Localização do meu sistema vai ser com caracteres UTF-8 em pt_BR
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self.__valor, grouping=True) # Vai agrupar (milhão,centena,...)
    

    # Método abstrato que define um comportamento obrigatório
    # para as classes que herdarem de Pagamento.
    @abstractmethod
    def pagar(self):
        pass


# Boleto herda de Pagamento e implementa sua própria versão de "pagar()".
class Boleto(Pagamento):
    def pagar(self, valor:float):
        try:
            self.valor = valor
            # Código p efetuar o pagamento 
            return f"Pagamento CONFIRMADO de {self.fvalor} via Boleto."
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via Boleto"



# Credito herda de Pagamento e implementa sua própria versão de "pagar()".
class Credito(Pagamento):
    def pagar(self, valor:float):
        try:
            self.valor = valor
            # Código p efetuar o pagamento 
            return f"Pagamento CONFIRMADO de {self.fvalor} via Crédito."
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via Crédito"


# Pix herda de Pagamento e implementa sua própria versão de "pagar()".
class Pix(Pagamento):
    def pagar(self, valor:float):
        try:
            self.valor = valor
            # Código p efetuar o pagamento 
            return f"Pagamento CONFIRMADO de {self.fvalor} via Pix."
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via Pix"
        
# PATO
# A função não precisa saber qual é o tipo específico do pagamento.
# Ela apenas utiliza o comportamento "pagar()" que o objeto fornece.
def finalizar_compra(tipo_pag:Pagamento, valor:float):
    print(tipo_pag.pagar(valor))


# A ideia central pra fixar:
# Pagamento define a estrutura comum.
# Boleto, Credito e Pix implementam o comportamento "pagar()" de suas próprias formas.
# O método "finalizar_compra()" pode trabalhar com qualquer um deles,
# pois todos possuem o método "pagar()".

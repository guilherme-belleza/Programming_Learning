# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from abc import ABC, abstractmethod


# Classe abstrata que serve como base para os tipos de funcionário.
class Funcionario(ABC):

    def __init__(self, nome: str = None, salario: float | int = 1_600):
        self.nome = nome
        self._salario = salario

    # Método abstrato: as classes filhas devem implementar sua própria versão.
    @abstractmethod
    def calcular_bonus(self):
        pass


    # Getter: permite acessar o salário através de funcionario.salario.
    @property
    def salario(self):
        return self._salario


    # Setter: controla alterações no salário e impede redução.
    @salario.setter
    def salario(self, valor: float | int = None):

        if valor is None:
            raise ValueError("Nenhum valor informado para ajuste.")

        if valor >= self._salario:
            self._salario = valor
        else:
            raise ValueError(
                f"Não permitido diminuir o salário p/ um valor abaixo do atual."
            )


    # Representação textual do funcionário.
    def __str__(self):
        return (
            f"{self.nome} ganha R${self.salario:,.2f} "
            f"e por ser {self.__class__.__name__} o bônus será de {self.calcular_bonus():,.2f}"
        )


# Polimorfismo: cada classe implementa calcular_bonus() de uma forma.
class Desenvolvedor(Funcionario):  # 10% de bônus
    def calcular_bonus(self):
        return self.salario * 0.10


class Gerente(Funcionario):  # 15% de bônus
    def calcular_bonus(self):
        return self.salario * 0.15


class Designer(Funcionario):  # 8% de bônus
    def calcular_bonus(self):
        return self.salario * 0.08

    
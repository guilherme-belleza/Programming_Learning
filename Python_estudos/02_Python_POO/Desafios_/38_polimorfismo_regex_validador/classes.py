# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

from abc import ABC, abstractmethod
import re

class Validador(ABC):
    
    @abstractmethod
    def validar(self, valor: str):
        pass


class Usuario(Validador):

    def validar(self, valor: str) -> bool:
        regex = r"^[a-z0-9_]{5,20}$"
        if re.fullmatch(regex, valor):
            return True
        else:
            return False


class Senha(Validador):

    def validar(self, valor: str) -> bool:
        regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%¨&*]).{8,}$"
        if re.fullmatch(regex, valor):
            return True
        else:
            return False


class Email(Validador):

    def validar(self, valor: str) -> bool:
        regex = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}$"
        if re.fullmatch(regex, valor):
            return True
        else:
            return False


def validar_dado(validador: Validador, valor: str):
    resultado = validador.validar(valor)
    print(f"Valor: {valor} é válido? {'SIM' if resultado else 'NÃO'}")


# ============================================================
# EXPLICAÇÃO DOS CONCEITOS
# ============================================================

#region ABC e classe abstrata

# ABC significa Abstract Base Class (Classe Base Abstrata).
#
# A classe Validador funciona como uma classe base para os
# diferentes tipos de validadores do sistema.
#
# Ela não representa um validador específico. Sua função é
# estabelecer uma estrutura que as classes filhas deverão seguir.

#endregion


#region @abstractmethod

# O decorator @abstractmethod define um método abstrato.
#
# O método validar() funciona como um contrato:
# toda classe que herdar de Validador deverá implementar
# sua própria versão desse método.
#
# Por isso Usuario, Senha e Email possuem um método validar(),
# mas cada classe pode utilizar uma regra diferente.

#endregion


#region Herança

# Usuario, Senha e Email herdam de Validador:
#
# class Usuario(Validador)
# class Senha(Validador)
# class Email(Validador)
#
# Isso permite que essas classes compartilhem a mesma estrutura
# definida pela classe base.

#endregion


#region Polimorfismo

# O método validar() existe nas três classes, porém seu
# comportamento depende do objeto utilizado.
#
# Usuario -> valida um nome de usuário
# Senha   -> valida uma senha
# Email   -> valida um endereço de e-mail
#
# Essa possibilidade de utilizar o mesmo método com
# comportamentos diferentes é um exemplo de polimorfismo.

#endregion


#region Expressões Regulares

# O módulo re permite trabalhar com expressões regulares
# (Regex), utilizadas para procurar ou validar padrões
# dentro de strings.
#
# Cada classe possui uma expressão regular própria,
# representando as regras que aquele dado precisa seguir.

#endregion


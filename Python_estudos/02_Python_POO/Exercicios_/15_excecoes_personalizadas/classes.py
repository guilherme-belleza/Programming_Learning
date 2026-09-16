# ============================================================
# Exercício de POO + Exceções Personalizadas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

# Código executável.
class IdadeInvalidaError(Exception):
    pass

class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome

        self.idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self,valor):
        if isinstance(valor, int) and  1 <= valor <= 99:
            self._idade = valor
        else:
            raise IdadeInvalidaError(
                f"Idade {valor} invalída! informe uma idade coerente (positivo e menor que 100)."
            )


#region - Documentação do exercício.
# EXCEÇÃO PERSONALIZADA
# Criamos uma exceção própria para representar situações em que
# a idade informada não atende às regras definidas pela classe Pessoa.
#
# Ao herdar de Exception, a classe passa a se comportar como
# qualquer outra exceção do Python e pode ser utilizada com
# raise, try e except.
# class IdadeInvalidaError(Exception):
#     pass


# # PESSOA
# # A classe Pessoa representa uma pessoa e possui os atributos
# # nome e idade.
# #
# # O atributo "idade" será controlado através de uma property,
# # permitindo realizar uma validação antes de armazenar o valor.

# class Pessoa:
#     def __init__(self, nome: str, idade: int):
#         # Armazena o nome da pessoa.
#         self.nome = nome

#         # Como "idade" possui um setter, essa atribuição
#         # automaticamente chama o método responsável pela validação.
#         self.idade = idade

#     # @property permite acessar a idade através de "pessoa.idade"
#     # sem acessar diretamente o atributo protegido "_idade".
#     @property
#     def idade(self):
#         # Retorna o valor armazenado no atributo protegido "_idade".
#         return self._idade

#     # O setter permite controlar o momento em que "idade"
#     # recebe um novo valor.
#     #
#     # Neste caso, ele será utilizado para validar a idade
#     # antes de armazená-la.
#     @idade.setter
#     def idade(self, valor):
#         # Verifica se o valor é inteiro e está entre 1 e 99.
#         if isinstance(valor, int) and 1 <= valor <= 99:
#             # Depois da validação, o valor é armazenado
#             # no atributo protegido "_idade".
#             self._idade = valor
#         else:
#             # Caso o valor não atenda às regras definidas,
#             # uma exceção personalizada é lançada.
#             raise IdadeInvalidaError(
#                 f"Idade {valor} inválida! "
#                 f"Informe uma idade coerente (positivo e menor que 100)."
#             )
#endregion


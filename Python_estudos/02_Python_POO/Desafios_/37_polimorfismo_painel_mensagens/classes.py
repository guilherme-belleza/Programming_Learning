# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

# MENSAGEM 
# Classe mãe que serve como estrutura base para os diferentes tipos de exibição de mensagens.
# As subclasses deverão implementar o método "mostrar()".


# Importação da classe rich, permite o uso de cores facilitado no terminal.
from rich import print
from rich.panel import Panel


class Mensagem:
    def __init__(self, msg:str = '', tipo:str = 'aviso', icone:str = ':speech_balloon:'):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone

    # Método mostrar retorna um PAINEL personalizado.
    def mostrar(self):

        msg = Panel.fit(
             
             f"{self._mensagem}",
             title=f"{self._icone}[bold italic] {self._tipo.upper()}[/] {self._icone}",
             style="black on white"
        )
        return print(msg)
    


# Sub classes realizando o polimorfismo e exibindo um Painel customizado próprio.
class Erro(Mensagem):
    def __init__(self, msg):
         super().__init__(msg, tipo= "erro", icone= ':prohibited:')


    def mostrar(self):

        msg = Panel.fit(
                    
                    f"{self._mensagem}",
                    title=f"{self._icone}[bold italic] {self._tipo.upper()}[/] {self._icone}",
                    style="yellow on red"
            )
        return print(msg)
    

class Aviso(Mensagem):
    def __init__(self, msg):
        super().__init__(msg, tipo= 'alerta', icone= ':warning:')

    def mostrar(self):
        msg = Panel.fit(
                            
            f"{self._mensagem}",
            title=f"{self._icone}[bold italic] {self._tipo.upper()}[/] {self._icone}",
            style="green on black"
        )
        return print(msg)

    
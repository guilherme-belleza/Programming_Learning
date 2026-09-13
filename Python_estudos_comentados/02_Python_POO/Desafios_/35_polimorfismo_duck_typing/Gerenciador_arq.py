# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

from abc import ABC, abstractmethod

# Classe abstrata que serve como base para os tipos de arquivos.
class Arquivo(ABC):
    def __init__(self, nome:str, ext:str, tam:int = 0):
        self.nome = nome
        self._extensao = None
        self.tamanho = tam
        self.extensao = ext
       
    # Método abstrato
    @abstractmethod
    def abrir(self):
        pass


     # Property-Getter: permite acessar a _extensao.
    @property
    def extensao(self):
        return self._extensao
    
    # Setter só aceita os formatos válidos (pdf, docx)
    @extensao.setter
    def extensao(self, ext:str):
        formatos = ['pdf', "docx"]
        ext = ext.lower().strip()

        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError(
                f"O arquivo está em um formato não suportado."
            )

    # Property-Getter: permite acessar um nome formatado para exibição.    
    @property
    def nome_format(self):
        return f'"{self.nome}.{self.extensao}"({self.tamanho/1_000_000} MB)'


# Polimorfismo: cada classe implementa abrir() de uma forma.
class PDF(Arquivo):

    def __init__(self, nome:str, tam:int):
        super().__init__(nome, 'pdf', tam)
        
    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_format} no Adobe Reader.')


class DOC(Arquivo):
    def __init__(self, nome:str, tam:int):
        super().__init__(nome, 'docx', tam)

    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_format} no Word.')


# Método polimórfico / Tipo PATO =P

def abrir_arquivo(arquivo):
    arquivo.abrir()
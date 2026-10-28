
# ============================================================
# Exercício de Arquivos e Dados
#
# Este arquivo faz parte do material de estudo e registra uma
# etapa do aprendizado. Os comentários explicam as responsabilidades
# das classes e os conceitos utilizados, sem alterar a lógica.
# ============================================================

class Aluno:
    def __init__(self, nome: str = '', curso: str = '', serie: str = ''):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class Usuario:
    def __init__(self, nome: str = '', email: str = ''):
        self.nome = nome
        self.email = email


class JSON:
    def exportar(self, dados):
        from json import dumps

        lista = []
        for item in dados:
            lista.append(item.__dict__)

        txt = dumps(lista, ensure_ascii=False, indent=2)
        return txt


class XML:
    def exportar(self, dados):
        import xml.etree.ElementTree as ET

        nome = dados[0].__class__.__name__.lower()
        pai = ET.Element("dados")

        for item in dados:
            filho = ET.SubElement(pai, nome)

            for chave, valor in item.__dict__.items():
                neto = ET.SubElement(filho, chave)
                neto.text = str(valor)

            ET.indent(pai, space='\t')
            txt = ET.tostring(
                pai,
                encoding="unicode",
                xml_declaration=True
            )
            return txt


def exportar_dados(formato, dados):
    print(formato.exportar(dados))


#region Documentação do exercício

# ============================================================
# 1. CLASSES DE MODELO: ALUNO E USUARIO
# ============================================================
# As classes Aluno e Usuario representam os dados que serão
# exportados.
#
# O método __init__ inicializa os atributos de cada objeto.
# Os Type Hints indicam que os atributos recebem strings.
# Os valores padrão permitem criar objetos sem informar todos
# os argumentos.
#
# ============================================================
# 2. CLASSE JSON
# ============================================================
# A classe JSON é responsável por transformar os objetos em
# uma representação textual no formato JSON.
#
# from json import dumps:
# Importa a função que converte objetos compatíveis com JSON
# em uma string.
#
# item.__dict__:
# Retorna um dicionário com os atributos armazenados no objeto.
# Por exemplo, um Usuario pode ser representado por:
# {"nome": "Jose", "email": "jose@gmail.com"}
#
# lista.append(...):
# Adiciona à lista os dados de cada objeto recebido.
#
# ensure_ascii=False:
# Permite manter caracteres Unicode, como acentos, no texto.
#
# indent=2:
# Organiza o JSON com indentação de dois espaços, facilitando
# a leitura.
#
# return txt:
# Devolve o JSON gerado para quem chamou o método.
#
# ============================================================
# 3. CLASSE XML
# ============================================================
# A classe XML transforma os atributos dos objetos em uma
# estrutura de elementos XML.
#
# import xml.etree.ElementTree as ET:
# Importa a biblioteca padrão utilizada para construir e
# serializar estruturas XML.
#
# dados[0].__class__.__name__.lower():
# Obtém o nome da classe do primeiro objeto, transforma o nome
# em letras minúsculas e utiliza esse resultado como nome
# dos elementos que representam os objetos.
#
# ET.Element("dados"):
# Cria o elemento raiz da estrutura XML.
#
# ET.SubElement(...):
# Cria elementos filhos dentro de um elemento existente.
# Neste exercício, os atributos dos objetos viram elementos
# XML, e seus valores são armazenados no texto desses elementos.
#
# str(valor):
# Converte o valor para string, pois o conteúdo textual dos
# elementos XML precisa ser representado como texto.
#
# ET.indent(...):
# Organiza a indentação da estrutura XML para facilitar a leitura.
#
# ET.tostring(...):
# Converte a estrutura XML em uma string.
#
# encoding="unicode":
# Solicita o resultado como uma string Python.
#
# xml_declaration=True:
# Solicita a declaração XML no início do documento.
#
# ============================================================
# 4. FUNÇÃO exportar_dados
# ============================================================
# Recebe dois argumentos:
# - formato: objeto responsável pela exportação;
# - dados: coleção de objetos que será exportada.
#
# formato.exportar(dados):
# Chama o método exportar do objeto recebido.
#
# Essa organização permite utilizar diferentes formatos com
# a mesma função, desde que cada formato disponibilize um
# método exportar compatível.
#
#endregion


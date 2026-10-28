
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

        txt = dumps(lista, ensure_ascii=False, indent= 2)
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

            ET.indent(pai, space= '\t')
            txt = ET.tostring(pai, encoding= "unicode", xml_declaration= True)
            return txt


def exportar_dados(formato, dados):
    print(formato.exportar(dados))



#region Classes de modelo

# A classe Aluno representa um aluno e armazena seu nome,
# curso e série.
#
# A classe Usuario representa um usuário e armazena seu nome
# e e-mail.
#
# O método __init__ é executado durante a criação do objeto.
# Os parâmetros possuem valores padrão, permitindo criar
# objetos sem informar todos os argumentos.
#
# As anotações : str indicam que os parâmetros são esperados
# como strings, mas não fazem validação automática dos valores.
#
# O uso de self.nome, self.curso e self.serie cria atributos
# de instância, cujos valores pertencem a cada objeto.

#endregion

#region Exportação para JSON

# A classe JSON é responsável por converter os dados recebidos
# em uma representação no formato JSON.
#
# O método exportar recebe uma coleção de objetos.
#
# O atributo especial __dict__ fornece um dicionário com os
# atributos de instância de cada objeto.
#
# O laço percorre os objetos e adiciona seus dicionários à lista.
# Assim, a lista passa a conter estruturas que o JSON consegue
# serializar nesse caso.
#
# A função dumps converte a lista Python em uma string JSON.
#
# ensure_ascii=False preserva caracteres como acentos.
# indent=2 organiza a saída com indentação de dois espaços.
#
# O método retorna a string gerada, em vez de imprimi-la
# diretamente. Isso permite que outra parte do programa decida
# como utilizar o resultado.

#endregion

#region Exportação para XML

# A classe XML utiliza o módulo ElementTree para construir
# uma estrutura de elementos XML.
#
# O nome da classe do primeiro objeto é obtido por meio de
# __class__.__name__ e convertido para letras minúsculas.
#
# ET.Element("dados") cria o elemento raiz do documento.
# ET.SubElement cria elementos filhos ligados a um elemento
# existente.
#
# Para cada objeto, o código cria um elemento com o nome
# definido anteriormente. Em seguida, percorre os atributos
# do objeto usando __dict__.items(), obtendo cada chave e valor.
#
# Cada atributo vira um elemento XML, e seu conteúdo é
# definido por neto.text. O valor é convertido para string
# porque o conteúdo textual de um elemento XML é texto.
#
# ET.indent organiza a estrutura com indentação.
# ET.tostring converte a árvore XML em uma string.
#
# ATENÇÃO: o return está dentro do primeiro laço. Portanto,
# a função termina na primeira iteração e não processa os
# demais objetos. Além disso, dados[0] exige uma coleção
# não vazia.

#endregion

#region Polimorfismo

# A função exportar_dados recebe dois argumentos:
# formato, que representa o objeto responsável pela exportação,
# e dados, que representa a coleção a ser exportada.
#
# A chamada formato.exportar(dados) utiliza o método exportar
# do objeto recebido, sem precisar verificar se ele é JSON ou XML.
#
# Como as duas classes oferecem um método com o mesmo nome,
# a função pode trabalhar com ambas. Esse é um exemplo de
# polimorfismo por interface comum, baseado no comportamento
# do objeto recebido.
#
# print exibe a string retornada pelo método exportar.

#endregion

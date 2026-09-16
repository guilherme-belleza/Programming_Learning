# Exercício 2 — Primeiro log
# Configure o logging para salvar mensagens em um arquivo.
# Sempre que uma Pessoa for criada com sucesso, registre um log INFO.
# Quando a criação falhar, registre um log ERROR.

import logging
import os
from classes import *


def main():
    caminho_main = os.path.dirname(os.path.abspath(__file__))
    caminho_log = os.path.join(caminho_main, "Relatório.log")
    
    print(caminho_main)
    print(caminho_log)
    # Configuração do logging.
    #
    # filename -> define o arquivo onde os logs serão salvos.
    # level -> define o nível mínimo de mensagens que serão registradas.
    # format -> define como cada registro aparecerá no arquivo.
    #
    # Como usamos logging.INFO, serão registrados:
    # INFO, WARNING, ERROR e CRITICAL.


    logging.basicConfig(
        filename=caminho_log,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    try:

        # Tentamos criar uma Pessoa.
        # A criação do objeto chama automaticamente o __init__() da classe Pessoa.
        # Como a idade -33 é inválida, o setter de idade irá, lançar a exceção IdadeInvalidaError.
        p1 = Pessoa("Teste", -33)

        # Só chegaremos aqui se a Pessoa for criada com sucesso.
        
        # logging.info() registra uma mensagem de nível INFO no arquivo configurado anteriormente.
        logging.info(f"{p1.nome} registrado com sucesso !")

        print(f"{p1.nome} possui {p1.idade}")

        # Tentativa de alterar a idade depois da criação.
        # Essa atribuição também passa pelo setter da propriedade
        # idade e será validada novamente.

        p1.idade = -50

    # Capturamos especificamente a exceção personalizada IdadeInvalidaError.

    # A palavra "as erro" coloca a própria exceção dentro da variável erro.
    except IdadeInvalidaError as erro:

        # Registramos o erro no arquivo de log.
        #
        # {erro} representa a mensagem que foi enviada
        # quando fizemos raise IdadeInvalidaError(...).
        logging.error(f"Erro ao criar a pessoa {erro}")

        # Também mostramos o erro diretamente no terminal.
        print(f"<ERRO> -> {erro}")

    # O else só é executado se NENHUMA exceção ocorrer dentro do bloco try.
    else:
        print(f"{p1.nome} possui {p1.idade} anos.")

    # O finally sempre será executado.
    #
    # Tanto faz se o try deu certo ou se caiu no except.
    finally:
        print(f"Fim !")


# Verifica se este arquivo está sendo executado diretamente.
#
# Se estiver, chama a função main().
if __name__ == "__main__":
    main()


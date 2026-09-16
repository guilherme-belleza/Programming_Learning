# Importamos as classes e exceções que estão no arquivo "classes.py".
from classes import *


# Importamos a biblioteca logging para registrar as operações
# realizadas pelo sistema.
import logging
# Importamos a biblioteca os para trabalhar com caminhos
# de arquivos e diretórios.
import os


# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================

def main():
    
    # Código pra pegar o diretório do main.
    caminho_main = os.path.dirname(os.path.abspath(__file__))

    # Junta o caminho da pasta do main.py com o nome do arquivo de log.
    caminho_log = os.path.join(caminho_main, "Relatório_caixa.log")

    print(caminho_main) 
    print(caminho_log)

    # Configuração básica do sistema de logging.

    logging.basicConfig(

        filename=caminho_log, # Informando o diretório do log.

        level=logging.INFO,

        format="%(asctime)s - %(levelname)s - %(message)s"
    )


    # ========================================================
    # CRIAÇÃO DA CONTA
    # ========================================================

    try:

        # Cria uma conta com um saldo inicial válido.
        conta_1 = Conta("João", 50)


        # Exibe os dados da conta no terminal.
        #
        # f_saldo é uma property criada para tentar retornar
        # o saldo formatado como moeda.
        print(
            f"Titular: {conta_1.titular.title()} "
            f"SALDO: {conta_1.f_saldo} "
            f"Registrado com sucesso."
        )


        # Registra a criação da conta no arquivo de log.
        logging.info(
            f"Titular: {conta_1.titular.title()} "
            f"SALDO: {conta_1.saldo} "
            f"Registrado com sucesso."
        )


        # ====================================================
        # TESTE 1 — SAQUE VÁLIDO
        # ====================================================

        try:

            # O saldo é 50.
            #
            # Portanto, um saque de 20 deve ser realizado
            # normalmente.
            resultado = conta_1.sacar(20)

            print(resultado)

            # Registra o sucesso da operação.
            logging.info(
                "SAQUE de 20 realizado com sucesso."
            )

        except SaldoInsuficienteError as erro:

            # Mostra o erro no terminal.
            print(erro)

            # Registra o erro no arquivo de log.
            logging.warning(
                f"Falha no saque: {erro}"
            )


        # ====================================================
        # TESTE 2 — SAQUE MAIOR QUE O SALDO
        # ====================================================

        # Depois do saque anterior, o saldo será 30.
        #
        # Descomente para testar a exceção
        # SaldoInsuficienteError.
        #
        # try:
        #
        #     resultado = conta_1.sacar(100)
        #
        #     print(resultado)
        #
        #     logging.info(
        #         "SAQUE de 100 realizado com sucesso."
        #     )
        #
        # except SaldoInsuficienteError as erro:
        #
        #     print(erro)
        #
        #     logging.warning(
        #         f"Falha no saque: {erro}"
        #     )


        # ====================================================
        # TESTE 3 — DEPÓSITO VÁLIDO
        # ====================================================

        # Descomente para testar um depósito válido.
        #
        # try:
        #
        #     conta_1.depositar(50)
        #
        #     print(
        #         f"Depósito de 50 realizado com sucesso."
        #     )
        #
        #     logging.info(
        #         "DEPÓSITO de 50 realizado com sucesso."
        #     )
        #
        # except ValorInvalidoError as erro:
        #
        #     print(erro)
        #
        #     logging.warning(
        #         f"Falha no depósito: {erro}"
        #     )


        # ====================================================
        # TESTE 4 — DEPÓSITO INVÁLIDO
        # ====================================================

        # O método depositar() possui uma validação:
        #
        #     if valor >= 1:
        #
        #     else:
        #         raise ValorInvalidoError(...)
        #
        # Portanto, um valor como 0 deve cair no ELSE.
        #
        # Descomente para testar.
        #
        # try:
        #
        #     conta_1.depositar(0)
        #
        #     logging.info(
        #         "DEPÓSITO de 0 realizado com sucesso."
        #     )
        #
        # except ValorInvalidoError as erro:
        #
        #     print(erro)
        #
        #     logging.warning(
        #         f"Falha no depósito: {erro}"
        #     )


        # ====================================================
        # TESTE 5 — DEPÓSITO COM TIPO INVÁLIDO
        # ====================================================

        # O primeiro IF do método depositar() verifica:
        #
        #     isinstance(valor, (float, int))
        #
        # Como "abc" é uma string, essa condição será False
        # e o segundo ELSE será executado.
        #
        # Descomente para testar.
        #
        # try:
        #
        #     conta_1.depositar("abc")
        #
        #     logging.info(
        #         "DEPÓSITO realizado com sucesso."
        #     )
        #
        # except ValorInvalidoError as erro:
        #
        #     print(erro)
        #
        #     logging.warning(
        #         f"Falha no depósito: {erro}"
        #     )


        # ====================================================
        # TESTE 6 — CRIAÇÃO DE CONTA COM SALDO NEGATIVO
        # ====================================================

        # O setter de saldo possui:
        #
        #     if valor > 0:
        #
        #     else:
        #         raise ValorInvalidoError(...)
        #
        # Portanto, -500 deve cair no ELSE.
        #
        # Descomente para testar.
        #
        # try:
        #
        #     conta_teste = Conta("Teste", -500)
        #
        # except ValorInvalidoError as erro:
        #
        #     print(erro)
        #
        #     logging.error(
        #         f"ERRO ao criar uma conta: {erro}"
        #     )


        # ====================================================
        # TESTE 7 — CRIAÇÃO DE CONTA COM TIPO INVÁLIDO
        # ====================================================

        # Aqui estamos passando uma string no lugar do saldo.
        # O setter verificará:
        #
        #     isinstance(valor, (float, int))
        #
        # Como "100" é uma string, a condição será False
        # e o segundo ELSE será executado.
        #
        # Descomente para testar.
        #
        # try:
        #
        #     conta_teste = Conta("Teste", "100")
        #
        # except ValorInvalidoError as erro:
        #
        #     print(erro)
        #
        #     logging.error(
        #         f"ERRO ao criar uma conta: {erro}"
        #     )


    # ========================================================
    # EXCEÇÃO DA CRIAÇÃO DA CONTA PRINCIPAL
    # ========================================================

    except ValorInvalidoError as erro:

        # Mostra a mensagem da exceção no terminal.
        print(erro)

        # Registra o erro no arquivo de log.
        logging.error(
            f"ERRO ao criar uma conta {erro}"
        )


# ============================================================
# PONTO DE ENTRADA DO PROGRAMA
# ============================================================

# Verifica se este arquivo está sendo executado diretamente.
# Quando executamos "main.py", __name__ recebe "__main__".
# Nesse caso, chamamos a função main().
if __name__ == "__main__":
    main()


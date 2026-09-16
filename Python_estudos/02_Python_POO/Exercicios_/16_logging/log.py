# import logging

# CONFIGURAÇÃO BÁSICA DO LOG

# logging.basicConfig(
#     filename="pessoas.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# logging.basicConfig() -> É a configuração básica do sistema de logging.
# Dentro dela colocamos as opções que queremos.

#filename="pessoas.log" -> Os registros serão gravados nesse arquivo.


#level=logging.INFO -> Aqui estamos dizendo qual é o nível mínimo de mensagem que queremos registrar.

#DEBUG       → detalhes de desenvolvimento
#INFO        → funcionamento normal
#WARNING     → situação inesperada
#ERROR       → erro
#CRITICAL    → erro muito grave

# format="%(asctime)s - %(levelname)s - %(message)s" ->  Isso define como a mensagem será escrita no arquivo.

# %(asctime)s   → data e hora do evento.
# %(levelname)s → nível do log (INFO, ERROR, etc.).
# %(message)s   → a mensagem que você escreveu.
#
# exemplo -> 026-09-14 12:40:10,123 - INFO - Pessoa João criada com sucesso


# DEPOIS DA CONFIG BÁSICA DO LOG

# logging.info() -  -> para registrar um evento normal.
# logging.warning() -> para uma situação de atenção.
# logging.error()   -> para um erro.

# logging.info("João foi cadastrado")
# logging.warning("Tentativa de cadastro com dados incompletos")
# logging.error("Não foi possível cadastrar Maria")

import logging

logging.basicConfig(
    filename="teste.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Programa iniciado")
logging.warning("Isso é um aviso")
logging.error("Isso é um erro")

# - SAÍDA: 
# 2026-09-14 12:45:20,088 - INFO - Programa iniciado
# 2026-09-14 12:45:20,089 - WARNING - Isso é um aviso
# 2026-09-14 12:45:20,092 - ERROR - Isso é um erro
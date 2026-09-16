# Linux Básico para Desenvolvedores

## Sumário
1. [grep — buscar dentro de arquivos](#1-grep--buscar-dentro-de-arquivos)
2. [find — buscar arquivos e pastas](#2-find--buscar-arquivos-e-pastas)
3. [Pipes (`|`)](#3-pipes-)
4. [Redirecionamento (`>`, `>>`, `<`)](#4-redirecionamento---)
5. [Variáveis de ambiente](#5-variáveis-de-ambiente)
6. [Shell scripting básico](#6-shell-scripting-básico)
7. [Processos](#7-processos)
8. [SSH](#8-ssh)
9. [Serviços (systemd)](#9-serviços-systemd)
10. [Resumo rápido (cheat sheet)](#10-resumo-rápido-cheat-sheet)

---

## 1. grep — buscar dentro de arquivos

`grep` procura por um padrão de texto dentro de arquivos.

```bash
grep "erro" log.txt              # linhas que contêm "erro"
grep -i "erro" log.txt           # ignora maiúsculas/minúsculas
grep -r "TODO" src/              # busca recursiva em uma pasta
grep -n "erro" log.txt           # mostra o número da linha
grep -v "debug" log.txt          # inverte: mostra linhas que NÃO contêm "debug"
grep -E "erro|falha" log.txt     # usa regex (múltiplos padrões)
```

---

## 2. find — buscar arquivos e pastas

`find` localiza arquivos/pastas por nome, tipo, tamanho, data, etc.

```bash
find . -name "*.py"              # todos os .py a partir da pasta atual
find . -type d -name "testes"    # pastas chamadas "testes"
find . -type f -mtime -7         # arquivos modificados nos últimos 7 dias
find . -size +10M                # arquivos maiores que 10MB
find . -name "*.pyc" -delete     # encontra e apaga de uma vez (cuidado!)
```

---

## 3. Pipes (`|`)

O pipe conecta a **saída** de um comando à **entrada** do próximo, permitindo combinar ferramentas simples em uma tarefa mais complexa.

```bash
cat log.txt | grep "erro" | wc -l
# lê o arquivo -> filtra linhas com "erro" -> conta quantas linhas sobraram

ps aux | grep python
# lista processos -> filtra os que têm "python" no nome
```

---

## 4. Redirecionamento (`>`, `>>`, `<`)

```bash
python app.py > saida.txt      # redireciona a saída para um arquivo (sobrescreve)
python app.py >> saida.txt     # adiciona ao final do arquivo (não sobrescreve)
python app.py 2> erros.txt     # redireciona só os erros (stderr)
python app.py > tudo.txt 2>&1  # redireciona saída normal e erros para o mesmo arquivo
comando < entrada.txt          # usa um arquivo como entrada do comando
```

---

## 5. Variáveis de ambiente

São valores disponíveis para os programas rodando no sistema, geralmente usadas para configuração (chaves de API, modo de ambiente, caminhos).

```bash
echo $HOME              # mostra o valor de uma variável já existente
export MINHA_VAR="ola"  # cria/define uma variável de ambiente para a sessão atual
echo $MINHA_VAR
unset MINHA_VAR          # remove a variável

printenv                 # lista todas as variáveis de ambiente atuais
```

Em Python, para ler essas variáveis:

```python
import os
valor = os.getenv("MINHA_VAR", "valor_padrao")
```

> Ligação com o tutorial de estrutura de projeto: é assim que o `.env` e o `config.py` funcionam por trás dos panos — variáveis de ambiente sendo lidas pelo programa.

---

## 6. Shell scripting básico

Um script de shell é um arquivo de texto com uma sequência de comandos, executado de uma vez.

```bash
#!/bin/bash
# backup.sh — script simples de exemplo

echo "Iniciando backup..."

PASTA_ORIGEM="dados"
PASTA_DESTINO="backup"

mkdir -p "$PASTA_DESTINO"
cp -r "$PASTA_ORIGEM" "$PASTA_DESTINO"

if [ $? -eq 0 ]; then
    echo "Backup concluído com sucesso."
else
    echo "Erro ao fazer backup."
fi
```

```bash
chmod +x backup.sh   # torna o arquivo executável
./backup.sh           # executa o script
```

Estruturas básicas:

```bash
# Variável
NOME="mundo"
echo "Olá, $NOME"

# Condicional
if [ "$NOME" = "mundo" ]; then
    echo "É o mundo"
fi

# Loop
for arquivo in *.txt; do
    echo "Processando $arquivo"
done
```

---

## 7. Processos

Todo programa em execução é um **processo**, identificado por um PID (número único).

```bash
ps aux              # lista todos os processos rodando
ps aux | grep python  # filtra só os processos relacionados a python

top                  # monitor interativo de processos (uso de CPU/memória)
htop                  # versão mais amigável do top (se instalado)

kill 1234             # encerra o processo de PID 1234 (pedido "educado")
kill -9 1234           # força o encerramento (último recurso)

comando &              # roda o comando em segundo plano (background)
jobs                    # lista processos em background da sessão atual
nohup python app.py &   # roda em background e continua mesmo se fechar o terminal
```

---

## 8. SSH

SSH (*Secure Shell*) permite acessar e controlar outra máquina remotamente, de forma segura (criptografada) — essencial para trabalhar com servidores.

```bash
ssh usuario@servidor.com          # conecta ao servidor remoto
ssh -p 2222 usuario@servidor.com  # conecta em uma porta específica

# Copiar arquivos entre máquinas via SSH
scp arquivo.txt usuario@servidor.com:/pasta/destino/
scp -r pasta_local usuario@servidor.com:/pasta/destino/

# Autenticação por chave (mais segura que senha)
ssh-keygen -t ed25519              # gera um par de chaves (pública/privada)
ssh-copy-id usuario@servidor.com   # copia a chave pública para o servidor
```

Depois de configurada a chave, você consegue conectar sem digitar senha toda vez — e é assim que a maioria dos deploys em servidores/VPS funciona na prática.

---

## 9. Serviços (systemd)

Em servidores Linux modernos, `systemd` é o responsável por gerenciar **serviços** — programas que devem ficar rodando continuamente (ex: seu servidor Flask em produção, um banco de dados).

```bash
sudo systemctl start meuapp     # inicia o serviço
sudo systemctl stop meuapp      # para o serviço
sudo systemctl restart meuapp   # reinicia
sudo systemctl status meuapp    # mostra o status atual
sudo systemctl enable meuapp    # faz o serviço iniciar automaticamente com o sistema
```

Um serviço é definido por um arquivo de configuração simples, por exemplo `/etc/systemd/system/meuapp.service`:

```ini
[Unit]
Description=Minha aplicação Flask

[Service]
ExecStart=/usr/bin/python3 /home/usuario/app/app.py
Restart=always
User=usuario

[Install]
WantedBy=multi-user.target
```

Isso é o que garante que sua aplicação continue rodando mesmo após reiniciar o servidor, ou volte a funcionar sozinha caso trave — ligação direta com o tutorial de deploy.

---

## 10. Resumo rápido (cheat sheet)

```bash
grep -rn "padrao" pasta/
find . -name "*.py"

comando1 | comando2
comando > saida.txt
comando >> saida.txt

export VAR="valor"
echo $VAR

#!/bin/bash
echo "script simples"

ps aux
kill -9 PID
comando &

ssh usuario@host
scp arquivo usuario@host:/destino/

sudo systemctl start|stop|restart|status meuapp
```

# ============================================================
# Exercício de dicionários
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================


from time import sleep
from random import randint
from operator import itemgetter 

jogo = {

    "jogador1" : randint(1,6),
    "jogador2" : randint(1,6),
    "jogador3" : randint(1,6),
    "jogador4" : randint(1,6),
    "jogador5" : randint(1,6)
}

ranking = []

print(f'Valores Sorteados:')

for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(ranking)

for i, v in enumerate(ranking):
    print(f'{i+1}º-Lugar: {v[0]} com {v[1]}.')
    sleep(1)


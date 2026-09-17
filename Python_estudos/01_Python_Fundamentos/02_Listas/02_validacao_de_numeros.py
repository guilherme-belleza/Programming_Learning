# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercicio 2.

#Limpando a Lista: Crie uma lista com 8 números inteiros digitados pelo usuário.
#Se o usuário digitar um número negativo, o programa deve ignorá-lo e não adicioná-lo à lista.
#Ao final, mostre a lista resultante.

# Iniciando uma lista vazia
lista_numeros = [] 

# Um laço com 8 entradas como pede o exercício.
#range(1, 9) iniciando de 1 até o 8 (range desconsidera o ultímo número.)
for item in range(1 , 9):

    # Repete a entrada até o usuário informe um número inteiro válido.
    while True:
        entrada_numeros_str = input(f'Informe o {item}º número inteiro: ')

        # Verificando se a entrada é apenas números.
        if entrada_numeros_str.isdigit():

            # Converte STR em INT   
            entrada_numeros_int = int(entrada_numeros_str)

            # Sendo possível o cast, adiciona somente os números positivos a lista
            if entrada_numeros_int >= 0:
                lista_numeros.append(entrada_numeros_int)

            break# finaliza o laço 

        # Entrada incorreta.
        else:
            print(f'Resposta inválida. {entrada_numeros_str} não é um número inteiro.')

# Resposta final do exercicío.            
print(f'Lista e números desconsiderando os negativos ---> {lista_numeros}')


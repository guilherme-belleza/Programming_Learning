# ============================================================
# Exercício de laços de repetição
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercício 3:

#Contagem de PAR e IMPAR
#leia 10 números  e no final mostre QUANTOS são pares e impares

# Estrutura de listas.
lista_numeros = list()#
lista_par = list()
lista_impar = list()


for n in range(1 , 11):

    while True:
        entrada = input(f'Informe o {n}º número inteiro: ').strip()

        # Verifica se entrada é digito e converte pra INT e adiciona a lista.
        if entrada.isdigit():
            numero = int(entrada)
            lista_numeros.append(numero)
            break 

        # Informação caso entrada não seja númerica.
        else:
            print(f'O valor: "{entrada}" não é um número.\nInforme novamente !')


print('Ok vamos anlizar a quantidade de PARES e IMPARES dos valores informados.')

# Varredura da lista de númeors e adicionando os valores
# PARES e ÍMPARES em listas.
for valor in lista_numeros:
    
    if valor % 2 == 0:
        lista_par.append(valor)

    else:
        lista_impar.append(valor)

# Resuldados
print(f'Valores informados são: {lista_numeros}')
print(f'Foi informado {len(lista_par)} números PARES.\n PARES >>>> {lista_par}')
print(f'Foi informado {len(lista_impar)} números ÍMPARES.\n ÍMPARES >>>> {lista_impar}')


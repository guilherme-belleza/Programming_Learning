# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Exercicio 1. (Verificando > e < 

# # Leia o nome e o peso de varias pessoas, guardando em uma lista. no final mostre:
# #A)qntos foram salvas
# #B) Os mais pesados
# #C) Os mais leves


# Estruturas utilizadas para armazenar os dados das pessoas
# e controlar os maiores e menores pesos encontrados.
temp = []
pessoas = []
lista_maior = []
lista_menor = []
maior = menor = 0


#Laço infinito
while True:

    #lista temporaria recebendo o nome e peso
    temp.append(str(input('NOME: ')))
    temp.append(float(input(f'PESO: ')))

    
    if len(pessoas) == 0:
        #Menor e maior recebei o peso 
        maior = menor = temp[1]

    #se n foi o primeiro valor inserido
    else:
        if temp[1] > maior:#verifica se o peso é maior q a variavel vaior
            maior = temp[1]#a variavel maior vai receber esse novo peso maior
        if temp[1] < menor:#se o peso for menor q a variavel menor
            menor = temp[1]#a variavel menor vai receber o novo peso menor

    #Lista de pessoas recebendo uma copia da lista temp 
    pessoas.append(temp[:])
    temp.clear()

    #Condição de parada do laço
    r = str(input('Deseja continuar [S/N]: '))
    if r not in 'Ss':
        break


# Percorre as pessoas para identificar quais possuem o maior peso.
for p in pessoas:
    if p[1] == maior:
        lista_maior.append(p[0])
    if p[1] == menor:
        lista_menor.append(p[0])

print(f'Quantidade informada = {len(pessoas)}')
print(f'O maior peso foi de {lista_maior} com {maior}kg.')
print(f'O menor peso foi de {lista_menor} com {menor}kg.')


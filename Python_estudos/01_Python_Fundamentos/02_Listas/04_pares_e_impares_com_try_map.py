# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Exercicio 2. (Usando TRY e MAP{})

# Leia n valores númericos e cadastre em uma unica lista 
# que mantenha os valores separados entre PARES e IMPARES.
# No final mostre os valores en ordem crescente 


#Lista com 2 listras encadeadas
lista_num_final = [[],[]]

# Repetição para a leitura dos valores
for c in range(0,7):

    
    while True:

        # Só aceita entrada de valores inteiros.
        try:

            entrada_num = (int(input(f'Digite o {c+1}º Valor: '))) 

            # Se o valor é PAR e adiciona a lista[0] ->  PAR
            if entrada_num % 2 == 0:
                print(f'Valor {entrada_num} Adicionado com sucesso na lista de PAR.')
                lista_num_final[0].append(entrada_num)

             # Valor ÍMPAR é adicionado a lista[1] ->  ÍMPAR
            else:
                print(f'Valor {entrada_num} adicionado com sucesso na lista ÍMPAR.')
                lista_num_final[1].append(entrada_num)

            break

        # Informação sobre o ERRO na entrada.             
        except (ValueError, TypeError):
            print(f'Entrada inválida ! Informe apenas NÚMEROS.')
#Resultado
        
print(f'Valores informados em uma única lista ----> {lista_num_final}')
print(f'Valores PARES ----> {lista_num_final[0]}')
print(f'Valores ÍMPARES ----> {lista_num_final[1]}')


#Transformando em TEXTO para usar o .join

pares_texto = map(str, sorted(lista_num_final[0]))

print(f'Valores PARES EM ORDEM ----> {"| ".join(pares_texto)}')


#join colocando "-" entre os valores, depois o MAP mudando pra STR e colocando em ordem com SORTED
print(f'Valores ÍMPARES EM ORDEM ----> {"| ".join(map(str , sorted(lista_num_final[1])))}')


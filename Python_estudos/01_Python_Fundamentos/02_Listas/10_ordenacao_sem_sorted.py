# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#ExercicioGuanabara
#region
#Leia 5 valores númerios e cadastre em uma lista, jána posição correta de inserção (sem o SORT())

lista = []

for c in range(0, 4):
    n = int(input('Informe um valor: '))

    # Se for o primeiro valor (indice 0) 
    # lista append valor.   
    if c == 0:     
        lista.append(n)

    # Se a entrada for maior q o ultimo elemento da lista.
    # lista append valor
    elif n > lista[-1]:
        lista.append(n)

    else:

        pos = 0

        #Enquanto a pos for menor que o tamanho da lista.
        #Verificar se o N é menor ou igual do indice. 
        # e atualiza a lista.
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
               
                break
            pos =+ 1

print(f'Os valores digitados foram {lista}')


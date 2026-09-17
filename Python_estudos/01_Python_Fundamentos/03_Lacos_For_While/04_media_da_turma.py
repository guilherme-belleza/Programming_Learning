# ============================================================
# Exercício de laços de repetição
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

#Exercício 4:
#region
# Calcúlo de média: Leia quantos alunos tem na sala.
# Depois pedir a nota final de cada aluno.
# E no final mostrar a média da SALA !

lista_notas = [] #Criando uma lista vazia []

while True:

    # Entrada, validação e conversão do valor em INT 
    entrada = input('Quantidade de alunos: ').strip()  

    if entrada.isdigit():
        alunos = int(entrada)
        break

    else:
        print('Informação ínvalida.')


for p in range(1, alunos + 1):
    
    while True:

        # Se usar (,) trocar para (.)
        # Verifica se tem (.) na entrada e troca por ('') o 1 garante q remove só 1º ponto       
        entrada_2 = input(f'Nota final do {p}º Aluno: ').strip().replace(',', '.')
        entrada_semponto = entrada_2.replace('.','',1)

        # Converte a entrada para float e adiciona a lista
        if entrada_semponto.isdigit() and entrada_2.count('.')<=1:
            notas = float(entrada_2)            
            lista_notas.append(notas)
            break

        else:
            print(f'Nota inválida, Informe novamente')


media = sum(lista_notas) / len(lista_notas)
print(f'A média da sala com {alunos} alunos foi de {media:.2f}')


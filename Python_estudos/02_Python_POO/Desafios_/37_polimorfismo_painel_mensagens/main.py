from classes import *

def main():
    
    a = Mensagem('Olá mundo', 'aviso')
    a.mostrar()

    b = Erro("Não encontrado ! ")
    b.mostrar()


    c = Aviso("Está sem espaço !")
    c.mostrar()


if __name__ == "__main__":
    main()

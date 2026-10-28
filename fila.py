fila=[]
menu = 's:'
while menu == 's':
    print("Gestão do refeitório")
    print('Digite 1 para adicionar alguém no fim da fila')
    print('Digite 2 para adcionar alguém em uma posição da fila')
    print('Digte 3 para remover alguém da fila')
    print('Digite 4 para remover alguém em uma posição da fila')
    

    novo_nome = input('Digite um nome para ser adicionado à fila:')

    fila.append(novo_nome)

    for nome in fila:
        print(nome)

    menu = input("Deseja adicionar mais um nome? (s/n)")

#programa que escreve em um arquivo

arqv = open("dados.txt", "a")
continuar = True

while continuar:
    time = input("Time: [Vazio para sair]")
    if not time:
        continuar = False
        continue
    arqv.write(time+'\n')
arqv.close()
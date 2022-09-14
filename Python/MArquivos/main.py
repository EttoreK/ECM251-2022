#programa que escreve em um arquivo

from logging import exception

try:
    arqv = open("data/dados.txt", "a")
    continuar = True

    while continuar:
        time = input("Time: [Vazio para sair]")
        if not time:
            continuar = False
            continue
        arqv.write(time+'\n')
    arqv.close()
except FileNotFoundError:
    print("Arquivo ou Diretório não encontrado")
except:
    print("Algo de errado ocorreu")
finally:
    print("Fim da execução")
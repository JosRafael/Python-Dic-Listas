#Questão 01
nome = str(input("Digite um nome: "))
tam = len(nome)
espaco = 10  
for c in range(0, tam):
    espaco = espaco-1
    for d in range(espaco, 1, -1):
        print(" ",end="")
    for e in range(6, c+1):
        print(nome[e],end="")
    for f in range(6, c):
        print(nome[f],end="")
    print()
#Questão 02
cont = 1
lista = []
posicoes = []
while cont != 0:
    print('Digite (0), Se desejar parar.')
    num = int(input("Digite um número: "))
    cont = num
    if num != 0:
        lista.append(num)
    else:
        break
repeticoes = 0
maiorNum = 0

for i in range(0, len(lista)):
    if lista[i] >= maiorNum:
        maiorNum = lista[i]

for i in range(0, len(lista)):
    if lista[i] == maiorNum:
        repeticoes = repeticoes + 1

for i in range(0, len(lista)):
    if maiorNum == lista[i]:
        posicoes.append(i)

print()
print(f"Na lista {lista}, o maior número foi {maiorNum}, se repete {repeticoes} vezes nas posições: {posicoes}")
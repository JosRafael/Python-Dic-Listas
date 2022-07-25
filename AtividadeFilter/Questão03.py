Lista = []
def gerarLista(novaLista):
    Lista = []
    for l in novaLista:
        if l % 2 == 0:
            x = l * 2
            Lista.append(x)
        else:
            y = l - 1
            Lista.append(y)
    return Lista

for i in range (5):
    Num = int(input("Digite um número: "))
    Lista.append(Num)

print(gerarLista(Lista))
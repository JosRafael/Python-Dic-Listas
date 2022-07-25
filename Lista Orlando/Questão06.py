def uniaoLista(lista1, lista2):
    return lista1 + lista2
def interLista(lista1, lista2):
    interlist = []
    for c in lista1:
        if c in lista2 and c in lista1:
            interlist.append(c)
    return interlist

def diferencaLista(lista1, lista2):
    dif = []
    for i in lista1:
        if i not in lista2:
            dif.append(i)
    for i in lista2:
        if i not in lista1:
            dif.append(i)
    return dif
controle = "s"
lista1 = []
lista2 = []

while controle == "s":
    lista1.append(input("Digite um elemento para ser acrescentado a primeira lista: "))
    controle = input("Deseja adicionar mais elementos? Digite (S) or (N): ")

controle = "s"
while controle == "s":
    lista2.append(input("Digite um elemento para ser acrescentado na segunda lista: "))
    controle = input("Deseja adicionar mais elementos? Digite (S) or (N): ")

print("-=" * 35)
print(f"1ª Lista criada: {lista1}")
print(f"2ª Lista criada: {lista2}")
print("-" * 35)



print("  A união das duas listas é: ")
print(uniaoLista(lista1, lista2))
print("-=" * 35)


print("A interseção das duas listas é: ")
print("-=" * 35)
print(interLista(lista1, lista2))
print("-=" * 35)



print("Os elementos que diferem nas duas listas são: ")
print("-=" * 35)
print(diferencaLista(lista1, lista2))
print("-=" * 35)
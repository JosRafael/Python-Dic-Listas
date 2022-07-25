#Questão 03
def soma(lista):
    tam = len(lista)
    lista_nova = []
    soma = 0
    for c in range(0, tam):
        for c in lista[c]:
            soma = soma + c
        lista_nova.append(soma)
        soma = 0
    return print(lista_nova)

print('-'*30)
print(' A SOMA SERÁ: ')
print('-'*30)
soma( [[4,7,8],[4,15,7],[5,2,4],[5,4,7],[5,10,11]])
print('-'*30)
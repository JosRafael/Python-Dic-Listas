numeros = [10,40,80,30,20,70,60,90,50]
lista = [10,40,80,30,20,70,60,90,50]
print("O elemento do índice 5 é :",numeros[5])
del numeros[8]
print("A tabela sem o último índice ficará a seguinte:",numeros)
numeros.insert(2, 100)
print("Adicionado o elemento 100 no índice 2 da lista:",numeros)
print("A tabela invertida ficará a seguinte: ",numeros[::-1])
print("elementos que estão em índices pares:",numeros[2::2]) 


def NumPares(np):
    numeros_pares = []
    for n in num:
        if n % 2 == 0:
            numeros_pares.append(n)
    return numeros_pares
for i in range(0,11):
    print()
    num = int(input('Digite um  número e diga quais são pares':))
    print('Elem =',NumPares(num))
print(NumPares)
        
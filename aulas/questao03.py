def NumPares():
    num = []
    numeros_pares = []
    for n in range(10):
        num.append(int(input('Digite um número:')))
        if num % 2 == 0:
            num.append(numeros_pares)
    return numeros_pares

     

print(NumPares())
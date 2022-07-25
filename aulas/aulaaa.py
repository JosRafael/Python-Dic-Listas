numeros = [int(input('Digite um numero: ')) for num in range(10)]
dado5 = len(list(filter(lambda n: n == 5, numeros)))
print()
print(f'O número 5 apareceu {dado5} vezes')

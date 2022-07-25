def InserirNumero():
      num = int(input('informe um numero: '))
      return num

def CalcularNumerosPrimos(numero):
      primos = ""
      for i in range(2, numero+1):
        contador = 0
        for j in range(2, i+1):
            if i % j == 0:
               contador += 1
        if contador <= 1:
            primos = primos + " " + str(i)
      return primos

num = int(input('Digite um número inteiro maior que "2": '))
print(f'O valor escolhido foi {num}')  
print(f'Os números primos, são: {CalcularNumerosPrimos(num)}')
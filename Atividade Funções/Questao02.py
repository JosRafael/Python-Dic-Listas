def soma():
    print("Calculo da soma dos n primeiros inteiros positivos")
    n = int(input("Digite o valor de n: "))
    soma = n * (n + 1) // 2 
    print("A soma dos", n, "primeiros inteiros positivos é", soma)

soma()
pessoas = dict()
dados = list()

for c in range(1,6):
    print('-----{}ª PESSOA -----'.format(c))
    pessoas.clear()
    pessoas['nome'] = str(input('Digite o nome: '))
    pessoas['e-mail'] = str(input("Digite um e-mail: "))
    dados.append(pessoas.copy())
 
print()
print('DADOS CADASTRADOS E ARMAZENADOS: ', dados)
    


   
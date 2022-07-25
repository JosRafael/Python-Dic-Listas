import json

arquivo = open('dados.json')
dados = json.load(arquivo)

print(dados)
print('-'*30)
print(dados['Nome'])
print('-'*30)
print(dados['Nota1'])
print('-'*30)
print(dados['Nota2'])
print('-'*30)
arquivo.close()
import json

arquivo = open('dados.json', 'w')

dic = {
    'Nome':'Rafael',
    'Nota1':'10',
    'Nota2':'7'
}
json.dump(dic, arquivo)
arquivo.close()
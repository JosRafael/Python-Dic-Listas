import requests

num = []
usuario = "P28rJfENmyK5M6kz4"
token = "yYeGobKD6KSMCM8Jfh2EdN228"
url = "https://api.apify.com/v2/datasets/igDbWarnuaARQEIkA/items?clean=true&format=json"
conteudo = requests.get(url)
if conteudo:
    dados = conteudo.json()
    resultados = dados[0]['infectedByRegion']
def estado(UF): 
    for resultado in resultados:
        if resultado['state'] == UF:  
            return resultado['count']
for i in range(len(resultados)):
    cont = resultados[i]['count']
    num.append(cont)
Pesquisa = max(num)
for j in range(len(resultados)):
    casos_Estado = resultados[j]['count']

    if Pesquisa == casos_Estado:
        print("+--------------------------------------------------------+")
        print("|                                                        |")
        print("|                   COVID-19 NO BRASIL                   |")
        print("|                                                        |")
        print("+--------------------------------------------------------+")
        print("\nEstado com maior número de infecção")
        print("+--------------------------------------------------------+")
        print("Estado:",resultados[j]['state'])
        print("Infectados:",resultados[j]['count'])
        print("+--------------------------------------------------------+")

pegarEstado = input("Digite a sigla (Ex: PE), do estado para visualizar os dados: ").upper()
print("\nEstado:",pegarEstado)
print("Casos  atualmente:", estado(pegarEstado))
print("Use Máscara e Álcool em Gel!")
def gerarLista1(num):
    mes= ['Janeiro','Fervereiro','Março','Abril', 'Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    for e in range(1, num+1):
        mes.append( e )
    return mes

def main():
    valor = int(input("Digite um número: "))
    lista = gerarLista1( mes )
    print(lista)

main()

def inverter(lista):
    return lista[::-1]

def imprimirChaves( dicionario ):
    for e in dicionario.keys():
        print( e )
    
def main():
    itens = ["Feijão", "Arroz", "Macarrão"]
    print( inverter(itens) )

    dic = {"um": 1, "dois": 2, "três": 3}
    imprimirChaves(dic)

main() #Chamando a função main() -> inverter() e imprimirChaves() 






     



   
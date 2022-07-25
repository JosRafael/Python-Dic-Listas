dicionario_voltas = {}
corredores = []
totalvoltas = 0
mediavoltas = 0
lista_medias = []

def PilotoMaisRapido():
    menorVolta = dicionario_voltas[corredores[0]][0]
    piloto = corredores[0]
    voltaMaisRapida = 0
    print(f"A menor volta foi do piloto(a){piloto}, na {voltaMaisRapida+1}ª volta com o tempo de {menorVolta} segundos.")


def Classificacao():
    totalvoltas = 0
    mediavoltas = 0
    lista_medias = []

    for pilotos in range(0, 6):
        for voltas in range(0, 3):
            totalvoltas = totalvoltas + dicionario_voltas[(corredores[pilotos])][voltas]
            mediavoltas = totalvoltas / 3
            lista_medias.append(mediavoltas)
            totalvoltas = 0

    print("\n")
    print("-" * 30)
    print(" **** Resultados ****")

    for pilotos in range(0, 6):
        print(f"{corredores[pilotos]} - Media de tempo: {lista_medias[pilotos]}")
    print("-" * 30)

    classificacao = sorted(lista_medias)
    print("-" * 30)
    print(" * Classificação *")
    print("Média de tempo na corrida: ")
    for i in range(0, 6):
        print(f"Posição {i+1}: {classificacao[i]}")

    print("-" * 30)

for nomes in range(0, 6):
    nome_corredor = input(f"Informe o nome do corredor {nomes+1}: ")
    corredores.append(nome_corredor)

for i in range(0, 6):
    dicionario_voltas[corredores[i]] = float(input(f"Informe os tempos (em segundos) das três voltas do piloto(a) {i+1}:\nVolta 1: ")), float(input("Volta 2: ")),float(input("Volta 3: "))


PilotoMaisRapido() 
PilotoMaisRapido()
Classificacao() 
import random
def printjogo(jogo):
    print(' '.join(jogo).upper())
    print('')
    
palavras = ['shevi', 'valorant', 'raze', 'atletico', 'cartolouco', 'jett']
palavra = random.choice(palavras)
jogo = ['_' for i in range(len(palavra))]
erro = 0
acerto = False

while erro < 6 and not acerto:
    printjogo(jogo)
    print('DIGITE UMA LETRA!:')
    tentativa = str(input()).lower()

    if tentativa not in palavra:
        erro += 1
        print(f'Você errou pela {erro}a vez. Tente novamente!')
        continue
    for i, letra in enumerate(palavra):
        if letra == tentativa:
            jogo[i] = tentativa
    if '_' not in jogo:
        acerto = True

if acerto:
    print()
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
else:
    print()
    print('Você errou, tente novamente!')
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

printjogo(jogo)
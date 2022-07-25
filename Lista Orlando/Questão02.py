matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um número inteiro para [{l}, {c}]: '))
print('-'*45)       
print('A matriz ficará a seguinte:')
for c in range(0,3):
    print(matriz[c])

print()
print('MATRIZ:-', matriz)
print('A diagonal secundaria da matriz, será:', matriz[0][2],'|', matriz[1][1],'|', matriz [2][0]) 
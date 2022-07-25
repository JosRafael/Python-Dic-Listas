temp = []
def Media(calculo):
    soma = 0
    for x in calculo:
        soma += x
        Resul = soma / len(calculo)
    Resul = '{0:.1f}'.format(Resul)
    return Resul

def mesEx(i):
    meses = ['Janeiro', 'Fevereiro','Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return meses[i]

for x in range(12):
    mes = mesEx(x)
    Temp = float(input(f"Informe a temperatura média do respectivo mês de {mes}: "))
    temp.append(Temp)
print('\n')
media = float(Media(temp))

for i in range(len(temp)):
    if temp[i] > media:
        mes = mesEx(i)
        print(f'A temperatura de {temp[i]:.1f}°c foi maior que a média anual de {media:.1f}°c ocorrida no mês de {mes}')
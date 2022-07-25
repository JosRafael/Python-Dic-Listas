from datetime import datetime
import winsound

print("*" * 45)
print("Configure seu Alarme / Temporizador")
print("*" * 45)

h_desejada = str(input("(Formato: HH:MM:) Digite a hora e o minuto para acionar o lembrete: "))
print("*" * 45)
alarme = datetime.strptime(h_desejada , '%H:%M')
aviso = str(input('Escolha um nome para o teu temporizador(Sem utilizar letras maiúsculas ) ' '\n' '\n'))

print("-" * 45)
print(f"O temporizador será tocado exatamente às: {alarme.hour}:{alarme.minute}")
print("-" * 45)

while True:
    if datetime.now().hour == alarme.hour and datetime.now().minute == alarme.minute:
        for i in range(0,5):
            winsound.Beep(300, 1000)
            print(str(aviso +'\n' + h_desejada))
        break



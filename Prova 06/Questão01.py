with open('texto_inicial.txt', 'r') as file:
    lines = file.readlines()

print(lines)
with open('texto_final.txt', 'w') as file:
    for i, j in enumerate(lines):
        file.writelines(f'{j.upper()}')
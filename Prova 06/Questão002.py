with open('lista_de_compras.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

itens = []
total = 0
for i in lines:
    item, preco = i.split(':')
    total += float(preco)
    itens.append(item)

print(itens, total)

with open('recibo_de_compras.html', 'w', encoding='utf-8') as file:
    file.writelines(itens.pop(0))
    max = len(itens)
    for i, j in enumerate(itens):
        file.writelines(f', {j}' if i < max-1 else f' e {j}.\n')
    file.writelines(f'Total: {total}')
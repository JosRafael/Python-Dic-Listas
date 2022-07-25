dia = input('Digite o dia de nascimento: ')
mês = input('Digite o mês de nascimento: ')
ano = input('Digite o ano de nascimento: ')

meses = ['JANEIRO','FERVEIRO','MARÇO','ABRIL',
         'MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO',
         'OUTUBRO','NOVEMBRO','DEZEMBRO']

print()
print ('VÔCE NASCEU EM:')
print( f'{ dia } de { meses[int(mês) - 1] } de {ano}.')



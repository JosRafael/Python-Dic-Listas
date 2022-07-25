def nomeMES(mes):
    m = ['','JANEIRO','FERVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO']
    return(m[mes])
for i in range(1,13):
    print()
    mes= int(input('Digite um  número e diga seu respectivo mês: '))
    print('Mês =',nomeMES(mes))

       
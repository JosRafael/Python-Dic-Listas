def NumNegativos(listadenegativos):
    neg = list(filter(lambda i: i > 0, listadenegativos)) 
    return neg

def main():
    print(NumNegativos([1, 2, 3, -4, 5, -6]))

print('------Lista sem os números negativos----- ')
main()
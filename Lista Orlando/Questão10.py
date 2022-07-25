def extractURL(link):
    for c in range (0, len(link)):
        if link[c] == 'u':
            if link[c+1] == 'r':
                if link[c+2] == 'l':
                    posicao = c + 4
                    break
                
    if link[posicao] == 'h':
        if link[posicao+1] == 't':
            if link[posicao+2] == 't':
                for c in range (posicao, len(link)):
                    print (link[c], end='')
    else:
        for i in range ((len(link)-1), posicao, -1):
            print (link[c], end='')
    

link = input ("Digite o link para extração da URL verdadeira: ")
(extractURL(link))
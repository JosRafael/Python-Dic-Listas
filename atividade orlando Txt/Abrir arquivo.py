'''manipulador = open('arquivo.txt','r')
print('\nMetodo Read(): \n')
print(manipulador.read())

manipulador.seek(0)

print('\nMetodo readline(): \n')
print(manipulador.readline())
print(manipulador.readline())

manipulador.seek(0)

print('\nMetodo readlines(): \n')
print(manipulador.readlines())

manipulador.close()'''

'''print('Teste de abertura de arquivos em Python')
print('Tentando abrir um arquivo de texto armazenado no PC: \n')

manipulador = open('arquivo.txt', 'r')
for linha in manipulador:
    linha = linha.rstrip()
    print(linha)
manipulador.close()'''

'''print('\nContando as linhas do arquivo de texto analisado: \n')
contador = 0
arq = open('arquivo.txt','r')
for linha in arq:
    contador +=  1
print('Numero de linhas no arquivo: ', contador)
arq.close()'''

'''print('\nRetornando Somente as linhas que possuem a palavra Python')
arq = open('arquivo.txt', 'r')
contador = 0
for linha in arq:
    linha = linha.rstrip()
    if 'python' in linha:
        contador += 1
        print(linha)
print('\nForam retornadas', contador, 'linhas')
arq.close() '''

print('\nRetornando somente as linhas que contenham a palavra python')
palavra = input('Digite a palavra para busca:')
arq = open('arquivo.txt','r')
contador = 0
for linha in arq:
    linha = linha.rstrip()
    if palavra in linha:
        contador += 1
        print(linha)
print('\n Foram retornadas', contador, 'linhas')

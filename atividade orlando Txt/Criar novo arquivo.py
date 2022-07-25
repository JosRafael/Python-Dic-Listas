arquivo = open('arq01.txt', 'w')
arquivo.write('Boson treinamentos\n')
arquivo.write('Criando um arquivo de texto com Python\n')
arquivo.write('Arquivo criado por Fabio dos Reis\n')
arquivo.write('É isso ai pessoal!\n ')
arquivo.close()

arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()

'''print('\n')
texto = input('Digite uma frase para acrescentar ao arquivo: ')
arquivo = open('arq01.txt','a')
arquivo.write(texto + '\n')
print('Operação concluida no arquivo '+ arquivo.name + 'usando o modo de acesso.')
arquivo.close()

print('\nTexto alterado:')
arquivo = open('arq01.txt', 'r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()'''
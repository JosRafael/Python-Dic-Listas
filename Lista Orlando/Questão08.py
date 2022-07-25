dicio = {}
def Novo_Nome(nome, numeros):
    dicio[nome] = numeros

def Incluir_Tel(nome, numero):
    if nome in dicio:
        dicio[nome].append(numero)
    else:
        resposta = input("deseja incluí­-lo?(s/n): ")
        if resposta.lower() == "s":
            Novo_Nome(nome, numero)

def excluirTelefone(nome, telefone):
     global dicio
     if nome in dicio.keys():
        if len(dicio[nome]) == 1:
            dicio[nome] = None
            print("O usuário %s foi exlcuido" % nome)
        else:
            print(len(dicio[nome]))
            for numero in range(len(dicio[nome]) - 1):
                if telefone == dicio[nome][numero]:
                    dicio[nome].pop(numero)
                    print("O número %s do usuário %s foi excluido" % (telefone, nome))
            else:
                print("Usuário não existe ")


def Retirar_Nome(nome):
    if nome in dicio:
        del dicio[nome]


def consultarTelefone(nome):
    if nome in dicio[nome]:
        print(
            "O contato %s possui os seguintes telefones %s"
            % (nome, dicio[nome])
        )

    return dicio[nome]


condicao = True
while condicao:
    print("1- ­Adicionar contato na agenda de telefone")
    print("2- Consultar numero do contato")
    print("3- Incluir telefone")
    print("4- Excluir telefone")
    print("5- Sair \n")
    
    resposta = int(input("Escolha uma opção: "))

    print("Opção escolhida: ", resposta)
    if resposta == 1:
        nome = input("Digite o nome que deseja salvar na lista: ")
        telefones = []
        numero = -1
        while numero != 0:
            numero = int(
                input("Digite o numero de telefone: ou digite zero (0) para parar ")
            )
            if numero != 0:
                telefones.append(numero)
        Novo_Nome(nome, telefones)
        print("Agenda atual: ", dicio)

    if resposta == 2:
        nome = input("Digite o nome: ")
        consultarTelefone(nome)
        print("Agenda consultada: ", dicio)

    if resposta == 3:
        nome = input("Digite o nome: ")
        telefone = int(input("Digite o telefone: "))
        Incluir_Tel(nome, telefone)
        print("Agenda atual: ", dicio)
    
    if resposta == 4:
        nome = input("Digite o nome: ")
        telefone = int(input("Digite o telefone: "))
        excluirTelefone(nome, telefone)
        print("Agenda atual: ", dicio)

    if resposta == 5:
        condicao = False
        print("Agenda atual: ", dicio)
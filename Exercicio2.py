#vetores globais para serem acessíveis de qualquer lugar da aplicação
nomes = []
resultado = []
#função para leitura de nomes digitados pelo usuário
def adicionarNomes():
    while True:
        nome = str(input("Digite um nome: "))
        if not nome == "":
            separador = nome.split()
            for a in separador:
                nomes.append(a)
        else:
            compararNomes(nomes)
            break
#Função para comparação dos nomes existentes 
def compararNomes(nomes):
    for controle in range(len(nomes)-1,-1,-1):
        for comparacao in range(controle):
            if nomes[controle] == nomes[comparacao]:
                resultado.append(nomes[controle])

#def removerDuplicados(resultado):
#    for controle in range(len(resultado)-1,-1,-1):
#        for comparacao in range(controle):
#            if resultado[controle] == resultado[comparacao]:
#                resultado.remove(resultado[controle])

#Função para ordenação da lista em ordem alfabética
def ordenar(resultado):
    for controle in range(len(resultado)-1,0,-1):
        for indice in range(controle):
            if resultado[indice] > resultado[indice+1]:
                temporario = resultado[indice]
                resultado[indice] = resultado[indice+1]
                resultado[indice+1] = temporario
#Função como menu principal           
def menu():
    while True:
        opcao = int(input('''Digite 1 para adicionar nomes
Digite 2 para ordenar
Digite 0 para sair
Digite sua opção: '''))
        if opcao == 1:
            adicionarNomes()
        elif opcao == 2:
            ordenar(resultado)
            print(resultado)
        elif opcao == 0:
            break
        else:
            print("Opção inválida")

menu()

            
        
        

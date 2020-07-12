valor = []
carrinho = []
pedido = int(0)

def cardapio():
    print("*** Selecione seu produto ***")
    print('''1 marmitex pequena R$ 11.00
2 marmitex média R$ 12.00
3 marmitex grande R$ 13.00
4 lanches R$ 16.50
5 doces e sobremesas R$ 12.50
6 bebidas R$ 5.00''')
    busca = int(input("Digite a opção desejada: "))
    return busca

def remover():
    cont = 0
    for a in range(0, len(carrinho)):
        cont += 1
        print(cont, carrinho[a])
    escolha = int(input("Digite um item a ser removido: "))
    try:
        carrinho.pop(escolha-1)
    except:
        print("Esta opção não existe no carrinho")

while True:
    print(30 * "=")
    print("*** Marmitex e Lanches ***")
    opcao = int(input('''Digite 1 para escolher produto
Digite 2 para alterar pedido
Digite 3 para carrinho
Digite 4 para compra
Digite 5 para informar dados de entrega
Digite 6 para finalizar pedido e entregar
Digite 7 para limpar dados e carrinho
Digite 0 para sair: '''))
    print(30 * "=")
    if opcao == 1:
        preco1 = ("Marmitex pequena: R$ 11.00")
        preco2 = ("Marmitex média: R$ 12.00")
        preco3 = ("Marmitex grande: R$ 13.00")
        preco4 = ("Lanches: 16.50")
        preco5 = ("Doces e sobremesas: R$12.50")
        preco6 = ("Bebidas: R$ 5.00")
        pro = cardapio()
        if pro == 1:
            carrinho.append(preco1)
            valor.append(float(11.00))
        if pro == 2:
            carrinho.append(preco2)
            valor.append(float(12.00))
        if pro == 3:
            carrinho.append(preco3)
            valor.append(float(13.00))
        if pro == 4:
            carrinho.append(preco4)
            valor.append(float(16.50))
        if pro == 5:
            carrinho.append(preco5)
            valor.append(float(12.50))
        if pro == 6:
            carrinho.append(preco6)
            valor.append(float(5.00))
        if pro != 1 and pro != 2 and pro != 3 and pro != 4 and pro != 5 and pro != 6:
            print(30 * "=")
            print("Opção inválida")
    elif opcao == 2:
        remover()
    elif opcao == 3:
        print("*** Carrinho ***")
        for itens in carrinho:
            print("- %s" %(itens))
    elif opcao == 4:
        total = float(0)
        soma = float(0)
        for soma in valor:
            total += soma
        print("*** Compra ***")
        print("Total: R$ %.2f" %(total))
    elif opcao == 5:
        nome = str(input("Digite seu nome: "))
        endereco = str(input("Digite o endereço de entrega: "))
        num = int(input("Digite o número para entrega: "))
    elif opcao == 6:
        total = float(0)
        soma = float(0)
        print("*** Pedido realizado com sucesso ***")
        print ("Nome: %s\nEndereço: %s\nNúmero: %s" %(nome,endereco,num))
        for itens in carrinho:
            print("- %s" %(itens))
        for soma in valor:
            total += soma
        print("Total: R$ %.2f" %(total))
        pedido += 1
        print("Número do pedido: %d" %(pedido))
        print("Tempo de entrega estimado em 30 e 45 min")
        valor = []
        carrinho = []
    elif opcao == 7:
        pedido = []
        valor = []
        carrinho = []
    elif opcao == 0:
        break
    else:
        print("Opção inválida")
        
            
        
        
        

    
        
        
    
                    

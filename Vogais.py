contlinhas = int(0)
linhasvogais = int(0)
totalvogais = int(0)
totalnum = int(0)
final = []
while True:
    frase = input("Digite uma frase: ")
    if not frase == "":
        contlinhas += 1
    vogais = str("aeiou")
    numeros = str("0123456789")
    for verif in frase:
        if verif in vogais:
            totalvogais += 1
        if verif in numeros:
            totalnum += 1
    if totalvogais > totalnum:
        final.append(frase)
        totalvogais = int(0)
        totalnum = int(0)
    if frase == "":
        for texto in final:
            print(texto)
        linhasvogais = len(final)
        print("Quantidade de linhas digitadas: %d" %(contlinhas))
        print("Total de linhas com mais vogais: %d" %(linhasvogais))
        break

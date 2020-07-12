a = ["Marmitex pequena: R$11.00", "Marmitex Grande: R$17.00", "Bebidas: R$6.00"]
cont = (0)
for c in a:
    cont += 1
    print(cont, c)
escolha = int(input("Escolha um produto a ser removido: "))
b = a[escolha-1]
c = b.split()
d = len(c)
e = slice(d-1,d)
f = (c[e])
for conv in f:
    g = conv
h = (g.strip("R$"))
i = float(h) + 5
print("%.2f" %(i))
#print(c[e])

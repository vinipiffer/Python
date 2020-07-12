def quantidade_Numeros_Caracteres(senha):
    NUMEROS = ("1234567890")
    CARACTERES = ("*%&$#!+=_-?@")
    totalnumeros = int(0)
    totalcaracteres = int(0)
    for verificador in senha:
        if verificador in NUMEROS:
            totalnumeros += 1
        if verificador in CARACTERES:
            totalcaracteres += 1
    return totalnumeros, totalcaracteres

def quantidade_Letras(senha):
    LETRASMINUSCULAS = ("abcdefghijklmnopqrstuvxwyz")
    LETRASMAIUSCULAS = ("ABCDEFGHIJKLMNOPQRSTUVXWYZ")
    total_letras = int(0)
    total_letras_ma = int(0)
    for verificador in senha:
        if verificador in LETRASMINUSCULAS:
            total_letras += 1
        if verificador in LETRASMAIUSCULAS:
            total_letras_ma += 1
    return total_letras, total_letras_ma

def verifica_numeros(numeros):
    QTDDNUMEROS = int(1)
    if numeros < QTDDNUMEROS:
        return False
    else:
        return True

def verifica_caracteres(caracteres):
    QTDDCARACTERES = int(2)
    if caracteres > QTDDCARACTERES:
        return False
    else:
        return True

def verifica_letras_min(letras_min):
    QTDDLETRAS = int(1)
    if letras_min < QTDDLETRAS:
        return False
    else:
        return True

def verifica_letras_ma(letras_ma):
    QTDDLETRAS_MA = int(1)
    if letras_ma < QTDDLETRAS_MA:
        return False
    else:
        return True

def confirmar_senha(numeros, caracteres, letras_min, letras_ma):
    senhaOk = [numeros, caracteres, letras_min, letras_ma]
    for verificador in senhaOk:
        if verificador == True:
            camposvalidos = verificador
        else:
            return False
    return True

def mensagem(erro):
    lista_erros = {
        0: 'Sua senha deve conter no mínimo 1 número',
        1: 'Sua senha deve ter no máximo 2 caracteres especiais',
        2: 'Sua senha deve ter no mínimo 1 letra minuscula',
        3: 'Sua senha deve ter no mínimo 1 letra maiuscula'
        }
    return print(lista_erros.get(erro))

while True:
    print("-" * 50)
    senha = str(input('''→ Sua senha deve ter no mínimo 8 e máximo 16 caracteres
→ Deve conter uma letra minusculas e uma miuscula
→ Deve conter no maximo 2 caracteres especiais
Digite sua senha: '''))
    if senha != "":
        if len(senha) >= 8 and len(senha) <= 16:
            totalnumeros, totalcaracteres = quantidade_Numeros_Caracteres(senha)
            total_letras, total_letras_ma = quantidade_Letras(senha)
            numerosOk, caracteresOk = verifica_numeros(
                totalnumeros), verifica_caracteres(totalcaracteres)
            letras_minOk, letras_maiOk = verifica_letras_min(
                total_letras), verifica_letras_ma(total_letras_ma)
            senhaOk = confirmar_senha(numerosOk, caracteresOk, letras_minOk, letras_maiOk)
            if senhaOk:
                print("Senha cadastrada com sucesso")
                break
            if numerosOk == False:
                mensagem(0)
            elif caracteresOk == False:
                mensagem(1)
            elif letras_minOk == False:
                mensagem(2)
            elif letras_maiOk == False:
                mensagem(3)
        else:
            print("Sua senha deve conter no mínimo 8 e maximo 16 caracteres")
    else:
        break
    
    
    
    

        

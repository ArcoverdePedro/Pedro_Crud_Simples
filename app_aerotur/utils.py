def validador(cpf):
    if len(cpf) == 11:
        somar = 0
        aux = 1
        cont= 0
        if len(cpf) == 11:
            #verificando o primeiro digito
            while cont <=8:
                somar = somar + int(cpf[cont]) * aux
                aux +=1
                cont+=1
            if somar%11 == int(cpf[9]) or somar%11 == 10 and int(cpf[9]) == 0:
                aux = 0
                cont = 0
                somar = 0
                while cont <=9:
                    somar = somar + int(cpf[cont]) * aux
                    aux+=1
                    cont+=1
                if somar%11 == int(cpf[10]) or somar%11 == 10 and int(cpf[10]) == 0:
                    return True
                else:
                    return False

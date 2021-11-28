cNum = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
cLet = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
dizionario = {'M':'1000', 'CM':'900', 'D':'500', 'CD':'400', 'C':'100', 'XC':'90', 'L':'50', 'XL':'40', 'X':'10', 'IX':'9', 'V':'5', 'IV':'4', 'I':'1'}

def formatta(rom):
    stringa = []
    i = 0
    while True:
        if i <= len(rom)-2:
            aggiunto = False
            for j in range(1, len(cLet), 2):
                if rom[i] + rom[i+1] == cLet[j]:
                    stringa.append(cLet[j])
                    aggiunto = True
                    i += 1
                    break
            if aggiunto == False:
                stringa.append(rom[i])
        elif i == len(rom)-1:
            stringa.append(rom[i])
        else:
            break
        i += 1
    return stringa

def tipoNumero(stringa):
    copia = formatta(stringa)
    num = let = 0
    for i in copia:
        if i.isdigit():
            num += 1
        else:
            let += 1
    if (num >= 1 and let > 0) or (num > 0 and let >= 1):
        stringa = input('Il numero inserito non è valido\nSi inserisca un numero arabo o romano: ').upper()
        tipo, stringa = tipoNumero(stringa)
    else:
        if num >= 1:
            tipo = 'int'
        elif let >= 1:
            tipo = 'str'
    return tipo, stringa

def unChar(rom):
    dec = 0
    error = False
    code = ''
    try:
        dec = int(dizionario[rom[0]])
    except KeyError:
        error = True
        code = 'KeyError'
    return error, code, dec

def errori(lista):
    condizioni = []
    ordinata = []
    error = False
    code = ''
    for i in range(len(lista)):
        try:
            aus = lista[i]
            lista[i] = int(dizionario[aus])
            ordinata.append(int(dizionario[aus]))
        except KeyError:
            error = True
            code = 'KeyError'
            break
    if error != True:
        for i in range(len(cLet)):
            condizioni.append(lista.count(cNum[i]))
        if condizioni[2] > 1 or condizioni[6] > 1 or condizioni[10] > 1:
            error = True
            code = 'rep2610'
        if error != True:
            for i in range(1, len(condizioni), 2):
                if condizioni[i] > 1:
                    error = True
                    code = 'rep*2dl'
                    break
            if error != True:
                for i in range(2, len(condizioni), 2):
                    if condizioni[i] > 3:
                        error = True
                        code = 'rep*2ul'
                        break
                if error != True:
                    for i in range(len(lista)):
                        if lista[i] != 1000 and lista[i] != 100 and lista[i] != 10 and lista[i] != 1:
                            numero = cNum[cNum.index(lista[i])+1]
                            for j in range(i, len(lista)):
                                if lista[j] == numero:
                                    error = True
                                    code = 'repafter2dl'
                                    break
                        if error == True:
                            break
                    if error != True:
                        ordinata.sort(reverse = True)
                        if ordinata != lista:
                            error = True
                            code = 'order'
    return error, code

def arToRom(stringa):
    stringa = int(stringa)
    roman = ''
    i = 0
    while stringa > 0:
        if (stringa - cNum[i]) >= 0:
            stringa -= cNum[i]
            roman += cLet[i]
        else:
            i += 1
    return roman

def romToAr(stringa):
    rom = [el for el in stringa]
    if len(rom) != 1:
        stringa = formatta(rom)
        error, code = errori(stringa)
        dec = 0
    else:
        error, code, dec = unChar(rom)
    if error != True:
        if dec == 0:
            for el in stringa:
                dec += el
        return dec
    else:
        stringa = input('Il numero inserito non è valido\nSi inserisca un numero arabo o romano: ').upper()
        tipo, stringa = tipoNumero(stringa)
        trasforma(tipo, stringa)

def trasforma(tipo, stringa):
    if tipo == 'int':
        num = arToRom(stringa)
        print(f'{stringa} in numeri romani si scrive {num}')
    elif tipo == 'str':
        num = romToAr(stringa)
        if num != None:
            print(f'{stringa} in numeri arabi è {num}')

print('Dato un numero questo programma lo converte nel corrispettivo arabo o romano')
answ = 'Y'
while answ == 'Y' or answ == 'y':
    stringa = input('Si inserisca un numero arabo o romano: ').upper()
    tipo, stringa = tipoNumero(stringa)
    trasforma(tipo, stringa)
    answ = input('Si vuole ripetere il processo?\n(Y/N)\n')
print('Grazie per aver usato il programma\nVisita www.github.com/claristorio')
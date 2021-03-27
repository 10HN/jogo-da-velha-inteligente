def aleatorio(valor,beta):
    import random
    while 1:
        num = random.choice(valor)
        if type(num)==int and num%2==beta:
            return num
            break
def percorreLista(lista, valor):
    for i in lista:
        if i.count(valor) == 2:
            for jogada in i:
                if type(jogada) == int:
                    return jogada
def maquina(mapa, mapaIA):
    if mapa[4] == 5:
        return 5
    else:
        valor = "O","X"
        for i in valor:
            n = percorreLista(mapaIA, i)
            if n:
                return n
                exit()
        if mapa[4] == "O":
            mapa2=[[mapa[0],mapa[1],mapa[3]],
                   [mapa[1],mapa[2],mapa[5]],
                   [mapa[3],mapa[6],mapa[7]],
                   [mapa[5],mapa[7],mapa[8]]]
            valor = percorreLista(mapa2, "X")
            if valor:
                return valor
                exit()
        if mapa[4] == "X":
            if mapa.count('X') == 4:
                valor = aleatorio(mapa, 0)
                if valor:
                    return valor
                    exit()
            else:
                valor = aleatorio(mapa,1)
                if valor:
                    return valor
                    exit()
        else:
            valor = aleatorio(mapa,0)
            if valor:
                return valor
                exit()
                
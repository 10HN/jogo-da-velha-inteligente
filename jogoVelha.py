# -*- coding: utf-8 -*-
import os
import IA
class JogoVelha (object):
    limpa = 'os.system("cls" if os.name == "nt" else "clear")'
    vez = 'X'
    mapa = [1,2,3,
            4,5,6,
            7,8,9]
    stop = 9
    def __init__(self):
        while 1:
            eval(self.limpa)
            self.interface()
            self.verificandoJogo(self.mapa)
            self.marcador(input('\nInforme onde deseja jogar: '))

    def interface(self):
        print('\n|  '+str(self.mapa[0])+'  |  '+str(self.mapa[1])+'  |  '+str(self.mapa[2])+'  |')
        print('+-----+-----+-----+')
        print('|  '+str(self.mapa[3])+'  |  '+str(self.mapa[4])+'  |  '+str(self.mapa[5])+'  |')
        print('+-----+-----+-----+')
        print('|  '+str(self.mapa[6])+'  |  '+str(self.mapa[7])+'  |  '+str(self.mapa[8])+'  |')
    
    def marcador(self, valorMarcar):
        if valorMarcar == '':
            self.marcador(input('**Escolha algum numero!!\nInforme onde deseja jogar: '))
        elif int(valorMarcar) in self.mapa:
            self.mapa[int(valorMarcar)-1] = self.vez
            self.vez = 'O' if self.vez == 'X' else 'X'
            self.stop-=1
            self.verificandoJogo(self.mapa)
        else:
            self.marcador(input('**O numero inserido já está marcado!! Escolha outro: '))

    def verificandoJogo(self, mapa):
        valor = [[mapa[0],mapa[1],mapa[2]],
                [mapa[3],mapa[4],mapa[5]],
                [mapa[6],mapa[7],mapa[8]],
                [mapa[0],mapa[3],mapa[6]],
                [mapa[1],mapa[4],mapa[7]],
                [mapa[2],mapa[5],mapa[8]],
                [mapa[0],mapa[4],mapa[8]],
                [mapa[2],mapa[4],mapa[6]]]
        if ['O','O','O'] in valor:
            self.interface()
            input('\nA MAQUINA GANHOU!!!')
            exit()
        elif self.stop == 0:
            self.interface()
            input('\nDEU VELHA!!!')
            exit()
        elif self.vez == 'O':
            self.marcador(IA.maquina(self.mapa, valor))
        else:
            return True
JogoVelha()

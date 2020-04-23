#coding: utf-8

class Recipiente(object):
    '''
    Armazena o volume máximo e atual de um recipiente, além de testar se o mesmo está cheio ou vazio.
    '''
    vol_max = 0
    vol_atual = 0

    def __init__(self, vol_max=0, vol_atual=0):
        self.vol_max = vol_max
        self.vol_atual = vol_atual

    def cheio(self):
        return True if self.vol_atual == self.vol_max else False

    def vazio(self):
        return True if self.vol_atual == 0 else False

class Problema(object):
    recipientes = [] # Lista de recipientes do desafio

    def __init__(self, r1, r2, r3):
        self.recipientes = [r1, r2, r3]

    def lista_recipientes(self):
        '''
        Mostra os conteúdos dos recipientes na tela.
        '''
        print('\nRecipiente 0: {}\nRecipiente 1: {}\nRecipiente 2: {}\n'.format(self.recipientes[0].vol_atual, self.recipientes[1].vol_atual, self.recipientes[2].vol_atual))

    def transfere(self, origem, destino):
        '''
        Recebe os índices de origem e destino e realiza a transferência de água, caso possível. Se não for possível, retorna False.
        '''
        if origem == destino: # Se fornecido o mesmo recipiente como origem e destino, não é possível realizar a transferência
            return False

        if not self.recipientes[origem].vazio() and not self.recipientes[destino].cheio():
            if self.recipientes[origem].vol_atual + self.recipientes[destino].vol_atual <= self.recipientes[destino].vol_max:
                self.recipientes[destino].vol_atual += self.recipientes[origem].vol_atual
                self.recipientes[origem].vol_atual = 0
            else:
                self.recipientes[origem].vol_atual -= self.recipientes[destino].vol_max - self.recipientes[destino].vol_atual
                self.recipientes[destino].vol_atual = self.recipientes[destino].vol_max
            return True
        else: #Se a origem estiver vazia ou o destino estiver cheio, não é possível realizar a transferência
            return False

    def testa_fim(self):
        '''
        Testa as condições finais do desafio
        '''
        return True if self.recipientes[1] == 400 and self.recipientes[2] == 400 else False

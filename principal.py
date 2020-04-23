#coding: utf-8

from classes import Recipiente, Problema
from random import randint
from time import sleep

if __name__ == '__main__':
    desafio = Problema( #Condições iniciais do desafio:
        Recipiente(vol_max = 300, vol_atual = 300),
        Recipiente(vol_max = 500, vol_atual = 500),
        Recipiente(vol_max = 700, vol_atual = 0),
    )

    while not desafio.testa_fim():
        origem = randint(0, 2)
        destino = origem
        while destino == origem:
            destino = randint(0, 2)
        desafio.transfere(origem, destino)
        print('{} - {}'.format(origem, destino))
        #desafio.lista_recipientes()

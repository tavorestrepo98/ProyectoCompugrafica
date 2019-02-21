import pygame as pg
import sys, os


BLANCO = [250, 250, 250]
NEGRO = [0,0,0]
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)

def recortar(imagen, ancho, alto, fil, col):
    l1 = []
    l2 = []
    for i in range(0, fil):
        for j in range(0, col):
            cuadro = imagen.subsurface(j*ancho, alto*i, ancho, alto)
            l2.append(cuadro)
        l1.append(l2)
        l2 = []
    return l1



def spritegoku():
    gok = {'standby': recortar(pg.image.load('./resource/goku/standby.png'), 23, 32, 2, 1),
            'walk': recortar(pg.image.load('./resource/goku/walk.png'), 24, 31, 2, 4),
            'run' : recortar(pg.image.load('./resource/goku/run.png'), 25, 31, 2, 4),
            'golpe1': recortar(pg.image.load('./resource/goku/golpe1.png'), 26, 30, 2, 3),
            'golpe2': recortar(pg.image.load('./resource/goku/golpe2.png'), 24, 31, 2, 4),
            'kame': recortar(pg.image.load('./resource/goku/kame.png'), 25, 32, 2, 3),
            'morir': recortar(pg.image.load('./resource/goku/morir.png'), 31, 32, 2, 4),
            'jump': recortar(pg.image.load('./resource/goku/jump.png'), 26, 32, 2, 4)}
    return gok

def spriteminion1():
    minion1 = {'standby': recortar(pg.image.load('./resource/enemigos/minion/minion1/standby.png'), 15, 31, 1, 1),
            'walk': recortar(pg.image.load('./resource/enemigos/minion/minion1/walk.png'), 17, 31, 1, 4),
            'golpe': recortar(pg.image.load('./resource/enemigos/minion/minion1/golpe.png'), 23, 31, 1, 4),
            'poder': recortar(pg.image.load('./resource/enemigos/minion/minion1/poder.png'), 23, 29, 1, 3),}
    return minion1

def spriteminion2():
    minion2 = {'standby': recortar(pg.image.load('./resource/enemigos/minion/minion2/standby.png'), 12, 31, 1, 1),
            'walk': recortar(pg.image.load('./resource/enemigos/minion/minion2/walk.png'), 15, 31, 1, 4),
            'golpe': recortar(pg.image.load('./resource/enemigos/minion/minion2/golpe.png'), 24, 31, 1, 4),
            'poder': recortar(pg.image.load('./resource/enemigos/minion/minion2/poder.png'), 23, 30, 1, 3),}
    return minion2

def spritepoder1():
    poder1 = {'poder1': recortar(pg.image.load('./resource/poderes/kame/poder1.png'), 16, 16, 2, 3)}
    return poder1

def spritekame():
    poder1 = {'kame': recortar(pg.image.load('./resource/poderes/kame/kame.png'), 61, 23, 1, 2)}
    return poder1

def spritepoderm():
    poderm = {'poderm': recortar(pg.image.load('./resource/poderes/poderminion/poder.png'), 13, 8, 1, 2)}
    return poderm

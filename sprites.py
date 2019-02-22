import pygame as pg
from componentes import *
import sys, os
import epilogo1 as ep1
import math
import random


BLANCO = [250, 250, 250]
NEGRO = [0,0,0]
BLANCO = [255,255,255]
VERDE = [0,255,0]
ROJO = [255,0,0]
AZUL = [0,0,255]
ancho = 660
alto = 640
dist_ataque = 300


class Personaje(pg.sprite.Sprite):
    def __init__(self, m, ancho, alto):
        pg.sprite.Sprite.__init__(self)
        self.m = m
        self.con = 0
        self.accion = 'standby'
        self.dir = 0
        self.lim = len(self.m[self.accion][self.dir])-1
        self.lis = self.m[self.accion]
        self.image = self.lis[self.dir][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = (ancho/2)-16
        self.rect.y = (alto/2)+66
        self.vel_x = 0
        self.vel_y = 0
        self.objs = pg.sprite.Group()
        self.posx_fondo = 0
        self.activateaccion = False
        self.salud = 215
        self.ki=96
        self.fuerza_inicial = 20
        self.fuerza = 20
        self.nivel = 1
        self.barra = 0
        self.resistencia = 0

    def update(self):

        if self.barra == 100:
            self.nivel += 1
            self.fuerza = self.fuerza_inicial * nivel
            self.resistencia += 5
        self.lim = len(self.m[self.accion][self.dir])-1

        if (self.accion != 'golpe2') and (self.accion != 'morir') and (self.accion != 'golpe1') and (self.accion != 'kame'):
            if self.con < self.lim:
                self.con +=1
            else:
                self.con = 0

        if self.activateaccion:
            if self.con < self.lim:
                self.con +=1
            else:
                self.con = 0
                self.accion = 'standby'
                self.vel_x = 0
                self.activateaccion = False

        self.lis = self.m[self.accion]
        self.image = pg.transform.scale(self.lis[self.dir][self.con], [self.rect.width * 3,self.rect.height * 3])
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


class Minion1(pg.sprite.Sprite):
    def __init__(self, m, ancho, alto):
        pg.sprite.Sprite.__init__(self)
        self.m = m
        self.con = 0
        self.accion = 'standby'
        self.lim = len(self.m[self.accion][0])-1
        self.image = self.m[self.accion][0][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = (ancho/2)+45
        self.rect.y = (alto/2)+66
        self.vel_x = 0
        self.vel_y = 0
        self.objs = pg.sprite.Group()
        self.activateaccion = False
        self.xini = (ancho/2)+45
        self.posx_fondo = 0
        self.vida = 80
        self.fuerza = 10
        self.con2 = 40
        self.temp = random.randint(0, 2)

    def update(self):
        # if self.con2 <= 0:
        #     self.temp = random.randint(0, 2)
        #     self.con2 = 40
        # else:
        #     self.con2 -=1

        self.lim = len(self.m[self.accion][0])-1
        if (self.accion != 'golpe') and (self.accion != 'poder'):
            if self.con < self.lim:
                self.con +=1
            else:
                self.con = 0
        if self.activateaccion:
            if self.con < self.lim:
                self.con +=1
            else:
                self.con = 0
                self.accion = 'standby'
                self.activateaccion = False


        self.rect.x = self.posx_fondo + self.xini
        self.image = pg.transform.scale(self.m[self.accion][0][self.con], [self.rect.width * 3,self.rect.height * 3])


class Poder1(pg.sprite.Sprite):
    def __init__(self, m, pos):
        pg.sprite.Sprite.__init__(self)
        self.m = m
        self.accion = 'poder1'
        self.dir = 0
        self.lis = self.m[self.accion]
        self.image = self.lis[self.dir][1]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel_x = 0
        self.velx_fondo = 0

    def update(self):
        self.rect.x = self.vel_x + self.rect.x + self.velx_fondo
        self.lis = self.m[self.accion]
        self.image = pg.transform.scale(self.lis[self.dir][1], [self.rect.width * 2,self.rect.height * 2])

class Poderm(pg.sprite.Sprite):
    def __init__(self, m, pos):
        pg.sprite.Sprite.__init__(self)
        self.m = m
        self.accion = 'poderm'
        self.dir = 0
        self.lis = self.m[self.accion]
        self.image = self.lis[self.dir][1]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel_x = 0
        self.velx_fondo = 0

    def update(self):
        self.rect.x = self.vel_x + self.rect.x + self.velx_fondo
        self.lis = self.m[self.accion]
        self.image = pg.transform.scale(self.lis[self.dir][1], [self.rect.width * 2,self.rect.height * 2])

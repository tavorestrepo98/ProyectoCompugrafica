import pygame as pg
from componentes import *
import sys, os

if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"

BLANCO = [250, 250, 250]
NEGRO = [0,0,0]
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)


class Pant(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.ancho = 660
        self.alto = 620
        self.pantalla = pg.display.set_mode([self.ancho, self.alto])
        pg.display.set_caption("DBZ")

    def main(self):
        # img_gok = pg.image.load('./resource/goku/goku-sprites.png')
        fondo = pg.image.load('./resource/mapas/mapa1/mapa1.png')
        m = spritegoku()
        m2 = spriteminion1()
        goku = Personaje(m, 710, 580)
        minion = Minion1(m2, 710, 580)
        enemigos = pg.sprite.Group()
        enemigos.add(minion)
        jugadores = pg.sprite.Group()
        jugadores.add(goku)
        reloj = pg.time.Clock()
        rl = 8
        fin = False
        pg.mixer.init()
        pg.mixer.music.load('./resource/sonidos/menu2.ogg')
        pg.mixer.music.play(-1)
        while not fin:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        fin = True
            self.pantalla.fill(VERDE)
            pg.display.flip()
            reloj.tick(rl)

        while fin:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        goku.accion = 'walk'
                        goku.dir = 0
                        goku.con = 0
                        goku.vel_x = 6.8
                        rl = 8.9

                    if event.key == pg.K_LEFT:
                        goku.accion = 'walk'
                        goku.dir = 1
                        goku.con = 0
                        goku.vel_x = -6.8
                        rl = 8

                    if event.key == pg.K_a:
                        if goku.activateaccion == False:
                            goku.accion = 'golpe2'
                            goku.con = 0
                            goku.vel_x = 0
                            rl = 8
                            goku.activateaccion = True

                    if event.key == pg.K_s:
                        if goku.activateaccion == False:
                            goku.accion = 'golpe1'
                            goku.con = 0
                            goku.vel_x = 0
                            rl = 8
                            goku.activateaccion = True

                if event.type == pg.KEYUP:
                    if event.key == pg.K_RIGHT:
                        goku.accion = 'standby'
                        goku.dir = 0
                        goku.con = 0
                        goku.vel_x = 0

                    if event.key == pg.K_LEFT:
                        goku.accion = 'standby'
                        goku.dir = 1
                        goku.con = 0
                        goku.vel_x = 0
                    # if event.key == pg.K_a:
                    #     goku.accion = 'standby'
                    #     goku.con = 0
                    #     goku.vel_x = 0

            enemigos.update()
            jugadores.update()
            self.pantalla.fill(VERDE)
            jugadores.draw(self.pantalla)
            enemigos.draw(self.pantalla)
            pg.display.flip()
            reloj.tick(rl)

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
        self.rect.y = (alto/2)-16
        self.vel_x = 0
        self.vel_y = 0
        self.objs = pg.sprite.Group()
        self.activateaccion = False

    def update(self):
        self.lim = len(self.m[self.accion][self.dir])-1

        if (self.accion != 'golpe2') and (self.accion != 'morir') and (self.accion != 'golpe1') and (self.accion != 'kame'):
            if self.con < self.lim:
                self.con +=1
            else:
                self.con = 0

        if self.activateaccion:
            if (self.accion == 'golpe2') or (self.accion == 'golpe1'):
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
        self.accion = 'golpe'
        self.lim = len(self.m[self.accion][0])-1
        self.image = self.m[self.accion][0][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = (ancho/2)+45
        self.rect.y = (alto/2)-16
        self.vel_x = 0
        self.vel_y = 0
        self.objs = pg.sprite.Group()
        self.activateaccion = False

    def update(self):
        self.lim = len(self.m[self.accion][0])-1
        if self.con < self.lim:
            self.con +=1
        else:
            self.con = 0
            self.accion = 'golpe'
        self.image = pg.transform.scale(self.m[self.accion][0][self.con], [self.rect.width * 3,self.rect.height * 3])



if __name__ == '__main__':
    pg.init()
    pantalla = Pant()
    pantalla.main()

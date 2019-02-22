import pygame as pg
from componentes import *
import sys, os
import epilogo1 as ep1
import math
import random
from sprites import *

if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"


BLANCO = [250, 250, 250]
NEGRO = [0,0,0]
BLANCO = [255,255,255]
VERDE = [0,255,0]
ROJO = [255,0,0]
AZUL = [0,0,255]
ancho = 660
alto = 640
dist_ataque = 300

balas = pg.sprite.Group()
jugadores = pg.sprite.Group()
enemigos = pg.sprite.Group()
balaenemiga = pg.sprite.Group()
ob = pg.sprite.Group()
contador=0


class orbes(pg.sprite.Sprite):
    def __init__(self, m, x, y):
        pg.sprite.Sprite.__init__(self)
        self.m = m
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xini = x
        self.posx_fondo=0

    def update(self):
        self.image = pg.transform.scale(self.m[0][0], [self.rect.width * 2, self.rect.height * 2])
        self.rect.x = self.xini + self.posx_fondo


if __name__ == '__main__':
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    pg.display.set_caption("DBZ")
    print('=================INICIANDO===================')

    fondo = pg.image.load('./resource/mapas/mapa1/mapa1.png')
    vida = pg.image.load('./resource/barlife.png')
    posxe = [1000,1100,2000,2100,3000,3100,4000,4100,5000,5100,6000,6100,7000,7100,8000,8100,9000,9100,10000,11000,11000,11100,12000,12100]
    m = spritegoku()
    m2 = spriteminion1()
    m3 = spritejeice()
    mo = recortar(pg.image.load('./resource/poderes/orb.png'), 8, 15, 1, 1)

    for e in posxe:
        minion = Minion1(m2, e, 580)
        enemigos.add(minion)

    jeice=Minion1(m3, 12250, 580)
    enemigos.add(jeice)

    goku = Personaje(m, 768, 580)
    jugadores.add(goku)
    reloj = pg.time.Clock()
    rl = 8
    fin = False
    info = fondo.get_rect()
    print(info)
    ancho_pantalla = info[2]
    lim_pantalla = ancho_pantalla-ancho
    posx_fondo = 0
    velx_fondo = -8
    pg.mixer.init()
    salud_g=215

    ep1.epilogo1(pantalla)

    while not fin:
        keystate = pg.key.get_pressed()

        # for b in balas:
        #     collisio = pg.sprite.spritecollide(b, enemigos, True)
        #     print(collisio,"hola")
        #     for col in collisio:
        #         print("hola2")

        if goku.accion == 'run':
            if (keystate[pg.K_SPACE]==0)and(keystate[pg.K_RIGHT]==1):
                goku.accion = 'walk'
                goku.dir = 0
                goku.con = 0
                goku.vel_x = 8
                rl = 10
                velx_fondo = -8
        else:
            if (keystate[pg.K_SPACE]==1)and(keystate[pg.K_RIGHT]==1):
                goku.accion = 'run'
                goku.dir = 0
                goku.con = 0
                goku.vel_x = 14
                rl = 12
                velx_fondo = -15

        if goku.accion == 'run':
            if (keystate[pg.K_SPACE]==0)and(keystate[pg.K_LEFT]==1):
                goku.accion = 'walk'
                goku.dir = 1
                goku.con = 0
                goku.vel_x = -8
                rl = 10
                velx_fondo = - 8
        else:
            if (keystate[pg.K_SPACE]==1)and(keystate[pg.K_LEFT]==1):
                goku.accion = 'run'
                goku.dir = 1
                goku.con = 0
                goku.vel_x = -14
                rl = 12
                velx_fondo = -15

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    goku.accion = 'walk'
                    goku.dir = 0
                    goku.con = 0
                    goku.vel_x = 8
                    rl = 12

                if event.key == pg.K_LEFT:
                    goku.accion = 'walk'
                    goku.dir = 1
                    goku.con = 0
                    goku.vel_x = -8
                    rl = 12

                if event.key == pg.K_a:
                    if goku.activateaccion == False:
                        goku.accion = 'golpe2'
                        goku.con = 0
                        goku.vel_x = 0
                        rl = 12
                        goku.activateaccion = True
                        ls_colje = pg.sprite.spritecollide(goku, enemigos, False)
                        for i in ls_colje:
                            i.vida-=10
                            if i.vida<=0:
                                orb=orbes(mo, i.rect.x + random.randint(-10, 10) + posx_fondo,i.rect.y + 70)
                                ob.add(orb)
                                i.kill()

                if event.key == pg.K_s:
                    if goku.activateaccion == False:
                        goku.accion = 'golpe1'
                        goku.con = 0
                        goku.vel_x = 0
                        rl = 12
                        goku.activateaccion = True
                        if goku.ki > 0:
                            if goku.dir == 0:
                                b = Poder1(spritepoder1(), [goku.rect.x + goku.rect.width + 25, goku.rect.y + 35])
                                b.dir = 0
                                b.vel_x = 12
                                balas.add(b)
                                goku.ki-=6
                            else:
                                b = Poder1(spritepoder1(), [goku.rect.x - 5, goku.rect.y + 35])
                                b.dir = 1
                                b.vel_x = -12
                                balas.add(b)
                                goku.ki-=6

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

        for b in balas:
            b.velx_fondo = 0
        for b2 in balaenemiga:
            b2.velx_fondo = 0
        for b2 in ob:
            b2.velx_fondo = 0

        if(goku.rect.x >= 400) and (goku.vel_x > 0):
            goku.rect.x = 400
            posx_fondo += velx_fondo
            for b in balas:
                b.velx_fondo = velx_fondo
            for b2 in balaenemiga:
                b2.velx_fondo = velx_fondo

        if (posx_fondo * -1) > lim_pantalla:
            posx_fondo = lim_pantalla * -1

        if(goku.rect.x <= 120) and (goku.vel_x < 0):
            goku.rect.x = 120
            posx_fondo -= velx_fondo
            for b in balas:
                b.velx_fondo = velx_fondo*1
            for b2 in balaenemiga:
                b2.velx_fondo = velx_fondo*1

        if posx_fondo >= 0:
            posx_fondo = 0

        for e in enemigos:
            e.posx_fondo = posx_fondo

        for o in ob:
            o.posx_fondo = posx_fondo


        for e in enemigos:
            if (math.fabs(goku.rect.x - e.rect.x) < dist_ataque) and (math.fabs(goku.rect.x - e.rect.x)>40):
                contador+=1
                if e.activateaccion == False:
                    if contador == 50:
                        e.accion = 'poder'
                        e.con = 0
                        e.activateaccion = True
                        e.rect.x -= 4
                        b = Poderm(spritepoderm(), [e.rect.x - 16, e.rect.y + 30])
                        b.vel_x = -7
                        balaenemiga.add(b)
                        rl = 12
                        contador=0

            elif math.fabs(goku.rect.x - e.rect.x) < 40:
                if e.activateaccion == False:
                    e.accion = 'golpe'
                    e.con = 0
                    e.activateaccion = True
                # if e.temp == 0:
                #     # e.accion = 'standby'
                #     pass
                # elif e.temp == 1:
                #     e.accion = 'golpe'

        for e in balaenemiga:
            if e.rect.x <= (goku.rect.x + (goku.rect.width*2)):
                salud_g-=4
                e.kill()
            '''if salud_g<=0:
                goku.accion='morir'
                salud_g=0'''


        for e in enemigos:
            for b in balas:
                #print(b)
                if e.rect.x <= (b.rect.x + (b.rect.width*2)):
                    e.vida-=20
                    b.kill()
                if e.vida<=0:
                    orb=orbes(mo, e.rect.x,e.rect.y + 70)
                    ob.add(orb)
                    e.kill()

        ls_ob = pg.sprite.spritecollide(goku, ob, False)
        for o in ls_ob:
            goku.ki+=6
            o.kill()
            if goku.ki >= 96:
                goku.ki=96

        for  o in ob:
            if math.fabs(goku.rect.x - o.rect.x) < 15:
                goku.ki+=6
                o.kill()
                if goku.ki >= 96:
                    goku.ki=96




        jugadores.update()
        balas.update()
        enemigos.update()
        balaenemiga.update()
        ob.update()


        pantalla.blit(fondo, [posx_fondo,0])
        pg.draw.rect(pantalla,[127,127,127],[30,30,215,18])
        pg.draw.rect(pantalla,[127,127,127],[30,45,132,14])
        pg.draw.rect(pantalla,VERDE,[30,30,salud_g,18])
        pg.draw.rect(pantalla,AZUL,[66,45,goku.ki,14])
        pantalla.blit(vida,[0,0])

        jugadores.draw(pantalla)
        enemigos.draw(pantalla)
        balas.draw(pantalla)
        balaenemiga.draw(pantalla)
        ob.draw(pantalla)

        pg.display.flip()
        reloj.tick(rl)

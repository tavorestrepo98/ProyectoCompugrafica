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

if __name__ == '__main__':
    pg.init()
    pantalla = pg.display.set_mode([ancho,alto])
    pg.display.set_caption("DBZ")
    print('=================INICIANDO===================')

    fondo = pg.image.load('./resource/mapas/mapa1/mapa1.png')
    posxe = [1300, 1420, 1595, 2400, 2459, 2530, 4330, 4421, 4590]
    m = spritegoku()
    m2 = spriteminion1()


    for e in posxe:
        minion = Minion1(m2, e, 580)
        enemigos.add(minion)

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
                goku.vel_x = 18
                rl = 9
                velx_fondo = -20

        if goku.accion == 'run':
            if (keystate[pg.K_SPACE]==0)and(keystate[pg.K_LEFT]==1):
                goku.accion = 'walk'
                goku.dir = 1
                goku.con = 0
                goku.vel_x = -8
                rl = 12
        else:
            if (keystate[pg.K_SPACE]==1)and(keystate[pg.K_LEFT]==1):
                goku.accion = 'run'
                goku.dir = 1
                goku.con = 0
                goku.vel_x = -14
                rl = 12

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
                        ls_colje = pg.sprite.spritecollide(goku, enemigos, True)

                if event.key == pg.K_s:
                    if goku.activateaccion == False:
                        goku.accion = 'golpe1'
                        goku.con = 0
                        goku.vel_x = 0
                        rl = 12
                        goku.activateaccion = True
                        if goku.dir == 0:
                            b = Poder1(spritepoder1(), [goku.rect.x + goku.rect.width + 25, goku.rect.y + 35])
                            b.dir = 0
                            b.vel_x = 12
                            balas.add(b)
                        else:
                            b = Poder1(spritepoder1(), [goku.rect.x - 5, goku.rect.y + 35])
                            b.dir = 1
                            b.vel_x = -12
                            balas.add(b)

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

        if(goku.rect.x >= 400) and (goku.vel_x > 0):
            goku.rect.x = 400
            posx_fondo += velx_fondo
            for b in balas:
                b.velx_fondo = velx_fondo
            for b2 in balaenemiga:
                b2.velx_fondo = velx_fondo

        if (posx_fondo * -1) > lim_pantalla:
            posx_fondo = lim_pantalla * -1

        if(goku.rect.x <= 20) and (goku.vel_x < 0):
            goku.rect.x = 24
            posx_fondo -= velx_fondo
            for b in balas:
                b.velx_fondo = velx_fondo*-1
            for b2 in balaenemiga:
                b2.velx_fondo = velx_fondo*-1

        if posx_fondo >= 0:
            posx_fondo = 0

        for e in enemigos:
            e.posx_fondo = posx_fondo

        for e in enemigos:
            if (math.fabs(goku.rect.x - e.rect.x) < dist_ataque) and (math.fabs(goku.rect.x - e.rect.x)>40):
                if e.activateaccion == False:
                    e.accion = 'poder'
                    e.con = 0
                    e.activateaccion = True
                    e.rect.x -= 4
                    b = Poderm(spritepoderm(), [e.rect.x - 16, e.rect.y + 30])
                    b.vel_x = -3
                    balaenemiga.add(b)
                    rl = 20
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
                e.kill()


        for e in enemigos:
            for b in balas:
                print(b)
                if e.rect.x <= (b.rect.x + (b.rect.width*2)):
                    b.kill()

        jugadores.update()
        balas.update()
        enemigos.update()
        balaenemiga.update()


        pantalla.blit(fondo, [posx_fondo,0])

        jugadores.draw(pantalla)
        enemigos.draw(pantalla)
        balas.draw(pantalla)
        balaenemiga.draw(pantalla)

        pg.display.flip()
        reloj.tick(rl)

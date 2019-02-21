import pygame as pg
from componentes import *
import sys, os

if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"

BLANCO = [250, 250, 250]
NEGRO = [0,0,0]
BLANCO = [255,255,255]
VERDE = [0,255,0]
ROJO = [255,0,0]
AZUL = [0,0,255]
ancho = 660
alto = 640

balas = pg.sprite.Group()
jugadores = pg.sprite.Group()
enemigos = pg.sprite.Group()

class Pant(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.ancho = 660
        self.alto = 640
        self.pantalla = pg.display.set_mode([self.ancho, self.alto])
        pg.display.set_caption("DBZ")

    def main(self):
        fondo = pg.image.load('./resource/mapas/mapa1/mapa1.png')
        posxe = [1300, 1420, 1595, 2300, 2356, 2430, 4330, 4421, 4590]
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

        while not fin:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        fin = True
            self.pantalla.fill(VERDE)
            pg.display.flip()
            reloj.tick(rl)


        while fin:
            keystate = pg.key.get_pressed()

            for b in balas:
                collisio = pg.sprite.spritecollide(b, enemigos, True)
                print(collisio,"hola")
                for col in collisio:
                    print("hola2")

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
                    rl = 10
            else:
                if (keystate[pg.K_SPACE]==1)and(keystate[pg.K_LEFT]==1):
                    goku.accion = 'run'
                    goku.dir = 1
                    goku.con = 0
                    goku.vel_x = -14
                    rl = 9

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
                        rl = 10

                    if event.key == pg.K_LEFT:
                        goku.accion = 'walk'
                        goku.dir = 1
                        goku.con = 0
                        goku.vel_x = -8
                        rl = 10

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
                            if goku.dir == 0:
                                b = Poder1(spritepoder1(), [goku.rect.x + goku.rect.width + 25, goku.rect.y + 35])
                                b.dir = 0
                                b.vel_x = 17
                                balas.add(b)
                            else:
                                b = Poder1(spritepoder1(), [goku.rect.x - 5, goku.rect.y + 35])
                                b.dir = 1
                                b.vel_x = -17
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
                    # if event.key == pg.K_a:
                    #     goku.accion = 'standby'
                    #     goku.con = 0
                    #     goku.vel_x = 0

            for b in balas:
                b.velx_fondo = 0

            if(goku.rect.x >= 560) and (goku.vel_x > 0):
                goku.rect.x = 560
                posx_fondo += velx_fondo
                for b in balas:
                    b.velx_fondo = velx_fondo


            if (posx_fondo * -1) > lim_pantalla:
                posx_fondo = lim_pantalla * -1

            if(goku.rect.x <= 20) and (goku.vel_x < 0):
                goku.rect.x = 24
                posx_fondo -= velx_fondo
                for b in balas:
                    b.velx_fondo = velx_fondo*-1


            if posx_fondo >= 0:
                posx_fondo = 0

            for e in enemigos:
                e.posx_fondo = posx_fondo

            jugadores.update()
            balas.update()
            enemigos.update()

            self.pantalla.blit(fondo, [posx_fondo,0])

            jugadores.draw(self.pantalla)
            enemigos.draw(self.pantalla)
            balas.draw(self.pantalla)

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
        self.rect.y = (alto/2)+66
        self.vel_x = 0
        self.vel_y = 0
        self.objs = pg.sprite.Group()
        self.posx_fondo = 0
        self.activateaccion = False
        self.vida = 100
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

    def update(self):
        self.ls_col = pg.sprite.spritecollide(self, balas, False)
        #print(self.ls_col)
        print(balas)
        for e in self.ls_col:
            print("hola")
            self.en.remove(e)
        self.lim = len(self.m[self.accion][0])-1
        if self.con < self.lim:
            self.con +=1
        else:
            self.con = 0
            self.accion = 'standby'
        self.rect.x = self.posx_fondo + self.xini
        self.image = pg.transform.scale(self.m[self.accion][0][self.con], [self.rect.width * 3,self.rect.height * 3])


class Poder1(pg.sprite.Sprite):
    def __init__(self, m, pos):
        pg.sprite.Sprite.__init__(self)
        self.m = m
        self.con = 0
        self.accion = 'poder1'
        self.dir = 0
        self.lim = len(self.m[self.accion][self.dir])-2
        self.lis = self.m[self.accion]
        self.image = self.lis[self.dir][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel_x = 0
        self.velx_fondo = 0


    def update(self):

        self.lim = len(self.m[self.accion][self.dir])-2
        if self.con < self.lim:
            self.con +=1
        self.rect.x = self.vel_x + self.rect.x + self.velx_fondo
        self.lis = self.m[self.accion]
        self.image = pg.transform.scale(self.lis[self.dir][self.con], [self.rect.width * 2,self.rect.height * 2])


if __name__ == '__main__':
    pg.init()
    print('=================INICIANDO===================')
    pantalla = Pant()
    pantalla.main()

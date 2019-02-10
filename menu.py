import pygame as pg
import sys, os

if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"

BLANCO = [250, 250, 250]
NEGRO = (0,0,0)
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
        img_gok = pg.image.load('./resource/goku/goku-sprites.png')
        m = recortar(img_gok, 6, 4)
        goku = Personaje(m, 660, 620)
        jugadores = pg.sprite.Group()
        jugadores.add(goku)
        reloj = pg.time.Clock()
        rl = 11
        fin = False
        while not fin:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        fin = True
            self.pantalla.fill(BLANCO)
            pg.display.flip()
            reloj.tick(rl)

        while fin:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        goku.accion = 3
                        goku.con = 0
                        goku.vel_x = -5
                        rl = 7.6
                    if event.key == pg.K_RIGHT:
                        goku.accion = 2
                        goku.con = 0
                        goku.vel_x = 5
                        rl = 7.6
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        goku.accion = 1
                        goku.con = 0
                        goku.vel_x = 0
                    if event.key == pg.K_LEFT:
                        goku.accion = 0
                        goku.con = 0
                        goku.vel_x = 0



            jugadores.update()
            self.pantalla.fill(BLANCO)
            jugadores.draw(self.pantalla)
            pg.display.flip()
            reloj.tick(rl)

class Personaje(pg.sprite.Sprite):
    def __init__(self, m, ancho, alto):
        pg.sprite.Sprite.__init__(self)
        self.m = m
        self.con = 0
        self.accion = 0
        self.lim = 3
        self.image = self.m[self.accion][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = (ancho/2)-16
        self.rect.y = (alto/2)-16
        self.vel_x = 0
        self.vel_y = 0
        self.objs = pg.sprite.Group()

    def update(self):
        if self.con < 3:
            self.con +=1
        else:
            self.con = 0

        self.image = pg.transform.scale(self.m[self.accion][self.con], [80,80])
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


def recortar(imagen, alto, ancho):
    l1 = []
    l2 = []
    for i in range(0, alto):
        for j in range(0, ancho):
            cuadro = imagen.subsurface(j*24, 32*i, 24, 32)
            l2.append(cuadro)
        l1.append(l2)
        l2 = []
    return l1

if __name__ == '__main__':
    print("Hola")


    pantalla = Pant()
    pantalla.main()

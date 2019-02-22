import pygame as pg
import math
import random
import creditos
import menu
import instrucciones
ancho=660
alto=640
centro=[330,320]
blanco=[255,255,255]
negro=[0,0,0]
amarillo=[255,255,0]
rojo=[255,0,0]
verde=[0,255,0]
azul=[0,0,255]


if __name__ == '__main__':
    #inicializacion
    pg.init()
    pantalla=pg.display.set_mode([ancho,alto])

    fondo=pg.image.load('Menu/fondo_menu.png')
    esfera=pg.image.load('Menu/esfera.png')

    fuente=pg.font.SysFont("comicsansms",30)
    texto1=fuente.render("ULTIMATE",True, rojo)
    texto2=fuente.render("PLAY",True, rojo)
    texto3=fuente.render("INSTRUCCIONES",True, rojo)
    texto4=fuente.render("CREDITOS",True, rojo)
    texto5=fuente.render("QUIT",True, rojo)

    b=350
    reloj = pg.time.Clock()
    fin = False
    fin_j=False
    evento=0
    pg.mixer.music.load('resource/sonidos/angels.ogg')
    pg.mixer.music.play(-1)

    while (not fin) and (not fin_j):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    fin = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        evento=1
                    if event.key == pg.K_DOWN:
                        b+=50
                    if event.key == pg.K_UP:
                        b-=50


                if b>500:
                    b=350
                if b<350:
                    b=500
                if b==500 and evento==1:
                    fin=True
                if b==450 and evento==1: #saber si se oprimio enter cuando estaba en creditos
                    pg.mixer.music.stop()
                    creditos.creditos(pantalla)
                    pg.quit()
                    #creditos.creditos()
                if b==400 and evento==1: #saber si se oprimio enter cuando estaba en instrucciones
                    instrucciones.instrucciones(pantalla)
                    pg.mixer.music.stop()
                    pg.mixer.music.load('resource/sonidos/angels.ogg')
                    pg.mixer.music.set_volume(1)
                    pg.mixer.music.play(-1)
                if b==350 and evento==1: #saber si se oprimio enter cuando estaba en play
                    menu.menu(pantalla)


            pantalla.fill(negro)
            pantalla.blit(fondo,[0,0])
            pantalla.blit(texto1,[250,300])
            pantalla.blit(texto2,[250,350])
            pantalla.blit(texto3,[250,400])
            pantalla.blit(texto4,[250,450])
            pantalla.blit(texto5,[250,500])
            pantalla.blit(esfera,[200,b])
            evento=0
            pg.display.flip()
            reloj.tick(60)

import pygame
import math
import random
ancho=660
alto=640
centro=[33,32]
blanco=[255,255,255]
negro=[0,0,0]


def epilogo1(pant):
    pygame.init()
    pantalla=pant
    #imagenes
    fondo=pygame.image.load('fondo1.jpg')
    goku1=pygame.image.load('goku1.png')
    goku2=pygame.image.load('goku2.png')
    goku3=pygame.image.load('goku3.png')
    lista_goku=[goku1,goku2,goku3]

    freezer1=pygame.image.load('freezer1.png')
    freezer2=pygame.image.load('freezer2.png')
    freezer3=pygame.image.load('freezer3.png')
    freezer4=pygame.image.load('freezer4.png')
    lista_freezer=[freezer1,freezer2,freezer3,freezer4]

    nube1=pygame.image.load('nube1.png')
    nube2=pygame.image.load('nube2.png')

    #texto
    fuente=pygame.font.SysFont("comicsansms",20)
    texto1=fuente.render("Devuelveme a mi esposa FREEZERRRRR",True,negro)
    texto2=fuente.render("Ven Por ella Basura",True,negro)
    texto3=fuente.render("Devuelvemela",True,negro)
    texto4=fuente.render("Me vengare Goku, sabandija",True,negro)
    texto5=fuente.render("No Metas a Milk En Nuestros Asuntos",True,negro)
    texto6=fuente.render("Hare Lo que Sea Para Vengarme",True,negro)
    texto7=fuente.render("Te Vencere FREEZERRRRR",True,negro)
    texto8=fuente.render("Tendras Que Vencer A Mi Ejercito",True,negro)

    lista_texto=[texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8]

    fin=False
    con=0
    t=fuente.render("",True,negro)
    while not fin:
        #captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    con+=1

        if con<8 and con>=0:
            if con%2 == 0:
                t=lista_texto[con]
                pantalla.fill([0,0,0])
                pantalla=pygame.display.set_mode([ancho,alto])
                pantalla.blit(fondo,[0,0])
                pantalla.blit(goku1,[0,50])
                pantalla.blit(nube1,[298,0])
                pantalla.blit(t,[320,100])
                pantalla.blit(freezer1,[490,440])
                pantalla.blit(nube2,[230,300])
                pygame.display.flip()
            else:
                t=lista_texto[con]
                pantalla.fill([0,0,0])
                pantalla=pygame.display.set_mode([ancho,alto])
                pantalla.blit(fondo,[0,0])
                pantalla.blit(goku1,[0,50])
                pantalla.blit(nube1,[298,0])
                pantalla.blit(freezer1,[490,440])
                pantalla.blit(nube2,[230,300])
                pantalla.blit(t,[270,400])
                pygame.display.flip()
        else:
            pantalla.fill([0,0,0])
            pantalla=pygame.display.set_mode([ancho,alto])
            pantalla.blit(fondo,[0,0])
            pantalla.blit(goku1,[0,50])
            pantalla.blit(freezer1,[490,440])
            fin = True

        '''t=fuente.render("",True,negro)
        pantalla.fill([0,0,0])
        pantalla=pygame.display.set_mode([ancho,alto])
        pantalla.blit(fondo,[0,0])'''

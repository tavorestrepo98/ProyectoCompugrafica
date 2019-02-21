import pygame
import math
import random
ancho=660
alto=640
centro=[33,32]
blanco=[255,255,255]
negro=[0,0,0]


if __name__ == '__main__':
    #inicializacion
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
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
    fuente=pygame.font.SysFont("comicsansms",15)
    texto1=fuente.render("FREEZERRRRR!!!!!!",True,negro)
    texto2=fuente.render("Como es que llegaste hasta aqui!!!!!!",True,negro)
    texto3=fuente.render("Tu nuca me venceras",True,negro)
    texto4=fuente.render("Te equivocas, Yo soy el mas fuerte",True,negro)
    texto5=fuente.render("No permitire que le hagas danio a Milk",True,negro)
    texto6=fuente.render("Entonces derrotame, Maldito Goku",True,negro)
    texto7=fuente.render("Ahora te demostrare mi grandioso poder!!!",True,negro)
    texto8=fuente.render("Y yo te mostrare el mio Maldito",True,negro)

    lista_texto=[texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8]

    fin=False
    con=-1
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
            if con==1 or con==2:
                f=freezer3
                pos_f=[420,480]
                pos_n2=[200,300]
            else:
                f=freezer4
                pos_f=[520,440]
                pos_n2=[230,300]

            if con>8:
                g=goku2
                pos_g=[0,75]
                pos_n=[260,0]
            else:
                g=goku3
                pos=[0,75]
                pos_n=[300,0]
            if con%2 == 0:
                t=lista_texto[con]
                pantalla.fill([0,0,0])
                pantalla=pygame.display.set_mode([ancho,alto])
                pantalla.blit(fondo,[0,0])
                pantalla.blit(g,pos)
                pantalla.blit(nube1,pos_n)
                pantalla.blit(t,[320,100])
                pantalla.blit(f,pos_f)
                pantalla.blit(nube2,pos_n2)
                pygame.display.flip()
            else:
                t=lista_texto[con]
                pantalla.fill([0,0,0])
                pantalla=pygame.display.set_mode([ancho,alto])
                pantalla.blit(fondo,[0,0])
                pantalla.blit(g,pos)
                pantalla.blit(nube1,pos_n)
                pantalla.blit(f,pos_f)
                pantalla.blit(nube2,pos_n2)
                pantalla.blit(t,[250,400])
                pygame.display.flip()
        else:
            pantalla.fill([0,0,0])
            pantalla=pygame.display.set_mode([ancho,alto])
            pantalla.blit(fondo,[0,0])
            '''pantalla.blit(goku1,[0,50])
            pantalla.blit(freezer1,[490,440])'''

        '''t=fuente.render("",True,negro)
        pantalla.fill([0,0,0])
        pantalla=pygame.display.set_mode([ancho,alto])
        pantalla.blit(fondo,[0,0])'''

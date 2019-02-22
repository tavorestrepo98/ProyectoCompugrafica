import pygame
import math
import random
ancho=660
alto=640
centro=[330,320]
blanco=[255,255,255]
negro=[0,0,0]


if __name__ == '__main__':
    #inicializacion
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    #texto
    fuente=pygame.font.SysFont("comicsansms",45)
    texto1=fuente.render("Cristian Arce",True,blanco)
    texto2=fuente.render("Jhon Mario Bedoya",True,blanco)
    texto3=fuente.render("Gustavo Adolfo Restrepo",True,blanco)

    #imagenes
    logo=pygame.image.load('logo1.png')
    compu=pygame.image.load('compu.png')
    fondo=pygame.image.load('esferas.jpg')
    pos_y_logo=300
    pos_y_compu=800
    pos_y_1=1300
    pos_y_2=1400
    pos_y_3=1500

    fin=False
    while not fin:
        #captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        pos_y_logo-=1
        pos_y_compu-=1
        pos_y_1-=1
        pos_y_2-=1
        pos_y_3-=1
        pantalla.fill([255,255,255])
        pantalla=pygame.display.set_mode([ancho,alto])
        pantalla.blit(fondo,[0,0])
        pantalla.blit(logo,[98,pos_y_logo])
        pantalla.blit(compu,[69,pos_y_compu])
        pantalla.blit(texto1,[85,pos_y_1])
        pantalla.blit(texto2,[85,pos_y_2])
        pantalla.blit(texto3,[85,pos_y_3])
        pygame.display.flip()

        if pos_y_3<-60:
            fin=True

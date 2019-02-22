import pygame
import math
import random
import sys, os
ancho=660
alto=640
centro=[330,320]
blanco=[255,255,255]
negro=[0,0,0]

if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"

def creditos(pant):
    #inicializacion
    pygame.init()
    pantalla=pant
    #texto
    fuente=pygame.font.SysFont("comicsansms",45)
    texto1=fuente.render("Cristian Arce",True,blanco)
    texto2=fuente.render("Jhon Mario Bedoya",True,blanco)
    texto3=fuente.render("Gustavo Adolfo Restrepo",True,blanco)

    #imagenes
    logo=pygame.image.load('Menu/logo1.png')
    compu=pygame.image.load('Menu/compu.png')
    fondo=pygame.image.load('Menu/esferas.jpg')
    pos_y_logo=300
    pos_y_compu=800
    pos_y_1=1300
    pos_y_2=1400
    pos_y_3=1500
    pygame.mixer.music.load('resource/sonidos/corazonencantado.ogg')
    pygame.mixer.music.play(3)

    reloj = pygame.time.Clock()
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

        reloj.tick(40)
    print("========Gracias por Jugar========")
    pygame.quit()
    sys.exit()

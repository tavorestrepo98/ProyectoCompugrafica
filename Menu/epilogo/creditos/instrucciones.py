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

    nube1=pygame.image.load('nube1.png')


    #texto
    fuente=pygame.font.SysFont("comicsansms",20)
    texto1=fuente.render("Hola, Soy Goku",True,negro)
    texto2=fuente.render("Vengo A Enseniarte",True,negro)
    texto3=fuente.render("Como Jugar.",True,negro)
    texto4=fuente.render("Primero: ",True,negro)
    texto5=fuente.render("Usa Las Flechas Para Moverte,",True,negro)
    texto6=fuente.render("Izquierda, Derecha",True,negro)
    texto7=fuente.render("Y Arriba Para saltar.",True,negro)
    texto8=fuente.render("Si Quieres Correr Mas Rapido,",True,negro)
    texto9=fuente.render("Puedes Utilizar Espacio.",True,negro)
    texto10=fuente.render("Ahora Vamos A luchar.",True,negro)
    texto11=fuente.render("Para Dar Un Golpe,",True,negro)
    texto12=fuente.render("Pulsa La Tecla A;",True,negro)
    texto13=fuente.render("Para Dar Un Golpe Fuerte,",True,negro)
    texto14=fuente.render("Pulsa La Tecla S;",True,negro)
    texto15=fuente.render("Para Lanzar Un Poder,",True,negro)
    texto16=fuente.render("Pulsa La Tecla D.",True,negro)
    t=fuente.render("",True,negro)
    lista_texto=[t,texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8,texto9,texto10,texto11,texto12,texto13,texto14,texto15,texto16]

    fin=False
    con=1

    while not fin:
        #captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    con+=1
        if con<17 and con>=0:
            t=lista_texto[con]
            t2=lista_texto[con-1]
            pantalla.fill([0,0,0])
            pantalla=pygame.display.set_mode([ancho,alto])
            pantalla.blit(fondo,[0,0])
            pantalla.blit(goku1,[0,180])
            pantalla.blit(nube1,[150,50])
            pantalla.blit(t2,[175,120])
            pantalla.blit(t,[175,150])
            pygame.display.flip()

        else:
            pantalla.fill([0,0,0])
            pantalla=pygame.display.set_mode([ancho,alto])
            pantalla.blit(fondo,[0,0])
            pantalla.blit(goku1,[0,50])

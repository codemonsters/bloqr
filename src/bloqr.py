import pygame, sys
from pygame.locals import *

WORLD_WIDTH = 256
WORLD_HEIGHT = 256

def mi_error(mensaje):
    print(f"ERROR: {mensaje}")
    pygame.quit()
    sys.exit()


def pantalla_menu():
    global pantalla
    # lectura cola de eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                pantalla = "partida"

    displaysurf.fill((0, 0, 0))
    displaysurf.blit(img_title, (100, 100))


def pantalla_partida():
    # lectura cola de eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    displaysurf.fill((255, 0, 0))


pygame.init()
displaysurf = pygame.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT),  HWSURFACE | DOUBLEBUF)
pygame.display.set_caption('bloqr')
font_title = pygame.font.Font("assets/arcade_i.ttf", 18)
img_title = font_title.render("bloqr", False, (0, 255, 0))

pantalla = "menu"
while True:  # main game loop
    if pantalla == "menu":
        pantalla_menu()
    elif pantalla == "partida":
        pantalla_partida()
    else:
        mi_error("Pantalla no válida")

    pygame.display.update()

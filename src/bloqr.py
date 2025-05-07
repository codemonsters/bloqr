import pygame, sys
from pygame.locals import *

WORLD_WIDTH = 256
WORLD_HEIGHT = 256

pyramid = []    # matriz que contiene información sobre todos los bloques del juego

def mi_error(mensaje):
    print(f"ERROR: {mensaje}")
    pygame.quit()
    sys.exit()


def init_game():
    global pyramid
    pyramid = []
    floor_columns = 7
    for floor_number in range(7):
        floor = []
        for column in range(floor_columns):
            floor.append(0)
        pyramid.append(floor)
        floor_columns -= 1
    print(pyramid)

def pantalla_menu():
    global pantalla
    # lectura cola de eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == VIDEORESIZE:
            #displaysurf.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
            #print(event.dict['size'])
            pass
        elif event.type == VIDEOEXPOSE:  # handles window minimising/maximising
            #displaysurf.fill((0, 0, 0))
            #displaysurf.blit(pygame.transform.scale(pic, screen.get_size()), (0, 0))
            pass
        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                init_game()
                pantalla = "partida"

    displaysurf.fill((0, 0, 0))
    displaysurf.blit(title_img, (100, 100))


def draw_block(x, y):
    displaysurf.blit(block_img, (x + block_img_shift_x, y + block_img_shift_y))


def draw_pyramid(x, y):
    for floor_number, blocks in enumerate(pyramid):
        for col_number in range(len(blocks)):
            draw_block(x + 32 * col_number + 16 * floor_number, y + (6 - floor_number)  * 24)


def pantalla_partida():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurf.fill((0, 0, 0))
    draw_pyramid(16, 32)


pygame.init()
displaysurf = pygame.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT),  HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption('bloqr')
font_title = pygame.font.Font("assets/arcade_i.ttf", 18)
title_img = font_title.render("bloqr", False, (0, 255, 0))
block_img = pygame.image.load('assets/block.png')
block_img_shift_x = -96
block_img_shift_y = -160

pantalla = "menu"
while True:  # main game loop
    if pantalla == "menu":
        pantalla_menu()
    elif pantalla == "partida":
        pantalla_partida()
    else:
        mi_error("Pantalla no válida")

    pygame.display.update()

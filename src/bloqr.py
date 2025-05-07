import pygame, sys
from pygame.locals import *

WORLD_WIDTH = 256
WORLD_HEIGHT = 256

pyramid = []    # matriz que contiene información sobre todos los bloques del juego

def mi_error(mensaje):
    print(f"ERROR: {mensaje}")
    pygame.quit()
    sys.exit()

def get_new_scale_factor(display_x_resolution, display_y_resolution):
    max_x_scale_factor = int(display_x_resolution / WORLD_WIDTH)
    max_y_scale_factor = int(display_y_resolution / WORLD_HEIGHT)
    new_scale_factor = min(max_x_scale_factor, max_y_scale_factor)
    new_scale_factor = max(1, new_scale_factor) # el factor de escala mínimo es 1
    return new_scale_factor

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
    global pantalla, scale_factor
    # lectura cola de eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == VIDEORESIZE:
            new_x_resolution, new_y_resolution = event.dict['size']
            scale_factor = get_new_scale_factor(new_x_resolution, new_y_resolution)
        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                init_game()
                pantalla = "partida"

    draw_surface.fill((0, 0, 0))
    draw_surface.blit(title_img, (100, 100))


def draw_block(x, y):
    draw_surface.blit(block_img, (x + block_img_shift_x, y + block_img_shift_y))


def draw_pyramid(x, y):
    for floor_number, blocks in enumerate(pyramid):
        for col_number in range(len(blocks)):
            draw_block(x + 32 * col_number + 16 * floor_number, y + (6 - floor_number)  * 24)


def pantalla_partida():
    global scale_factor

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == VIDEORESIZE:
            new_x_resolution, new_y_resolution = event.dict['size']
            scale_factor = get_new_scale_factor(new_x_resolution, new_y_resolution)

    draw_surface.fill((0, 0, 0))
    draw_pyramid(16, 32)


pygame.init()

# definimos el factor por el que se multiplicará la superficie draw_surface al mostrarla en display_surface
scale_factor = get_new_scale_factor(int(pygame.display.Info().current_w * 0.7), int(pygame.display.Info().current_h))

display_surface = pygame.display.set_mode((WORLD_WIDTH * scale_factor, WORLD_HEIGHT * scale_factor),  HWSURFACE | DOUBLEBUF | RESIZABLE)
draw_surface = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT),  HWSURFACE | DOUBLEBUF)

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

    scaled_draw_surface = pygame.transform.scale(draw_surface, (WORLD_WIDTH * scale_factor, WORLD_HEIGHT * scale_factor))
    display_surface.fill((0, 0, 0))
    display_surface.blit(scaled_draw_surface, ((display_surface.get_width() - scaled_draw_surface.get_width()) / 2, (display_surface.get_height() - scaled_draw_surface.get_height()) / 2))
    pygame.display.update()

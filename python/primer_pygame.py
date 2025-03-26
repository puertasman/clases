import pygame
from pygame.locals import *

# incialización de tamaño

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() # para controlar la velocidad de la pantalla

# constantes

# variables
cuadrado = pygame.Rect(0, HEIGHT-60, 60, 60)
# posición y tamaño
'''velocidad = 1
aceleracion = 0.1'''
# con vectores
velocidad = [3, -8]
gravedad = 0.4  

# bucle principal
while True:
    for event in pygame.event.get():
        # los eventos es lo que el usuario hace y el programa responde
        if event.type == QUIT:
            exit()
    # actualización de variables
    '''cuadrado.x += velocidad
    velocidad += aceleracion'''
    # con vectores
    cuadrado.x += velocidad[0]
    cuadrado.y += velocidad[1]
    velocidad = [velocidad[0], velocidad[1] + gravedad]
    if cuadrado.y > HEIGHT-60:
        velocidad[1] = 0
        gravedad = 0
    if cuadrado.x > WIDTH-60:
        velocidad[0] = 0
    # dibujo
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), cuadrado)
    pygame.display.flip()
    clock.tick(60)
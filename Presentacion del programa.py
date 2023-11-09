import pygame
import sys

# Iniciamos pygame 
pygame.init()

# Configuracion de pantalla 
ancho_de_pantalla = 800
altura_de_pantalla = 600
screen = pygame.display.set_mode((ancho_de_pantalla, altura_de_pantalla))
pygame.display.set_caption("Jump Score Game")

# Colores
blue = (255, 255, 255)
black = (0, 0, 0)
blue = (150, 150, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Jugador 
ancho_del_jugador = 50
altura_del_jugador  = 50
jugador = pygame.Rect(ancho_de_pantalla // 2, altura_de_pantalla // 2, ancho_del_jugador, altura_del_jugador)
velocidad_del_jugador = 5

# Altura máxima del salto
altura_del_salto = 15 

# Movimientos 
movimiento_en_x = 0
movimiento_en_y = 0
tiempo_en_aire = 0

# Gravedad
gravedad = 0.5

# Plataformas
lista_de_plataformas = []
altura_de_plataforma = 20
ancho_de_plataforma = 200
posicion_de_plataforma = altura_de_pantalla - altura_de_plataforma

for i in range(5):
    plataforma = pygame.Rect(i * ancho_de_plataforma, posicion_de_plataforma, ancho_de_plataforma, altura_de_plataforma)
    lista_de_plataformas.append(plataforma)

# Obstaculos 
lista_de_obstaculos = []
ancho = 30
alto = 30

for i in range(3):
    obstaculos = pygame.Rect(i * 150, posicion_de_plataforma - alto - 20, ancho, alto)
    lista_de_obstaculos.append(obstaculos)

# Bucle principal del juego 
running = True
while running:
    # Fondo de pantalla 
    screen.fill(blue)

    # Eventos 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Asignacion de teclas 
    teclas = pygame.key.get_pressed()

    # Movimientos 
    if teclas[pygame.K_LEFT]:
        movimiento_en_x = -velocidad_del_jugador
    if teclas[pygame.K_RIGHT]:
        movimiento_en_x = velocidad_del_jugador
    # Salto
    if teclas[pygame.K_UP] and tiempo_en_aire == 0:
        movimiento_en_y = -altura_del_salto
        tiempo_en_aire = 1

    movimiento_en_x *= 0.9
    
    # Gravedad del jugador
    if movimiento_en_y < 8:
        movimiento_en_y += gravedad 

    # Verificar colisiones 
    for platform in lista_de_plataformas:
        if jugador.colliderect(platform):
            movimiento_en_y = 0
            tiempo_en_aire = 0
            jugador.bottom = platform.top

    # Verificar colisiones con obstaculos 
    for obstacle in lista_de_obstaculos:
        if jugador.colliderect(obstacle):
            jugador.x = obstacle.left - jugador.width
            movimiento_en_x = 0
    
    # Incrementar el contador de tiempo en el aire
    if tiempo_en_aire > 0:
        tiempo_en_aire += 1

    # Posicion del jugador 
    jugador.x += movimiento_en_x
    jugador.y += movimiento_en_y

    # Dibujos de las plataformas y obstaculos
    for platform in lista_de_plataformas:
        pygame.draw.rect(screen, green, platform)

    for obstacle in lista_de_obstaculos:
        pygame.draw.rect(screen, red, obstacle)

    # Dibujo del jugador 
    pygame.draw.rect(screen, black, jugador)

    # Actualizador de pantalla
    pygame.display.update()

    # Limite de 60 FPS
    pygame.time.Clock().tick(60)

# Salir del juego 
pygame.quit()
sys.exit()

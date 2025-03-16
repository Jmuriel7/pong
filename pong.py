import pygame

# Configuraciones
ANCHO = 640
ALTO = 480
COLOR_FONDO = (0, 50, 0)

class Pong:

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))

    def jugar(self):
        salir = False

        while not salir:
            # Bucle principal (main loop)
            
            # Capturar los eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    print("Has pulsado el botón de cerrar la ventana")
                    salir = True
    
        # renderizar mis objetos (pintar en pantalla)
        # 1. borrar pantalla
        pygame.draw.rect(
            self.pantalla,
            COLOR_FONDO,
            ((0,0), (ANCHO, ALTO)))

        # 2. Pintar los objetos en la posición correspondiente
        rectangulo = pygame.Rect(ANCHO/2 - 125, ALTO/2 - 75, 250, 150)
        pygame.draw.rect(self.pantalla, (10, 68, 158), rectangulo)

        # 3. mostrar los cambios en la pantalla
        pygame.display.flip()

    pygame.quit()


juego = Pong()
juego.jugar()

otro = Pong()
otro.jugar()



import pygame

##############################################################
# Configuraciones
##############################################################
ANCHO = 400
ALTO = 600

ALTO_PALA = 70
ANCHO_PALA = 10
MARGEN = 10


COLOR_FONDO = (0, 0, 0)
COLOR_OBJETOS = (200, 200, 200)

###############################################################

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

            y = (ALTO - ALTO_PALA) / 2
            # Pinto el jugador 1 a la izquierda
            x1 = MARGEN
            jugador1 = pygame.Rect(x1, y, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, COLOR_OBJETOS, jugador1)

            # Pinto el jugador 2
            x2 = ANCHO - MARGEN - ANCHO_PALA
            jugador2 = pygame.Rect(x2, y, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, COLOR_OBJETOS, jugador2)
            

            # 3. mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()


juego = Pong()
juego.jugar()





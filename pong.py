import pygame

##############################################################
# Configuraciones
##############################################################
ALTO = 600
ANCHO = 800

ALTO_PALA = 100
ANCHO_PALA = 10
MARGEN = 30

TAM_PELOTA = 8

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
            
            # pinto la red
            self.pintar_red()



            # pinto la pelota
            xp = (ANCHO - TAM_PELOTA) / 2
            yp = (ALTO - TAM_PELOTA) / 2
            pelota = pygame.Rect(xp, yp, TAM_PELOTA, TAM_PELOTA)
            pygame.draw.rect(self.pantalla, (200, 0, 0), pelota)

            # 3. mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()
    def pintar_red(self):
        """pinta la red en la pantalla"""
        # es una linea discontinua

            # son "muchas" lineas de tamaño "tramo_pintado"
            # con una separación entre ellas "tramo_vacio"
            # la pintamos de color "COLOR_OBJETOS"
            # de un ancho "ancho_red"
        # está centrada horizontalmente
        # ocupa todo el alto de la pantalla
        
        pos_x = ANCHO / 2 - 1
        tramo.pintado = 20
        tramo.vacio = 15
        ancho_red =6

        # bucle:
        # 1. dónde empiezo: pos_y = 0
        # 2. dónde termino: pos_y = ALTO
        # 3. cómo voy de un paso al siguiente: incrementar y en tramo_pintado + tramo_vacio
        # 4. pintar la linea con pygame.draw.line()

        for pos_y in range(0, ALTO, tramo.pintado+tramo.vacio):
            pygame.draw.line(
                self.pantalla,
                COLOR_OBJETOS,
                (pos_x, pos_y),
                (pos_x, pos_y + tramo_pintado),
                ancho_red

            )


juego = Pong()
juego.jugar()





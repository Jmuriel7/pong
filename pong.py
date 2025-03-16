import pygame

class Pong:

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((640, 480))

    def jugar(self):
        pantalla = self.pantalla

        salir = False

        pos_x = 0
        pos_y = 0

        while not salir:
            # Bucle principal (main loop)
            pos_x += 1
            pos_y += 1
            # Capturar los eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    print("Has pulsado el botón de cerrar la ventana")
                    salir = True
    
        # renderizar mis objetos (pintar en pantalla)
        # 1. borrar pantalla
        pygame.draw.rect(self.pantalla, (0, 0, 50), ((0,0), (640,480)))

        # 2. Pintar los objetos en la posición correspondiente
        rectangulo = pygame.Rect(pos_x / 10, pos_y / 20, 250, 150)
        pygame.draw.rect(self.pantalla, (10, 68, 158), rectangulo)

        # 3. mostrar los cambios en la pantalla
        pygame.display.flip()

pygame.quit()


juego = Pong()
juego.jugar()

otro = Pong()
otro.jugar()



import pygame 
import random
class ManchaAceite:
    def __init__(self):
        self.imagen = pygame.image.load("mancha_aceite.png")
        self.imagen = pygame.transform.scale(self.imagen,(50,50))
        self.rect = self.imagen.get_rect()
        self.reiniciar_posicion() 
           
    def reiniciar_posicion(self):
        self.rect.x = random.randint(150,950)
        self.rect.y = -300
    def actualizar(self,largo):
        self.rect.y += 2
        if self.rect.y > largo:
            self.reiniciar_posicion()
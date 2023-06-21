import pygame
import random
from funciones import get_superficies
from coche import get_superficies
class Enemigo(pygame.sprite.Sprite):
    def __init__(self,lista_enemigos):
        super().__init__()
        self.lista_fotograma = get_superficies("enemigos.png", 1, 8, 50, 100)
        self.auto_enemigo = random.choice(self.lista_fotograma)
        self.auto_enemigo = pygame.transform.rotate(self.auto_enemigo, 180)
        self.rect_coche = self.auto_enemigo.get_rect()
        self.lista_coordenadas = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950]
        self.lista_enemigos = lista_enemigos
        self.generar_coordenadas()

    def generar_coordenadas(self):
        overlapping = True
        while overlapping:
            self.rect_coche.x = random.choice(self.lista_coordenadas)
            self.rect_coche.y = -300
            overlapping = False
            for enemigo in self.lista_enemigos:
                if enemigo != self and self.rect_coche.colliderect(enemigo.rect_coche):
                    overlapping = True
                    break
                
    def eleccion_aleatoria(self,lista):
        return random.choice(lista)
    def actualizar(self, velocidad):
        self.rect_coche.y += velocidad 
        if self.rect_coche.y > 680:
            self.generar_coordenadas()

    def dibujar(self, pantalla):
        pantalla.blit(self.auto_enemigo, self.rect_coche) 
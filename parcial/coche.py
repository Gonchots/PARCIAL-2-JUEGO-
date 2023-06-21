import pygame
import time
import random
from funciones import get_superficies
class Auto:
    def __init__(self):
        self.lista_fotograma = get_superficies("carro.png", 1, 2, 50, 100)
        self.pos_inicial = self.lista_fotograma[1]
        self.rect_coche = self.pos_inicial.get_rect()
        self.rect_coche.x = 600
        self.rect_coche.y = 557
        self.estado_juego = False
        
    def dibujar(self, pantalla):
        for fotograma in self.lista_fotograma:
            pantalla.blit(fotograma, self.rect_coche)

    
    def mover_coche(self, keys, pantalla):
        if self.estado_juego:
            return 
        pantalla_rect = pantalla.get_rect()
        if True in keys:
            if keys[pygame.K_RIGHT]:
                self.rect_coche.x += 5
                if self.rect_coche.right >= pantalla_rect.right - 120:
                    self.rect_coche.right = pantalla_rect.right - 120
                
            if keys[pygame.K_LEFT]:
                self.rect_coche.x -= 5
                if self.rect_coche.left <= pantalla_rect.left + 120:
                    self.rect_coche.left = pantalla_rect.left + 120
    def alternar_juego(self,choco):
        if choco:
            self.estado_juego = True
            
    def colision_aceite(self,tiempo_inicial,mancha_aceite):
        if pygame.Rect.colliderect(self.rect_coche,mancha_aceite.rect):
            contador_vueltas = 0
            while contador_vueltas < 90:
                self.rect_coche.x += random.randint (-5,5)
                contador_vueltas += 1
import pygame
class Carretera:
    def __init__(self,alto,ancho):
        self.carretera = pygame.image.load("carretera.png")
        self.carretera = pygame.transform.scale(self.carretera,(ancho,alto))
        self.rect_carretera = self.carretera.get_rect()
        self.rect_carretera.x = 0
        self.rect_carretera.y = 0
        self.segunda_carretera_y = -alto
    def actualizar_fondo(self,pantalla,alto):
        pantalla.blit(self.carretera,(self.rect_carretera.x,self.rect_carretera.y))
        pantalla.blit(self.carretera,(self.rect_carretera.x,self.segunda_carretera_y))
        self.rect_carretera.y += 3
        self.segunda_carretera_y += 3
        if self.rect_carretera.y >= alto:
            self.rect_carretera.y = -alto
        if self.segunda_carretera_y >= alto:
            self.segunda_carretera_y = -alto

        
    
        
        
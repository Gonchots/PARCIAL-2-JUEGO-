import pygame
import sys
from boton import Boton
from funciones import get_superficies
def main_menu(pantalla,ancho,largo):
    pygame.display.set_caption("Menu")
    fondo = pygame.image.load("fondo.png")
    fondo = pygame.transform.scale(fondo,(ancho,largo))
    lista_imagen_menu = get_superficies("menu.png",3,1,350,100)
    musica = pygame.mixer.Sound("musica_menu.mp3")
    musica.set_volume(0.5)
    musica.play(-1)
    
    boton_salir = Boton(lista_imagen_menu[2],450,420,pantalla)
    boton_ranking = Boton(lista_imagen_menu[1],450,310,pantalla)
    boton_jugar = Boton(lista_imagen_menu[0],450,200,pantalla)

    flag_correr = True
    while flag_correr:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_correr = False
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_salir.revisar_posicion(pygame.mouse.get_pos()):
                    flag_correr = False
                    pygame.quit()
                    sys.exit()
                if boton_jugar.revisar_posicion(pygame.mouse.get_pos()):
                    musica.stop()
                    return "JUGAR"
                if boton_ranking.revisar_posicion(pygame.mouse.get_pos()):
                   return "RANKING"

        pantalla.blit(fondo,(0,0))

        boton_jugar.dibujar()

        boton_ranking.dibujar()

        boton_salir.dibujar()
        
        pygame.display.flip()
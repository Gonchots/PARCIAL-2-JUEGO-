import pygame,pygame_gui
from base_datos import *
def get_superficies(path,filas,columnas,ancho,alto):
    lista = []
    superficie_imagen = pygame.image.load(path)
    fotograma_ancho = int(superficie_imagen.get_width()/columnas)
    fotograma_alto = int(superficie_imagen.get_height()/filas)

    for fila in range(filas):
        for columna in range(columnas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            superficie_fotograma = superficie_imagen.subsurface(x,y,fotograma_ancho, fotograma_alto)
            superficie_fotograma = pygame.transform.scale(superficie_fotograma,(ancho,alto))
            lista.append(superficie_fotograma)

    return lista

def game_over(pantalla,puntuacion):
    imagen = pygame.image.load("game_over.png")
    imagen = pygame.transform.scale(imagen,(800,500))
    imagen_rect = imagen.get_rect()
    imagen_rect.x = 175
    imagen_rect.y = 25
    MANAGER = pygame_gui.UIManager((1200, 680))
    entrada_de_texto = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((50,200),(200,50)), manager=MANAGER,object_id="#main_text_entry")
    entrada_de_texto.set_text_length_limit(10)
    flag = True
    while flag:
        pantalla.blit(imagen,imagen_rect)
        RELOJ = pygame.time.Clock()
        UI_REFRESH_RATE = RELOJ.tick(60)/1000
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag = False
        
            if evento.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and evento.ui_object_id == "#main_text_entry":
                crear_tabla_jugadores()
                modificar_tabla_jugadores(evento.text, str(puntuacion))
                

            MANAGER.process_events(evento)
        MANAGER.update(UI_REFRESH_RATE)
        MANAGER.draw_ui(pantalla)
        pygame.display.update() 
        pygame.display.flip()
    pygame.quit()
        

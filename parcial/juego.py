import pygame
import random
import time
from coche import Auto
from carretera import Carretera
from auto_enemigo import Enemigo
from mancha_aceite import ManchaAceite
from menu import main_menu
from base_datos import *
from colores import RED1
from funciones import *

ANCHO_VENTANA = 1200
LARGO_VENTANA = 680

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, LARGO_VENTANA))
pygame.display.set_caption("Carreritas")

auto = Auto()
enemigos = []
velocidades = [3,4]
mancha_aceite = ManchaAceite() 
tiempo_inicial = round(time.time(),2)
tiempo_actual = 0 
puntuacion = 0 


for i in range(5):
    enemigo = Enemigo(enemigos)
    velocidad = enemigo.eleccion_aleatoria(velocidades)
    enemigo.velocidad = velocidad 
    enemigos.append(enemigo)

carretera = Carretera(LARGO_VENTANA, ANCHO_VENTANA)

eleccion = main_menu(pantalla,ANCHO_VENTANA,LARGO_VENTANA)
if eleccion == "JUGAR":
    musica = pygame.mixer.Sound("musica_juego.mp3")
    musica.set_volume(0.5)
    musica.play(-1)
    flag_game = True
    while flag_game:
        tiempo_actual = round(time.time() - tiempo_inicial,1)
        if tiempo_actual == 1:
            tiempo_actual = 0
            puntuacion += 10
        
        carretera.actualizar_fondo(pantalla, LARGO_VENTANA)
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_game = False
        
        keys = pygame.key.get_pressed()
        auto.mover_coche(keys, pantalla)
        auto.dibujar(pantalla)
        auto.colision_aceite(tiempo_inicial,mancha_aceite)
        
        pantalla.blit(mancha_aceite.imagen,mancha_aceite.rect)
        mancha_aceite.actualizar(LARGO_VENTANA)
        
        for bot in enemigos:
            bot.actualizar(bot.velocidad)
            bot.dibujar(pantalla)
            choco = pygame.Rect.colliderect(auto.rect_coche, bot.rect_coche)
            auto.alternar_juego(choco)
            if choco == True:
                game_over(pantalla,puntuacion)
        pygame.display.flip()
    pygame.quit()
elif eleccion == "RANKING":
    musica.stop()
    flag = True
    font = pygame.font.SysFont("Arial",25)
    while flag:
        pantalla.fill((0,0,0))
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag = False
        try: 
            conexion = sqlite3.connect('bd_btf.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre, puntuacion from corredores ORDER BY puntuacion DESC LIMIT 10")
            resultados = cursor.fetchall()
            y = 51
            posicion_juego = 1
            for nombre, puntuacion in resultados:
                texto = font.render(f"{posicion_juego}. {nombre} - {puntuacion}", True, RED1)
                pantalla.blit(texto, (55, y))
                y += 41
                posicion_juego += 1
        except sqlite3.OperationalError:
            pass
        pygame.display.flip()
    pygame.quit()
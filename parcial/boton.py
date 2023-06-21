class Boton():
    def __init__(self,imagen,x,y,pantalla):
        self.imagen = imagen
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.pantalla = pantalla

    def dibujar(self):
        self.pantalla.blit(self.imagen,self.rectangulo)

    def revisar_posicion(self,posicion):
        if posicion[0] in range(self.rectangulo.left,self.rectangulo.right) and posicion[1] in range(self.rectangulo.top,self.rectangulo.bottom): 
            return True
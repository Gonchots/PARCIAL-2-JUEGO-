import sqlite3

def crear_tabla_jugadores():
    with sqlite3.connect("bd_btf.db") as conexion:
        try:
            sentencia = ''' create table corredores
                            (
                                id integer primary key autoincrement,
                                nombre text,
                                puntuacion integer
                            )
                        '''
            conexion.execute(sentencia)
            print("Se creo la tabla jugadores")
        except sqlite3.OperationalError:
            print("La tabla jugadores ya esta creada")

def leer_tabla_jugadores():
    with sqlite3.connect("bd_btf.db") as conexion:
        cursor = conexion.execute("SELECT nombre, puntuacion FROM corredores ORDER BY puntuacion DESC LIMIT 10")
        resultados = cursor.fetchall()

    return resultados

def modificar_tabla_jugadores(nombre,puntuacion):
    with sqlite3.connect("bd_btf.db") as conexion:
        cursor = conexion.cursor()

        cursor.execute("SELECT nombre FROM corredores WHERE nombre = ?", (nombre,))
        registro_existente = cursor.fetchone()

        if registro_existente:
            cursor.execute("UPDATE corredores SET puntuacion = ? WHERE nombre = ?", (puntuacion, nombre))
        else:
            cursor.execute("INSERT INTO corredores (nombre, puntuacion) VALUES (?, ?)", (nombre, puntuacion))

        conexion.commit()
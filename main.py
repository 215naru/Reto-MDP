import logica
import json
from manejo_archivos import palabra_buscada
from manejo_archivos import palabras_validas
from datetime import datetime, timezone
NOMBRE_ARCHIVO = "partidas.json"

def actualizar_partidas(cont):
    try:
        registrar_partidas(cont)
    except FileNotFoundError:
        with open(NOMBRE_ARCHIVO,"w") as archivo:
            json.dump([],archivo)
        registrar_partidas(cont)

def registrar_partidas(cont):
    fecha = datetime.now(timezone.utc).astimezone()
    fecha_str = str(fecha)
    nuevo_dic = {"fecha": fecha_str, "palabra buscada":palabra_buscada, "intentos":cont}
    with open(NOMBRE_ARCHIVO,"r+") as archivo:
        data = json.load(archivo)
        data.append(nuevo_dic)
        archivo.seek(0)
        json.dump(data,archivo,indent=4)

def main():
    cont = 0
    tablero,teclado = logica.inicializar_juego()
    while True:
        print(palabra_buscada)
        logica.mostrar_juego(tablero,teclado)
        if logica.juego_perdido(cont):
            print("Perdiste :(")
            logica.resumir_partida(tablero)
            actualizar_partidas(cont)
            return
        inter = logica.validar_interaccion(palabras_validas)
        n_tablero,n_teclado = logica.actualizar_juego(tablero,teclado,inter,palabra_buscada,cont)
        if n_tablero != tablero:
            tablero = n_tablero
            teclado = n_teclado
        if logica.juego_ganado(inter,palabra_buscada):
            cont+=1
            logica.mostrar_juego(n_tablero,n_teclado)
            print("Ganaste!")
            logica.resumir_partida(tablero)
            actualizar_partidas(cont)
            return
        cont+=1
main()
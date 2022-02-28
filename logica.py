import copy
from operator import le
import re
INTENTOS = 6
LEN_PAL = 5

def inicializar_juego():
    tablero = formar_tablero()
    teclado = formar_teclado()
    return tablero,teclado

def formar_tablero():
    tablero = []
    for fil in range(INTENTOS):
        tablero.append([])
        for _ in range(LEN_PAL):
            tablero[fil].append(" ")
    return tablero

def formar_teclado():
    teclado = []
    teclado_up = ["Q","W","E","R","T","Y","U","I","O","P"]
    teclado_mid = ["A","S","D","F","G","H","J","K","L","Ñ"]
    teclado_down = ["Z","X","C","V","B","N","M"]
    teclado.append(teclado_up)
    teclado.append(teclado_mid)
    teclado.append(teclado_down)
    return teclado

def resumir_partida(tablero):
    color_unic = "\t"
    for fila in tablero:
        for col in fila:
            letra = re.sub("\>|\<|\=","",col)
            if col == f"<{letra}>":
                color_unic += "\U0001F7E8"
            elif col == f">{letra}<":
                color_unic += "\U00002B1C"
            elif col == f"={letra}=":
                color_unic += "\U0001F7E9"
        color_unic += "\n\t"
    print("----RESUMEN DE LA PARTIDA----")
    print(color_unic)
    print("\U0001F7E8 U+1F7E8")
    print("\U00002B1C U+2B1C")
    print("\U0001F7E9 U+1F7E9")

def mostrar_juego(tablero, teclado):
    cols = ""
    color = "\t"
    for filas in tablero:
        for col in filas:
            letra = re.sub("\>|\<|\=","",col)
            if col == f"<{letra}>":
                color += "|"+"\033[30;43m"+"  "+letra+ "  "+"\033[0m"
            elif col == f">{letra}<":
                color += "|"+"\033[30;100m"+"  "+letra+ "  "+"\033[0m"
            elif col == f"={letra}=":
                color += "|"+"\033[30;42m"+"  "+letra+ "  "+"\033[0m"
            else:
                color += "|"+"\033[37;40m"+"  "+letra+ "  "+"\033[0m"
            cols += f"|\t{col}\t"
        cols += "|\n"
        color += "|\n\033[0m\t"
    # print(cols)
    print(color)

    cols_tec = "\t"
    color_tec = "\t"
    for filas in teclado:
        for col in filas:
            letra = re.sub("\>|\<|\=","",col)
            if col == f"<{letra}>":
                color_tec += "\033[30;43m"+"["+"  "+letra+ "  "+"]"+"\033[0m"
            elif col == f">{letra}<":
                color_tec += "\033[30;100m"+"["+"  "+letra+ "  "+"]"+"\033[0m"
            elif col == f"={letra}=":
                color_tec += "\033[30;42m"+"["+"  "+letra+ "  "+"]"+"\033[0m"
            else:
                color_tec += "\033[37;40m"+"["+"  "+letra+ "  "+"]"+"\033[0m"
            cols_tec += f"[{col}]"
        cols_tec += "\n\t"
        color_tec += "\n\033[0m\t"
    # print(cols_tec)
    print(color_tec)
    

def pedir_interaccion(palabras_validas):
    inter = input("Ingrese la palabra:")
    if len(inter)!=LEN_PAL or inter not in palabras_validas :
        raise ValueError
    return inter.upper()

def validar_interaccion(palabras_validas):
    while True:
        try:
            inter = pedir_interaccion(palabras_validas)
            if inter:
                return inter
        except ValueError:
            continue

def actualizar_juego(tablero,teclado,inter,palabra_buscada,cont):
    copia_teclado = copy.deepcopy(teclado)
    copia_tablero = copy.deepcopy(tablero)
    copia_tablero.pop(cont)
    copia_tablero.insert(cont,list(inter))
        
    for i,letra in enumerate(copia_tablero[cont]):
        if letra not in palabra_buscada:
            copia_tablero[cont][i] = ">"+letra+"<"
        elif letra == palabra_buscada[i]:
            copia_tablero[cont][i] = "="+letra+"="
        else:
            copia_tablero[cont][i] = "<"+letra+">"
    ultima_fila = "".join(copia_tablero[cont])

    for fila in copia_teclado:
        for i, letra in enumerate(fila):
            letra = re.sub("\>|\<|\=","",letra)
            if letra in ultima_fila:
                idx = ultima_fila.index(letra)
                fila[i] = ultima_fila[idx-1]+ultima_fila[idx]+ultima_fila[idx+1]
    return copia_tablero,copia_teclado

def juego_ganado(inter,palabra_buscada):
    if inter == palabra_buscada:
        return True
    return False

def juego_perdido(cont):
    if cont == INTENTOS:
        return True
    return False
    
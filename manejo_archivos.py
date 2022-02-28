import funciones_auxiliares
import requests
import random
import json
from datetime import datetime
from logica import LEN_PAL
URL = "https://raw.githubusercontent.com/javierarce/palabras/master/listado-general.txt"
ARCH_DESCARGADO = "descargado.txt"
ARCH_VALIDO = "palabras5.txt"
ARCH_FECHA = "palabras_por_fecha.json"

def escribir_archivo_descargado():
    res = requests.get(URL)
    with open(ARCH_DESCARGADO,"w",encoding="utf8") as archivo:
        archivo.write(res.text)

def leer_archivo():
    with open(ARCH_DESCARGADO,encoding="utf8") as archivo:
        palabras_validas = []
        for palabra in archivo:
            palabra = palabra.rstrip()
            if len(palabra) == LEN_PAL: 
                palabras_validas.append(palabra)
    return palabras_validas

def escribir_archivo_valido(palabras_validas):
    with open(ARCH_VALIDO, "w",encoding="utf8") as archivo:
        for palabra in palabras_validas:
            archivo.writelines(palabra+"\n")

def actualizar_json(palabras_validas):
    palabra_buscada = random.choice(palabras_validas)
    palabra_buscada = palabra_buscada.upper()
    fecha = datetime.today().strftime('%Y-%m-%d')
    fecha_str = str(fecha)
    nuevo_dic = {fecha_str:palabra_buscada}
    with open(ARCH_FECHA,"r+") as archivo:
        data = json.load(archivo)
        for diccionario in data:
            if diccionario.values() == palabra_buscada:
                palabra_buscada = random.choice([ele for ele in palabras_validas if ele != palabra_buscada])
                nuevo_dic = {fecha_str:palabra_buscada}
        data.append(nuevo_dic)
        archivo.seek(0)
        json.dump(data,archivo,indent=4)
    return palabra_buscada

escribir_archivo_descargado()
palabras_validas  = leer_archivo()
palabras_validas = funciones_auxiliares.retirar_tildes(palabras_validas)
escribir_archivo_valido(palabras_validas)
try:
    palabra_buscada = actualizar_json(palabras_validas)
except FileNotFoundError:
    with open(ARCH_FECHA,"w") as archivo:
        json.dump([],archivo)
    palabra_buscada = actualizar_json(palabras_validas)

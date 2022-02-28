def retirar_tildes(palabras_validas):
    dic = {"á":"a","é":"e","í":"i","ó":"o","ú":"u"}
    sin_tildes = []
    for palabra in palabras_validas:
        letras_palabra = list(palabra)
        for i, letra in enumerate(letras_palabra):
            for clave, valor in dic.items():
                if letra == clave:
                    letras_palabra.remove(letra)
                    letras_palabra.insert(i,valor)
        nueva_palabra = "".join(letras_palabra)
        sin_tildes.append(nueva_palabra)
    return sin_tildes

# cadena = ["nímer","ábel","ródriguez"]

# nuevo = retirar_tildes(cadena)
# print(nuevo)
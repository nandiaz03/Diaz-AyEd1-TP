def long_sin_puntuacion(palabras: str)->int:
    """ contrato:
    Pre: palabra es un str.
    Post: devuelve la cantidad de caracteres alfanuméricos de palabra, sin contar los signos de puntuación."""
    cant = 0
    for  caracter in palabras:
        if caracter.isalnum():
            cant += 1
    return cant

def ordenar_por_longitud(cadena: str):
    """Contrato: 
    Pre:  cadena es un str con palabras separadas por uno o más espacios.
    Post: devuelve un nuevo str con las mismas palabras ordenadas de menor a mayor longitud (sin contar signos de puntuación)."""
    palabras = cadena.split()
    palabras_ordenadas = sorted(palabras, key = long_sin_puntuacion)
    return " ".join(palabras_ordenadas)

def main()->None: 
    """contrato: ejecuta el programa principal
    Pre:  ninguna.
    Post: lee una cadena por teclado e imprime sus palabras ordenadas por longitud."""
    cadena = input("Ingrese la cadena: ")
    print(ordenar_por_longitud(cadena))
    
if __name__ == "__main__":
    main()
    
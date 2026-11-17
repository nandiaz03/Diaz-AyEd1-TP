def reemplazar_palabra(cadena:str, palabra_original: str, palabra_nueva: str) -> tuple[str, int]:
    
    """contrato: Esta funcion reemprlaza todas las apariciones en una cadena de caracteres
    precondiciones: cadena, palabra_original y palabra_nueva son strings.
    Postcondiciones: devuelve una tupla (cadena_nueva, cantidad)"""
    palabras = cadena.split()
    palabras_nuevas = []
    cantidad = 0
    for palabra in palabras: 
        if palabra == palabra_original:
            palabras_nuevas.append(palabra_nueva)
            cantidad += 1
        else: 
            palabras_nuevas.append(palabra)
    cadena_nueva = " ".join(palabras_nuevas)
    return cadena_nueva, cantidad

def main()->None: 
    """contrato: ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: imprime la nueva cadena con la palabra reemplazadas y la cantidad de veces que se reemplazo"""
    cadena = input("Ingrese la cadena de caracteres: ")
    palabra_original = input("Ingrese la palabra a cambiar: ")
    palabra_nueva = input("Ingrese la nueva palabra: ")
    cadena_nueva, cantidad = reemplazar_palabra(cadena, palabra_original, palabra_nueva)
    print(f"cadena nueva: {cadena_nueva}")
    print(f"cantidad de reemplazos: {cantidad}")

if __name__ == "__main__":
    main()
def contar_subcadena(cadena: str, subcadena:str)->int:
    """contrato: 
    precondiciones: cadena y subcadena son strings
    postcondiciones: devuelve la cantidad de veces que los caracteres de subcadena aparecen en cadena"""
    cadena_minusculas = cadena.lower()
    subcadena_minusculas = subcadena.lower()
    cantidad = 0
    i = 0
    for caracter in cadena_minusculas:
        if caracter == subcadena_minusculas[i]:
            i += 1
            if i == len(subcadena_minusculas):
                cantidad += 1
                i = 0
    return cantidad

def main()->None: 
    """contrato: Ejecuta el programa principal
    precondiciones: ninguna 
    postcondiciones: imprime la cantidad de veces que la subcadena se en cuentra en la cadena"""
    cadena = input("Ingrese la cadena: ")
    subcadena = input("Ingrese la subcadena: ")
    cantidad = contar_subcadena(cadena, subcadena)
    print(f"Cantidad encontrada: {cantidad}")

if __name__ == "__main__":
    main()    
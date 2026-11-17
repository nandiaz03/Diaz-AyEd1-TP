def extraer_con_rebanada(cadena:str, posicion:int, cantidad:int)->str:
    """ Contrato: Extrae una subcadena indicando la posición de inicio y la cantidad de caracteres, usando slices.
    Precondición: cadena debe ser un str, posicion un entero mayor o igual a 0 y cantidad un entero positivo.
    Postcondición: Devuelve la subcadena obtenida, o los caracteres disponibles  si se piden más de los que quedan."""
    sub = cadena[posicion: posicion + cantidad]
    return sub

def extraer_sin_rebanadas(cadena:str, posicion:int, cantidad:int)->str:
    """Contrato: Extrae una subcadena indicando la posición de inicio y la cantidad de caracteres, sin usar slices
    Precondición: cadena debe ser un str, posicion un entero mayor o igual a 0 y cantidad un entero positivo
    Postcondición: Devuelve la subcadena obtenida, o los caracteres disponibles si se piden más de los que quedan"""
    ultima = posicion + cantidad
    if ultima > len(cadena): 
        ultima = len(cadena)
    subcadena = ""
    i = posicion 
    while i < ultima:
        subcadena += cadena[i]
        i += 1
    return subcadena
    
def main()->None:
    """Contrato: Ejecuta el programa principal
    Precondición: Ninguna
    Postcondición: Muestra el resultado de cada función"""
    cadena = input("ingrese una cadena: ")
    posicion = int(input("Ingrese la posicion de inicion: "))
    cantidad = int(input("Ingrese la cantidad de caracteres: "))
    sub_con = extraer_con_rebanada(cadena, posicion, cantidad)
    sub_sin = extraer_sin_rebanadas(cadena, posicion, cantidad)
    print(f"con rebanada: {sub_con}")
    print(f"sin rebanada: {sub_sin}")

if __name__ == "__main__":
    main()
    
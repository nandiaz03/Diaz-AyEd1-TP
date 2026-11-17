def eliminar_con_rebanadas(cadena: str, posicion:int, cantidad:int)->str: 
    """Contrato: Elimina una subcadena indicando la posición de inicio y la cantidad de caracteres, usando rebanadas
    Precondición: cadena debe ser un str, posicion un entero mayor o igual a 0 y cantidad un entero positivo
    Postcondición: Devuelve la cadena sin la subcadena eliminada. Si se piden más caracteres de los que quedan, elimina hasta el final. Si la posición está fuera de la cadena, la devuelve sin cambios"""
    return cadena[0:posicion] + cadena[posicion + cantidad:]

def eliminar_sin_rebanadas(cadena: str, posicion:int, cantidad:int)->str:
    """Contrato: Elimina una subcadena indicando la posición de inicio y la cantidad de caracteres, sin usar rebanadas.
    Precondición: cadena debe ser un str, posicion un entero mayor o igual a 0 y cantidad un entero positivo.
    Postcondición: Devuelve la cadena sin la subcadena eliminada. Si se piden más caracteres de los que quedan, elimina hasta el final. Si la posición está fuera de la cadena, la devuelve sin cambios."""
    ultima = posicion + cantidad 
    sub = ""
    i = 0
    while i < len(cadena):
        if i < posicion or i >= ultima:
            sub += cadena[i]
        i += 1
    return sub

def main()->None:
    """Contrato: Ejecuta el programa principal.
    Precondición: Ninguna.
    Postcondición: Muestra la cadena resultante de cada función."""
    cadena = input("ingrese una cadena: ")
    posicion = int(input("Ingrese la posicion de inicion: "))
    cantidad = int(input("Ingrese la cantidad de caracteres a eliminar: "))
    sub_con = eliminar_con_rebanadas(cadena, posicion, cantidad)
    sub_sin = eliminar_sin_rebanadas(cadena, posicion, cantidad)
    print(f"con rebanada: {sub_con}")
    print(f"sin rebanada: {sub_sin}")
    
if __name__ == "__main__":
    main()
def ultimos_caracteres(cadena: str, n:int)->str:
    """"Contrato: Devuelve una subcadena con los ultimos n caracteres de una cadena ingresada por el usuario.
    Pre:  cadena es un string y n debe ser un entero positivo.
    Post: devuelve un nuevo str con los últimos n caracteres de cadena, en el mismo orden en que aparecen. La cadena original no se modifica."""
    return cadena[-n:]

def main()->None:
    """ contrato: Ejecuta el programa
    Pre:  ninguna
    Post: lee una cadena y una cantidad n por teclado, e imprime los últimos n caracteres de la cadena."""
    cadena = input("Ingrese los caracteres: ")
    n = int(input("Ingrese la cantidad de caracteres: "))
    ultimos = ultimos_caracteres(cadena, n)
    print(ultimos)
    
if __name__=="__main__":
    main()
    
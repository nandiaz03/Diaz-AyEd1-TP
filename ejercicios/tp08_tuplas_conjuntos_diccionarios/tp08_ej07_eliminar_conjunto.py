def eliminar_numeros(conjunto: set)->None:
    """Contrato: Elimina del conjunto los números que ingresa el usuario
    precondiciones: conjunto es un conjunto de enteros
    postcondiciones: pide números hasta que se ingrese -1, quita cada uno del conjunto con remove y muestra el conjunto tras cada eliminación. Si el número no está, muestra un mensaje de error"""
    numero = int(input("Ingrese un número a eliminar (-1 para terminar): "))
    while numero != -1:
        try: 
            conjunto.remove(numero)
            print(f"conjunto actual: {conjunto}")
        except KeyError: 
            print("Error - El número {numero} no esta en el conjunto")
        numero = int(input("Ingrese un número a eliminar (-1 para terminar): "))
        
def main()->None:
    """Contrato: ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: permite eliminas sus elementos hasta ingresar -1"""
    conjunto = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    print(f"conjunto original: {conjunto}")
    eliminar_numeros(conjunto)
    
if __name__ == "__main__":
    main()
    
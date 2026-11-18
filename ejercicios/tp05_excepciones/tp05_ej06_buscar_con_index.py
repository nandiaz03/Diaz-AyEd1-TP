def cargar_lista()->list[int]:
    """contrato: Esta funcion carga una lista solicitando numeros al usuario 
    precondiciones: los numeros ingresados deben ser enteros
    postcondiciones: Devuelve una list con numeros ingresados por el usuario"""
    lista = []
    numero = int(input("Ingrese un numero entero (-1 para terminar): "))
    while numero != -1:
        lista.append(numero)
        numero = int(input("Ingrese un numero entero (-1 para terminar): "))
    return lista

def buscar_elementos(lista: list[int])->None:
    """Contrato: Busca un elemento en la lista
    precondiciones: ninguna
    postcondiciones: pide números por teclado e imprime la posición que ocupa cada uno en lista, usando el método index + 1"""
    errores = 0
    while errores < 3: 
        numero = int(input("Ingrese el número a buscar: "))
        try: 
            posicion = lista.index(numero)
            print(f"El numero {numero} esta en la posicion {posicion + 1}")
        except ValueError:
            errores += 1
            print(f"Error - el número {numero} no pertenece a la lista")
    print("3 errores acumulados. proceso cancelado")
    
def main()->None:
    """Contrato: Ejecuta el programa principal
    Precondicioens: ninguna
    Postcondiciones:  carga una lista de enteros terminando con -1 y permite buscar la posición de sus elementos hasta detectar el tercer error."""
    lista = cargar_lista()
    buscar_elementos(lista)
    
if __name__ == "__main__":
    main()
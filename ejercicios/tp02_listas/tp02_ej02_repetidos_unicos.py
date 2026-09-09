"""contrato: generar una lista con numeros aleatorios con una cantidad de elementos ingresado por el usuario
precondiciones: el numero ingresado debe ser un numero entero positivo
postdiciones: devolver True si la lista contiene elementos repetidos y devolver una lista con los elementos unicos de la lista"""
import random as rn

def generar_lista(numero:int) -> list[int]:
    """generar una lista con numero aleatorios"""
    lista = []
    for i in range(numero):
        lista.append(rn.randint(1,100))
    return lista

def contiene_repetidos(lista: list[int]) -> bool:
    """Recibir una lista como parámetro y devolver True si la misma contiene algún
    elemento repetido. La función no debe modificar la lista."""
    for i in range(len(lista)):
        contador = lista.count(lista[i])
        if contador > 1:
            return True
        else:
            return False

def elementos_unicos(lista: list[int]) -> list[int]:
    """recibier una lista y devolver una lista con elementos unicos"""
    lista_unicos = []
    for i in range(len(lista)):
        if lista[i] not in lista_unicos:
            lista_unicos.append(lista[i])
    return lista_unicos

def main()->None:
    numero = int(input("ingrese la cantidad de elementos de la lista: "))
    while numero < 0:
        numero = int(input("Ingrese un numero valido: "))
    lista = generar_lista(numero)
    repetidos = contiene_repetidos(lista)
    if repetidos == True:
        print("La lista contiene elementos repetidos")
        lista_unicos = elementos_unicos(lista)
        print(f"Los elementos unicos de la lista son: {lista_unicos}")
    else:
        print(f"La lista no contiene elementos repetidos ")
        print(lista)
        
if __name__ == "__main__":
    main()


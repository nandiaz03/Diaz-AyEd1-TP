"""contrato: generar una lista con los cuadrados de los numeros ingresados y devolver los ultimos 10 elementos de la lista
precondiciones: el numero ingrsado debe ser un numero entero positivo
postdiciones: devuelve una lista con los cuadrados de los numeros y devuelve los ultimos 10 elementos de la lista"""
import random as rn

def generar_cuadrados(numero:int) -> list[int]:
    """generar una lista con los cuadrados de los numeros ingresados"""
    lista = []
    for i in range(20):
        lista.append(rn.randint(1,numero)**2)
    return lista 

def ultimos_elementos(lista:list[int]) -> list[int]:
    """devuelve los ultimos 10 elementos de la lista"""
    lista_ultimos = lista[-10:]
    return lista_ultimos

def main()->None:
    numero = int(input("Ingrese un numero: "))
    while numero < 0:
        numero = int(input("Ingrese un numero valido: "))
    lista = generar_cuadrados(numero)
    lista_ultimos = ultimos_elementos(lista)
    print(f"Los cuadrados de los numeros ingresados son: {lista}")
    print(f"Los ultimos 10 elementos de la lista son: {ultimos_elementos(lista)}")

if __name__ == "__main__":
    main()
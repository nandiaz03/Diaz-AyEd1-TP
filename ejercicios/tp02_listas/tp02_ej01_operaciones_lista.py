import random as rn

"""contrato: Generar una lista con numeros aleatorios de 4 digitos y la cantidad de elementos estara deterinada por un numero de 2 digitos ingresado por el usuario
pre condiciones: el numero ingresado es un numero entero positivo de 2 digitos 
post condiciones: devuelve una lista con numeros aleatorios de 4 digitos, la suma de los elementos, elimina un elemento de la lista si se encuentra y verifica si la lista es capicua"""

def cargar_lista(numero:int)-> lista[int]:
    """armar una lista con numeros aleatorios de 4 digitos"""
    lista = [] 
    for i in range(numero):
        lista.append(rn.randint(1000, 9999))
    return lista

def calcular_producto(lista:lista[int])->int:
    """Calcular el producto de los elementos de la lista"""
    if len(lista) > 0:
        producto = 1
        for i in range(len(lista)):
            producto *= lista[i]
    else:
        producto = 0
    return producto  

def eliminar_elemento(lista:list[int], elemento:int)->list[int]:
    """se solicita un elemento de la lista y se elimina si esta"""
    if elemento in lista: 
        lista.remove(elemento)
        return lista
    else:
        print("El elemento no se encuentra en la lista")
        return lista

def es_capicua(lista:list[int])->bool:
    """verificar si la lista es capicua"""
    lista_invertida = lista.reverse()
    if lista == lista_invertida:
        return True
    else:
        return False

def main()->none:
    numero = int(input("Ingrese un numero de 2 digitos: "))
    while numero < 10 or numero > 99:
        print("Error - el numero ingresado es invalido")
        numero = int(input("Ingrese un numero de 2 digitos: "))
    lista = cargar_lista(numero)
    print(f"a. lista generada: {lista}")
    producto = calcular_producto(lista)
    print(f"b. el producto de los elementos de la lista: {producto}")
    elemento = int(input("ingrese un valor de la lista para eliminarlo: "))
    lista = eliminar_elemento(lista, elemento)
    print(f"c. lista actualizada: {lista}")
    capicua = es_capicua(lista)
    if capicua == True:
        print("d. La lista es capicua")
    else:
        print("d. La lista no es capicua")
        
if __name__ == "__main__":
    main()
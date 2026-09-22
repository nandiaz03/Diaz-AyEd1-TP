"""contrado: Recibir una lista de enteros y devolver una lista de decimales que al sumarlos de 1 
precondiciones: la lista no debe estar vacia y sus elementos deben ser numero enteros mayores a 0
postcondiciones: devuelve una lista con decimales que al sumarlos dan como resultado 1"""

def crear_lista()-> list[int]:
    """Esta funcion solicita numeros y los agrega a la lista"""
    lista = []
    while len(lista) < 3:
        numero = int(input("Ingrese un numero: "))
        if numero > 0: 
           lista.append(numero)
        else: 
            print("numero ingresado invalido")
    return lista

def genera_decimales(suma:int, lista: list[int])->list[float]:
    """Esta funcion pasa los numeros enteros a decimales"""
    lista_decimales = []
    for i in range(len(lista)):
        div = lista[i]/suma
        lista_decimales.append(div)
    return lista_decimales

def main()->None:
    lista = crear_lista()
    suma = sum(lista)
    lista_decimales = genera_decimales(suma, lista)
    print(lista_decimales)
if __name__ == "__main__": 
    main()

import random as rn

def cargar_matriz(cant_fabricas: int)->list[list[int]]:
    """contrato: generar una matriz de tantas fabricas como ingrese el usuario con la cantidad de produccion de fabricas durante una semana
    precondiciones: cantidad de fabricas debe ser un numero mayor a 0
    postcondiciones: devuelve la matriz"""
    matriz = []
    for i in range(cant_fabricas):
        fila = []
        for j in range(6):
            fila.append(rn.randint(0, 150)) 
        matriz.append(fila)    
    return matriz

def opcion_a(matriz: list[list[int]])->None: 
    """contrato: Esta funcion muestra la cantidad total de fabricaciones por fabrica
    precondiciones: matriz no debe estar vacia
    postcondiciones: devuelve el total acumulado de cada fabrica"""
    for i, valores in enumerate(matriz):
        sum_fila = sum(valores)
        print(f"la fabrica {i + 1} produjo un total de {sum_fila}")
    
def opcion_b(matriz: list[list[int]])->int:
    """contrato: esta funcion muestra la mayor produccion en un solo dia por fabrica
    precondiciones: matriz no debe estar vacia
    postcondiciones: devuelve la maxima produccion y el dia de cada fabrica"""
    max_produc = matriz[0][0]
    dia_produc = 0
    fabrica = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] > max_produc: 
                max_produc = matriz[i][j]
                dia_produc = j + 1
                fabrica = i + 1
    return max_produc, dia_produc, fabrica

def opcion_c(matriz: list[list[int]])->int:
    """contrato: cual fue el dia mas productivo teniendo en cuenta todas las fabricas
    precondiciones: matriz no debe estar vacia
    postcondiciones: devuelve la mayor produccion y el dia teniendo en cuenta todas las fabricas."""
    total_produc = []
    suma_produc = 0
    for i in range(len(matriz)):
        for j in range(6):
            suma_produc += matriz[i][j]
        total_produc.append(suma_produc)
    maximo = total_produc.max()
    dia_max = total_produc.index(maximo)
    return maximo, dia_max

def opcion_d(matriz: list[list[int]])->list[int]:
    """contrato: esta funcion devuelbe la menor cantidad fabricada de cada fabrica
    precondiciones: matriz no debe estar vacia
    postcondiciones: devuelve una lista con las menores producciones de cada fabrica"""
    menores = [min(i) for i in matriz]
    return menores

def mostrar_opciones()->None:
    print("a. Cantidad total de bicicletas fabricadas por fabrica")
    print("b. cual es la fabrica que mas produjo en un solo dia")
    print("c. cual fue el dia mas productivo considerndo todas las fabricas combinadas")
    print("d. la menor cantidad fabricada por cada empresa")
    print("0. para salir")
    
def main()->None:
    cant_fabricas = int(input("ingrese la cantidad de fabricas: "))
    while cant_fabricas < 0:
        cant_fabricas = int(input("ingrese una cantidad de fabricas valida: "))
    matriz = cargar_matriz(cant_fabricas)
    print(matriz)
    opcion = "-1"
    while opcion != 0: 
        mostrar_opciones()
        opcion = input("ingrese una opcion: ")
        if opcion == "a":
            opcion_a(matriz)
        elif opcion == "b":
            max_produc, dia_produc, fabrica = opcion_b(matriz)
            print(f"la fabrica que mas produjo fue la {fabrica} el dia {dia_produc} con una produccion de {max_produc}")
        elif opcion == "c":
            maximo, dia_max = opcion_c(matriz)
            print(f"El dia de mayor produccion fue {dia_max} con un total de {maximo} produccciones")
        elif opcion == "d":
            menores = opcion_d(matriz)
            print(menores)
        else: 
            print("opcion incorrecta")
if __name__ == "__main__":
    main()
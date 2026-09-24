def cargar_matriz(numero: int)->list[int[int]]:
    """contrato: cargar datos en la matriz con numeros ingresados por el teclado.
    precondiones: numero debe ser un numero mayor a 0
    postcondiones: retorna una matriz"""
    matriz = []
    for i in range(numero):
        fila = []
        for j in range(numero):
            num = int(input("Ingrese un numero para agregar a la matriz: "))
            fila.append(num)
        matriz.append(fila)    
    return matriz
        
def opcion_a(matriz: list[list[int]])->list[list[int]]:
    """contrato: ordena de forma ascendente cada fila de la matriz
    precondiciones: matriz no debe estar vacia
    postcondiones: retorna una matriz ordenada de forma ascendentes"""
    for i in range(len(matriz)):
        matriz[i].sort()
    return matriz

def opcion_b(matriz: list[list[int]], fila_1: int, fila_2:int)->list[list[int]]:
    """contrato: intercambia de posicion dos filas dentro de la matriz 
    precondiciones: matriz no debe estar vacia y, fila 1 y 2 deben ser numeros dentro del rango de la matriz
    postcondiciones: retorna la matriz con las filas intercambiadas"""
    fila_aux = matriz[fila_1 - 1] 
    matriz[fila_1 - 1] = matriz[fila_2 - 1]
    matriz[fila_2 - 1] = fila_aux
    return matriz
    
def opcion_c(matriz: list[list[int]], colum_1:int, colum_2:int)->list[list[int]]:
    """ contrato: intercambia de posicion dos columnas dentro de la matriz 
        precondiciones: matriz no debe estar vacia y, columna 1 y 2 deben ser numeros dentro del rango de la matriz
        postcondiciones: retorna la matriz con las columnas intercambiadas"""
    for i in range(len(matriz)):
        colum_aux = matriz[i][colum_1 - 1]
        matriz[i][colum_1 - 1] = matriz[i][colum_2 - 1]
        matriz[i][colum_2 - 1] = colum_aux
    return matriz

def opcion_d(matriz: list[list[int]])->list[list[int]]:
    """contrato: intercambia filas por columnas
    precondiciones: matriz no debe estar vacia
    postcondiciones: retorna la matriz con filas y columnas intercambiadas """
    for i in range(len(matriz)): 
        for j in range(i + 1, len(matriz)):
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = matriz[i][j]
    return matriz

def opcion_e(matriz: list[list[int]], fila: int)->float:           
    """ contrato: calcular el promedio de los elementos de una fila especifica
    precondiciones: matriz no debe estar vacia
    postcondiciones:  promedio de los elementos en la fila"""
    suma = sum(matriz[fila])
    promedio = suma/len(matriz[fila])
    return promedio 
    
def opcion_f(matriz: list[list[int]], colum:int)->float:
    """ contrato: calcula el porcentaje de elementos impares en una columna determinada por el usuario
    precondiciones: matriz no debe estar vacia y columna debe ser un numero dentro del rango
    postcondiciones: devuelve el porcentaje de elementos impares"""
    contador = 0
    for i in range(len(matriz)):
        if matriz[i][colum - 1] % 2 != 0:
            contador += 1
    impares = contador/len(matriz) * 100
    return impares     
 
def opcion_g(matriz: list[list[int]])->bool:
    """contrato: determina si una matriz es simetrica respecto a su diagonal principal
    precondiones: matriz no debe estar vacia 
    postcondiones: retorna True si la atriz es asimetrica y False en caso contrario"""
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True
     
def opcion_h(matriz: list[list[int]])->bool:
    """contrato: determina si una matriz es simetrica respecto a su diagonal segundaria
        precondiones: matriz no debe estar vacia 
        postcondiones: retorna True si la atriz es asimetrica y False en caso contrario"""
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i - 1][j - 1] == matriz[j - 1][i - 1]:
                return False
    return True

def opcion_i(matriz: list[list[int]])->None:
    pass
"""Consultar"""    
                

def mostrar_opciones()->None:
    print("a. Ordenar en forma ascendente cada una de las filas de la matriz.")
    print("b. Intercambiar dos filas.")
    print("c. Intercambiar dos columnas dadas.")
    print("d. Trasponer la matriz sobre si misma.")
    print("e. Calcular el promedio de los elementos de una fila")
    print("f. Calcular el porcentaje de elementos con valor impar en una columna.")
    print("g. Determinar si la matriz es simétrica con respecto a su diagonal principal.")
    print("h. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.")
    print("i. Determinar qué columnas de la matriz son palíndromos (capicúas)")
    print("0. para salir")

def main()->None:
    numero = int(input("Ingrese un numero: "))
    while numero <= 0:
        numero = int(input("Ingrese un numero valido: "))
    matriz = cargar_matriz(numero)
    print(matriz)
    opcion = "-1"
    while opcion != "0":
        mostrar_opciones()
        opcion = input("Ingrese una opcion: ")
        if opcion == "a":
            opcion_a(matriz)
            print(matriz)
        elif opcion == "b":
            fila_1 = int(input("ingrese la primer fila a intercambiar: "))
            fila_2 = int(input("ingrese la segunda fila a intercambiar: "))
            matriz = opcion_b(matriz, fila_1, fila_2)
            print(matriz)
        elif opcion == "c":
            colum_1 = int(input("ingrese la primer columna a intercambiar: "))
            colum_2 = int(input("ingrese la segunda columna a intercambiar: "))
            opcion_c(matriz, colum_1,colum_2)
            print(matriz)
        elif opcion == "d":
            opcion_d(matriz)
            print(matriz)
        elif opcion == "e":
            fila = int(input("ingrese la fila: "))
            while fila < len(matriz) or fila > len(matriz):
                fila = int(input("ingrese una fila dentro del rango: "))
            promedio = opcion_e(matriz, fila)
            print(f"el promedio de los elementos de la fila {fila} es de {promedio: .2f}")
        elif opcion == "f":
            colum = int(input("ingrese la columna: "))
            while colum < len(matriz) or colum > len(matriz):
                colum = int(input("ingrese una columna dentro del rango: "))
            impares = opcion_f(matriz, colum)
            print(f"el porcentaje de impares en la columana {colum} es de {impares: .2f}%")
        elif opcion == "g":
            simetrica = opcion_g(matriz)
            if simetrica == True:
                print("la matriz es simetrica")
            else: 
                print("la matriz no es asimetrica")
        elif opcion == "h":
            simetrica = opcion_h(matriz)
            if simetrica == True:
                print("la matriz es simetrica")
            else: 
                print("la matriz no es asimetrica")   
        elif opcion == "i":
            pass
        else:
            print("opcion incorrecta")
        
    numero = int(input("ingrese el numero: "))
    matriz = cargar_matriz(numero)

if __name__ == "__main__":
    main()
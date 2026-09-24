import random as rn

def cargar_sala(n: int, m: int)->list[list[int]]:
    """contrato: carga aleateoriamente si las butacas estan libres o no (0- libre y 1- ocupada)
    precondiciones: n y m debes ser mayores a 0
    postcondiciones: devuelve una matriz"""
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(rn.randint(0, 1)) 
        matriz.append(fila)    
    return matriz

def mostrar_butacas(matriz: list[list[int]], n: int, m: int)->None:
    """contrato: Muestra si las butacas estan disponibles o no
    precondiciones: matriz no debe estar vacia
    postcondiciones: devuelve si cada fila esta o no ocupada"""
    for i in range(n): 
        for j in range(m):
            if matriz[i][j] == 0:
                print(f"En la fila {i + 1} la butaca {j + 1} se encuentra disponible")
            else:
                print(f"En la fila {i + 1} la butaca {j + 1} se encuentra ocupada")
                

def reservar(matriz: list[list[int]], fila: int, butaca: int)->bool:
    """contrato: reserva una butaca en especifica si esta libre
    precondiciones: fila y butaca deben estar dentro de los limites del rango
    postcondiciones: devuelve True si se pudo reservar o False si no"""
    if matriz[fila - 1][butaca - 1] == 0:
        matriz[fila - 1][butaca - 1] = 1
        return True
    else: 
        return False

def butacas_libres(matriz: list[list[int]], n: int, m: int)->int:
    """contrato: Cuenta cuantas butacas libres hay en la sala
    precondiciones: matriz no debe estar vacia
    postcondiciones: devuelve la cantidad de butacas libres en la sala"""
    disponibles = 0
    for i in range(n):
        for j in range(m):
            if matriz[i][j] == 0:
                disponibles += 1
    return disponibles

def butacas_continuas(matriz:list[list[int]], n: int, m: int):   
    pass
    """contrato: busca la secuencia mas larga de butacas libres y seguidas en una misma fila
    precondiciones: matriz no debe estar vacia
    postcondiciones: devuelve las coordenadas de inicio de la secuencia mas larga """        
                 
    
def main()->None:
    n = int(input("ingrese el numero de filas: "))
    while n < 0: 
        n = int(input("ingrese el numero de filas: "))
    m = int(input("ingrese el numero de butacas: "))
    while m < 0:
        m = int(input("ingrese el numero de butacas: "))
    matriz = cargar_sala(n, m)
    mostrar_butacas(matriz, n, m)
    fila =  int(input("Ingrese la fila: "))
    while fila < 0 or fila > n:
        fila =  int(input("Ingrese la fila valida: "))
    butaca = int(input("Ingrese una butaca: "))
    while butaca < 0 or butaca > m:
        butaca = int(input("Ingrese una butaca valida: "))
    confirmar = reservar(matriz, fila, butaca)
    if confirmar == True:
        print(f"La butaca {butaca} en la fila {fila} fue reservada con exito")
    else: 
        print(f"La butaca {butaca} en la fila {fila} se encuentra ocupada, no se pudo completar la reserva")
    disponibles = butacas_libres(matriz, n, m)
    print(f"hay {disponibles} butacas libres")
    
    mostrar_butacas(matriz, n, m)
if __name__ == "__main__":
    main()    
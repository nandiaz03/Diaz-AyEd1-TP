"""Contrato: generar un matriz con numeros aleatorios sin que ningun numero se repita  
precondiciones: numero debe ser mayor a 0
postcondiciones: devuelve una matriz cargada con numeros al azar sin repetir"""
import random as rn

def cargar_matriz(num: int)->list[list[int]]:
    matriz = []
    revisar = []
    for i in range(num):
        fila = []
        for j in range(num):
            agregar = (rn.randint(0, num**2 - 1))
            while agregar in revisar: 
                agregar = (rn.randint(0, num**2 - 1))
            fila.append(agregar)
            revisar.append(agregar) 
        matriz.append(fila)    
    return matriz

def main()->None:
    num = int(input("ingrese un numero: "))
    while num < 0: 
        num = int(input("ingrese un numero: "))
    matriz = cargar_matriz(num)
    print(matriz)

if __name__ == "__main__":
    main()
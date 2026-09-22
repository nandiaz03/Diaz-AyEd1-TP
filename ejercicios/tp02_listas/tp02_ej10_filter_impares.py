"""contrato: generar un lista con numeros al azar entre 1 y 100
precondiciones: 
postcondiciones: """

import random as rn

def generar_lista(cantidad: int)->list[int]:
    lista = []
    for i in range(cantidad): 
        lista.append(rn.randint(1, 101))
    return lista

def impar_lista(valor: int)->bool:
    if valor % 2 != 0: 
        return True
    return False
    

def main()->None:
    cantidad = int(input("ingrese un numero: "))
    while cantidad < 0: 
        cantidad = int(input("ingrese un numero: "))
    lista = generar_lista(cantidad)
    impares = list(filter(impar_lista, lista))
    print(lista)
    print(impares)
    
if __name__=="__main__":
    main()
"""contrato: intercalar los elementos de un lista entre los elementos de otra 
precondiciones: las listas no deben estar vacias
postcondiciones:  devuelve la primer lista con los elementos intercalados"""

def intercalar(lista1: list[int], lista2: list[int])->list[int]:
    for i, elemento in enumerate(lista2):
        lista1[(i*2+1):(i*2+1)] = [elemento]
    return lista1




def main()->None:
    lista1 = [1, 2, 3]
    lista2= [4, 5, 6, 7]
    lista1= intercalar(lista1, lista2)
    print(lista1)
    pass

if __name__=="__main__":
    main()
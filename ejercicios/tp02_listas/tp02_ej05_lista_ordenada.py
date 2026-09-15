"""contrato: 
precondiciones: 
postcondiciones: devolver True si la lista esta ordenada de forma ascendente o False si no es asi."""

def esta_ordenada(lista_enteros:list[int])->bool:
    for i in range(len(lista_enteros) - 1):
        if lista_enteros[i] <= lista_enteros[i+1]:
            return True 
    return False

def str_orden(lista_letras:list[str])->bool:
    for i in range(len(lista_letras) - 1):
        if lista_letras[i] <= lista_letras[i+1]:
            return True
    return False 

def main()->None:
    lista_enteros = [1, 2, 3]
    lista_letras = ["b", "a"]
    orden_enteros = esta_ordenada(lista_enteros)
    
    if orden_enteros == True:
        print(f"{lista_enteros} Esta ordenada de forma ascendente")
    else:
        print(f"{lista_enteros} esta desordenada")
    letras_orden = str_orden(lista_letras)
    if letras_orden == True:
        print(f"{lista_letras} esta ordenada de forma ascendente")
    else: 
        print(f"{lista_letras} esta desordenada")
        
if __name__ == "__main__":
    main()
    
    
           
        
def buscar_clave(diccionario: dict, valor)-> list:
    """contrato: busca las claves de un diccionario
    precondiciones: diccionario debe ser un diccionario
    postcondiciones: devuelve una lista con las claves cuyo valor es igual a valor"""
    claves = []
    for clave in diccionario: 
        if diccionario[clave] == valor:
            claves.append(clave)
    return claves
def main()->None:
    """contrato: ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: prueba buscar_clave con varios casos e imprime los resultados"""
    notas = {"Ana": 8, "Juan": 6, "Martina": 8, "sofia": 8, "Pedro": 4}
    print(f"diccionario: {notas}")
    print(f"claves con valor 8: {buscar_clave(notas, 8)}")
    print(f"claves con valor 6: {buscar_clave(notas, 6)}")  
    print(f"claves con valor 4: {buscar_clave(notas, 4)}")  
    print(f"claves con valor 10: {buscar_clave(notas, 10)}")

if __name__ == "__main__":
    main()
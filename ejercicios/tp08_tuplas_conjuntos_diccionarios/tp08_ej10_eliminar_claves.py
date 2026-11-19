def eliminar_clave(diccionario: dict, claves: list)->tuple:
    """Contrato: elimina de un diccionario las claves que estan en una lista
    precondiciones: diccionario es un diccionario y claves una lista
    postcondiciones: devuelve el diccionario modificado y la cantidad de claves eliminadas"""
    eliminados = 0
    for clave in claves: 
        if clave in diccionario:
            del diccionario[clave]
            eliminados += 1 
    return diccionario, eliminados

def main()->None:
    """Contrato: Ejecuta el programa principal
    precondiciones: ninuna
    postcondiciones: prueba eliminar_claves con varios casos e imprime los resultados"""
    alumnos = {1: "Ana", 2: "Juan", 3: "Martina", 4: "Pedro", 5: "Lucia"}
    print(f"diccionario original: {alumnos}")
    alumnos, cantidad = eliminar_clave(alumnos, [2, 4])
    print(f"tras eliminar[2,4]: {alumnos} - eliminados: {cantidad}")
    alumnos, cantidad = eliminar_clave(alumnos, [1, 7, 9])
    print(f"tras eliminar[1, 7, 9]: {alumnos} - eliminados: {cantidad}")
    alumnos, cantidad = eliminar_clave(alumnos, [10, 11])
    print(f"tras eliminar[10, 11]: {alumnos} - eliminados: {cantidad}")
    alumnos, cantidad = eliminar_clave(alumnos, [])
    print(f"tras eliminar[]: {alumnos} - eliminados: {cantidad}")
    
if __name__ == "__main__":
    main()
        
                
def encajan(ficha_1: tuple[int, int], ficha_2: tuple[int,int])->bool:
    """Contrato: Indica si dos fichas de domino encajan
    precondiciones: ficha_1 y ficha_2 son tuplas de dos enteros entre 0 y 6 
    postcondiciones: devuelve True si las fichas tienen al menos un número en comun y False en caso contrario"""
    comunes = set(ficha_1) & set(ficha_2)
    return len(comunes) > 0 

def verificar(ficha_1: tuple[int, int], ficha_2: tuple[int, int], esperado: bool)-> None:
    """contrato: Prueba de verificacion para ver si el programa funciona correctamente
    precondiciones: Ficha_1 y ficha_2 deben ser tuplas validas 
    postcondiciones: Imprime OK si encajan o Error si no."""
    resultado = encajan(ficha_1, ficha_2)
    if resultado == esperado: 
        print("OK")
    else: 
        print("Error")

def main()->None:
    """contrato: Ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: Imprime el resultado de varios casos de prueba"""
    verificar((3, 4), (4, 6), True)
    verificar((3, 4), (4, 3), True)
    verificar((3, 4), (1, 2), False)
    verificar((6, 6), (1, 6), True)
    verificar((6, 6), (1, 2), False)
    verificar((0, 0), (0, 0), True)   
    
if __name__ == "__main__":
    main()     

def generar_cuadrados()->dict:
    """Contrato: Genera un diccionario de números y sus cuadrados
    precondiciones: ninguna
    postcondiciones: devuelve un diccionario con claves de 1 a 20 y como valor el cuadrado"""
    cuadrados = {}
    for numero in range(1, 21):
        cuadrados[numero] = numero **2
    return cuadrados

def main()->None:
    """contrato: ejecuta el programa principal.
    precondiciones: ninguna.
    postcondiciones: genera e imprime el diccionario de cuadrados."""
    cuadrados = generar_cuadrados()
    print(cuadrados)
    
if __name__ == "__main__":
    main()
    
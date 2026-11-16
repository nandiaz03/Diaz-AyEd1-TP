def separar_claves(clave_maestra: int)->tuple[str,str]:
    """contrato: separa los digitos de la clave maestra en 2 claves.
    precondiciones: clave_maestra debe ser un entero positivo
    postcondiciones: retorna una tupla"""
    digitos = str(clave_maestra)
    clave_1 = ""
    clave_2 = ""
    for i in range(len(digitos)): 
        if i % 2 == 0: 
            clave_1 += digitos[i]
        else:
            clave_2 += digitos[i]
    return clave_1, clave_2

def main()->None:
    """contrato: Ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: muestra en pantalla ambas claves obtenidas"""
    clave_maestra = input("Ingrese la clave maestra: ")
    clave_1, clave_2 = separar_claves(clave_maestra)
    print(f"Clave 1: {clave_1}")
    print(f"clave 2: {clave_2}")
    
if __name__=="__main__":
    main()
ancho = 80

def centrar(cadena: str, ancho: int)->str:
    """contrato: devuelve l cadena con los espacios
    precondiciones: cadena debe ser una string y ancho un entero positivo
    postcondiciones: retorna la cadena centrada"""
    espacios = (ancho - len(cadena)) // 2
    return " " * espacios + cadena
        
def main()->None:
    """contrato: ejecuta el programa
    precondiciones: ninguna
    postcondiciones: muestra la cadena centrada"""
    cadena = input("Ingrese la cadena de caracteres: ")
    cadena_centrada = centrar(cadena, ancho)
    print(cadena_centrada)
    
if __name__=="__main__":
    main()
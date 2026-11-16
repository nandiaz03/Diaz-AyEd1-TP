def es_capicua(cadena: str)-> bool:
    """Contrato: Determina si una cadena es capicua o no
    pre condiciones: cadena debe ser una string
    postcondiciones: Retorna True si es y False en caso de que no""" 
    
    for i in range(len(cadena)//2):
        if cadena[i] != cadena[-(i + 1)]:
            return False
    return True

def main()->None:
    """Contrato: Ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: Muestra en la pantalla si la cadena ingresada es capicua o no"""
    cadena = input("Ingrese los caracteres: ")
    capicua = es_capicua(cadena)
    if capicua == True: 
        print(f"{cadena} es capicua")
    else: 
        print(f"{cadena} no es capicua")
    
if __name__ == "__main__":
    main()    
    
        
    
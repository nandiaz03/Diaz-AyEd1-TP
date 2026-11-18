def sumar_cadenas(cadena_1:str, cadena_2: str)->float:
    """Contrato: suma las cadenas y devuelve su resultado
    precondiciones: cadena_1 y cadena_2 deben ser strings
    postcondicioens: Devuelve la suma de los numeros reales representados por cadena_1 y cadena_2. Si alguna de las dos no contiene un numero valido devuelve -1"""
    try: 
        numero_1 = float(cadena_1)
        numero_2 = float(cadena_2)
    except ValueError:
        return -1
    return numero_1 + numero_2

def main()-> None:
    """contrato: Ejecuta el programa principal
    precondicioens: ninguna
    postcondiciones: imprime el resultado de sumarlas"""
    cadena_1 = input("Ingrese el primer número: ")
    cadena_2 = input("Ingrese el segundo número: ")
    resultado = sumar_cadenas(cadena_1, cadena_2)
    print(f"Resultado: {resultado}")
    
if __name__ == "__main__":
    main()
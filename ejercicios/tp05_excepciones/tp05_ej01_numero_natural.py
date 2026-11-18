def validar_natural(natural: str): 
    """contrato: 
    precondiciones: texto es una string
    postcondiciones: devuelve el numero natural representado por texto"""
    try: 
        numero = float(natural)
    except ValueError: 
        raise ValueError(f"{natural} no es un número entero")
    if not numero.is_integer():
        raise ValueError(f"{natural} no es un número")
    numero = int(numero)
    if numero <= 0:
        raise ValueError(f"{numero} no es mayor a 0")
    return numero 

def main()->None:
    """Contrato: Ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: imprime el valor devuelto"""
    while True: 
        natural = input("Ingrese un número natural: ")
        try: 
            numero = validar_natural(natural)
            break
        except ValueError as error:
            print(f"Error: {error}")
    print(f"Número ingresadao correctamente: {numero}")
        
if __name__ == "__main__":
    main()
    
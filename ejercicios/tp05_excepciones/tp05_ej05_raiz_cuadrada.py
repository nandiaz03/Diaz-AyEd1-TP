import math

def raiz(numero: float)->float:
    """Contrato: Esta funcion recibe como parametro y devuelve la raiz del numero
    precondiciones: numero es un flotante
    postcondiciones: devuelve la raiz cuadrada del numero. En caso de ser negativo lanza ValueError"""
    return math.sqrt(numero)

def main()->None:
    """Contrato: Ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: Imprime la raiz cuadrada del numero ingresado por el usuario"""
    num_texto = input("Ingrese un número: ")
    try: 
        numero = float(num_texto)
    except ValueError:
        print("Error - Debe ingresar un numero")
        return
    
    try:
        resultado = raiz(numero)
        print(f"La raiz cuadrada de {numero} es {resultado}")
    except ValueError:
        print("Error - no se puede calcular la raiz cuadrada de un numero negativo")
        
if __name__ == "__main__":
    main()
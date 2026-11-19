def generar_tabla(num: int):
    """Contrato: Contrato: genera la tabla de multiplicar de un número.
    precondiciones: num es un entero.
    postcondiciones: devuelve un diccionario con claves de 1 a 12 y como valor num multiplicado"""
    tabla = {numero: numero * num for numero in range(1, 13)}
    return tabla

def main()->None:
    """Contrato: Ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: Pide un entero e imprime su tabla de multiplicar del 1 al 12"""
    num = int(input("Ingrese un número: "))
    tabla = generar_tabla(num)
    for numero in tabla:
        print(f"{num} x {numero} = {tabla[numero]}")
        
if __name__ == "__main__":
    main()
    
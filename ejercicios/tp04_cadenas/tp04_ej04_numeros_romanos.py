valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
def convertir_a_romano(numero:int, valores:int, simbolos:str)->str:
    """contrato: convierte un número entero entre 0 y 3999 a número romano
    precondiciones: numero debe ser un entero entre 0 y 3999
    postcondiciones: devuele una string con el numero representado en romano"""
    num_romano = ""
    i = 0
    while i < len(valores): 
        while numero >= valores[i]:
            num_romano += simbolos[i]
            numero -=valores[i]
        i += 1
    return num_romano

def main()->None:
    """contrato: ejecuta el programa y solicita un numero
    precondiciones: ninguna
    postcondiciones: muestra el numero ingresado convertido a romano"""
    numero = int(input("Ingrese el número a convertir: "))
    while numero < 0 or numero > 3999: 
        print("ingrese un numero entre 0 y 3999")
        numero = int(input("Ingrese el número a convertir: "))
    convertir = convertir_a_romano(numero, valores, simbolos)
    print(f"{numero} en números romanos es {convertir}")

if __name__=="__main__":
    main()
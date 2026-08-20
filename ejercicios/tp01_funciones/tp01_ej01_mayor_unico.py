
def numero_positivo():
    """Ingresar 3 numeros y revisar que sean positivos, en caso de no serlo, vuelve a pedirlo"""
    numero_a = int(input("Ingrese un numero: "))
    while numero_a < 0: 
        numero_a = int(input("Ingrese un numero: "))
    numero_b = int(input("Ingrese un numero: "))
    while numero_b < 0:
        numero_b = int(input("Ingrese un numero: "))
    numero_c = int(input("Ingrese un numero: "))
    while numero_c < 0:
        numero_c = int(input("Ingrese un numero: "))
    return numero_a, numero_b, numero_c

def mayor():
    """Busca el mayor de los numros ingresados y devuelve el mayor si es unico, sino devuelve -1"""
    numero_a, numero_b, numero_c = numero_positivo()
    if numero_a > numero_b and numero_a > numero_c:
        print(f"el numero mayor es {numero_a}")
    elif numero_b > numero_a and numero_b > numero_c:
        print(f"el numero mayor es {numero_b}")
    elif numero_c > numero_a and numero_c > numero_b:
        print(f"el numero mayor es {numero_c}")
    else: 
        print("-1")

mayor()

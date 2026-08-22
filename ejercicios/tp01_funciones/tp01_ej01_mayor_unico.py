""" pre condicion: ninguno de los numeros ingresados es negativo
    post condicion: post condicion:devuelve el mayor si es unico, sino devuelve -1"""

def numero_positivo():
    """El usuario ingresa 3 numeros y la funcion valida que sean positivos"""
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
    """Busca el mayor de los numeros ingresados y devuelve -1 si no es unico"""
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

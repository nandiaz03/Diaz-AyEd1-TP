"""El usuario ingresa dos números y devuelve un numero resultante de la combinacion de amobos
   pre condiciones: los números ingresados deben ser enteros positivos
   post condicion: devolver el número resultante del conjunto de ambos numeros"""

numero_1 = int(input("Ingrese el primer número: "))
while numero_1 < 0:
    numero_1 = int(input("Error - Ingrese un número positivo: "))
numero_2 = int(input("Ingrese el segundo número: "))
while numero_2 < 0:
    numero_2 = int(input("Error - Ingrese un número positivo: "))

def numero_completo(numero_1, numero_2):
    """juntar los numeros ingresados en un solo número"""
    aux = numero_2
    multiplicador = 1
    while aux > 0:
        multiplicador = multiplicador * 10
        aux = aux // 10
    return (numero_1 * multiplicador) + numero_2

numero_final = numero_completo(numero_1, numero_2)
print(f"El número resultante es: {numero_final}")

    
   




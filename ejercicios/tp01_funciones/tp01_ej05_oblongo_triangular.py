"""Solicitar al usuario un numero entero """
numero = int(input("Ingrese un número entero: "))

def oblongo(numero):
    resultado = round(numero ** (1/2))
    verificar = resultado * (resultado + 1)
    if verificar == numero:
        print("Es oblongo")
    else:
        print("No es oblongo")
        
oblongo(numero)

def triangular(numero):
    verificar = (numero * 8 + 1) ** (1/2)
    if verificar == round(verificar):
        print("Es triangular")
    else:
        print("No es triangular")

triangular(numero)

"""Solicitar al usuario un numero entero """
numero = int(input("Ingrese un número entero: "))

def oblongo(numero):
    resultado = round(numero ** (1/2))
    verificar = resultado * (resultado + 1)
    if verificar == numero:
       return True
    else:
       return False
        
oblongo(numero)

def triangular(numero):
    verificar = (numero * 8 + 1) ** (1/2)
    if verificar == round(verificar):
        return True
    else:
        return False

triangular(numero)

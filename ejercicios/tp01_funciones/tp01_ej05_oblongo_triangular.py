"""Solicitar al usuario un numero entero 
    pre condicion: el numero ingresado debe ser un numero entero y positivo
    post condicion: devuelve true si el numero es oblongo, false en caso contrario y true si el numero es triangular, false en caso contrario"""

numero = int(input("Ingrese un número: "))
while numero < 0:
    numero = int(input("Numero invalido. Ingrese un número positivo: "))
    
def oblongo(numero):
    resultado = round(numero ** (1/2))
    verificar = resultado * (resultado + 1)
    if verificar == numero:
       return True
    else:
       return False
        
validar_oblongo = oblongo(numero)
if validar_oblongo == True:
    print(f"El numero {numero} es oblongo")
else: 
    print(f"El numero {numero} no es oblongo")

def triangular(numero):
    verificar = (numero * 8 + 1) ** (1/2)
    if verificar == round(verificar):
        return True
    else:
        return False

validar_triangular = triangular(numero)
if validar_triangular == True:
    print(f"El numero {numero} es triangular")
else: 
    print(f"El numero {numero} no es triangular")
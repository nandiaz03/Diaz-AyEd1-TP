import random 

def adivinar_numero(numero_secreto: int)->int:
    """Contrato: 
    precondiciones: El numero_secreto debe estar ente 1 y 500
    postcondicioens: """
    intentos = 0
    acierto = False
    while not acierto: 
        numero_texto = input("Ingrese un numero entre 1 y 500: ")
        intentos += 1
        try:
            numero = int(numero_texto)
            if numero == numero_secreto:
                acierto = True
            elif numero_secreto > numero:
                print("El número a adivinar es mayor")
            else:
                print("El número a adivinar es menor")
        except ValueError:
            print("Error- debe ingresar un número")
    return intentos
    
def main()->None:
    """Contrato: Ejecuta el programa principal
    PRecondiciones: ninguna
    Postcondiciones: imprime si el usuario adivino el numero, en caso de que no le indica si es mayor o menor al numero ingresado"""
    numero_secreto = random.randint(1, 500)
    intentos = adivinar_numero(numero_secreto)
    print(f"¡Felicidades has acertado! lo conseguiste en {intentos} intentos")
    
if __name__ == "__main__":
    main()
"""contrato: 
precondiciones:
postcondiciones: """

def main()->None:
    numero_a = int(input("ingrese un numero: "))
    numero_b = int(input("ingrese un numero: "))
    while numero_a > numero_b:
        print("ingrese un numero mayor al anterior")
        numero_b = int(input("ingrese un numero: "))
    lista = [valor for valor in range(numero_a, numero_b + 1) if valor % 7 == 0 and valor % 5 != 0]
    print(lista)
    
if __name__ == "__main__":
    main()
def main()->None:
    """Contrato: Ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: imprime los números enteros de 1 a 100000, uno por línea. Si se presiona Ctrl-C (KeyboardInterrupt), pide confirmación.
    si el usuario responde "s" el programa se detiene, y con cualquier otra respuesta continúa imprimiendo.""" 
    print("precione Ctrl-C para dener el programa")
    for numero in range(1, 100_001):
        try: 
            print(numero)
        except KeyboardInterrupt: 
            pausar = input("¿Esta seguro de pausar el programa? (ingrese s o n): ")
            if pausar.lower() == "s": 
                break 

if __name__ == "__main__":
    main()
    
                
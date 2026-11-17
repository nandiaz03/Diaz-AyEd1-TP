def crear_baraja(palos: list[str])->list[str]:
    """Contrato: 
    precondiciones: ninguna
    postcondiciones: devuelve una lista y la cantidad de cartas"""
    numeros = [numeros for numeros in range(1,13)]
    baraja = [f"{numero} {palo}" for palo in palos for numero in numeros]
    return baraja

def main()->None:
    """Contrato: Ejecuta la funcion principal
    precondiciones: ninguna
    postondiciones imprime una lista y la cantidad de cartas"""
    palos = ["oro", "basto", "espada", "copa"]
    baraja = crear_baraja(palos)
    print(baraja)
    cantidades = len(baraja)
    print(f"cantidad de cartas: {cantidades}")
    
if __name__ == "__main__":
    main()
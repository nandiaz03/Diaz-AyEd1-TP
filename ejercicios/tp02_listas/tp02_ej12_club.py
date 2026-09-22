"""contrato: el usuario registra los ingresos de cada socio y puede eliminarlos
precondicionales: el numero de socio debe ser un entero
postcondicionales: muestra una lista, cantidad de ingresos de cada socio y elimina resgistros de ingreso"""

def cargar_socios()->list[int]: 
    lista_socios = []
    num_socio = int(input("Ingrese el número de socio (0 para salir): "))
    while num_socio != 0:
        while (num_socio < 10_000 or num_socio > 99_999) and num_socio != 0:
            num_socio = int(input("Ingrese el número de socio (0 para salir): "))
        if num_socio == 0: 
            break
        lista_socios.append(num_socio)
    return lista_socios

def opcion_a(lista_socios: list[int])->None:
    cant_socios = []
    for valor in lista_socios:
        if valor in cant_socios: 
            continue
        else: 
            cant_socios.append(valor)
            contador = lista_socios.count(valor)
            print(f"El socio {valor} ingreso {contador} veces al club")

def opcion_b(lista_socios: list[int]):
    pass


def mostrar_opciones()->None:
    print("a. Cantidad de veces ingreso cada socio.")        
    print("b. Eliminar registros de ingreso e informar cuantos se eliminaron.")   
    print("0. para salir.")   

def main()->None: 
    lista_socios = cargar_socios()
    mostrar_opciones()
    opcion = input("ingrese una opcion: ")
    while opcion != "0": 
        if opcion == "a":
            pass
        elif opcion == "b":
            pass
        else: 
            print("opcion invalida")
if __name__ == "__main__":
    main()
"""contrato: el usuario registra los ingresos de cada socio y puede eliminarlos
precondicionales: el numero de socio debe ser un entero
postcondicionales: muestra una lista, cantidad de ingresos de cada socio y elimina resgistros de ingreso"""

def cargar_socios()->list[int]: 
    lista_socios = []
    num_socio = int(input("Ingrese el número de socio (0 para salir): "))
    while num_socio != 0:
        while (num_socio < 10_000 or num_socio > 99_999) and num_socio != 0:
            print("numero ingresado invalido.")
            num_socio = int(input("Ingrese el número de socio (0 para salir): "))
        if num_socio == 0: 
            break
        lista_socios.append(num_socio)
        num_socio = int(input("Ingrese el número de socio (0 para salir): "))
    return lista_socios

def opcion_a(lista_socios: list[int])->None:
    socios_vistos = []
    for valor in lista_socios:
        if valor in socios_vistos: 
            continue
        else: 
            socios_vistos.append(valor)
            contador = lista_socios.count(valor)
            print(f"El socio {valor} ingreso {contador} veces al club")

def opcion_b(lista_socios: list[int])->None:
    baja_socio = int(input("Ingrese el número de socio a dar de baja: "))
    while baja_socio < 10_000 or baja_socio > 99_999:
        print("numero ingresado invalido.")
        baja_socio = int(input("Ingrese el número de socio a dar de baja: "))
    eliminados = 0
    while baja_socio in lista_socios: 
        lista_socios.remove(baja_socio)
        eliminados += 1
    print(f"se eliminaron {eliminados} ingresos de {baja_socio}")

def mostrar_opciones()->None:
    print("a. Cantidad de veces ingreso cada socio.")        
    print("b. Eliminar registros de ingreso e informar cuantos se eliminaron.")   
    print("0. para salir.")   

def main()->None: 
    lista_socios = cargar_socios()
    mostrar_opciones()
    opcion = "-1"
    while opcion != "0": 
        opcion = input("ingrese una opcion: ")
        if opcion == "a":
            opcion_a(lista_socios)
        elif opcion == "b":
            opcion_b(lista_socios)
        else: 
            print("opcion invalida")
            
if __name__ == "__main__":
    main()
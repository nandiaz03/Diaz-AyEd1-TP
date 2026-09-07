import random as rn
"""Ingresar la cantidad de naranjas, clasificarlas según su tamaño y determinar cuántos cajones se necesitan para guardarlas.
    pre condiciones: la cantidad de naranjas es un número entero positivo
    Postcondición: Informar la cantidad de cajones completos, naranjas para jugo, naranjas sobrantes y camiones necesarios para transportar la cosecha."""
 
def generar_peso(naranjas:int)->list[int]:
    """generar una lista con el peso de las naranjas de forma aleatoria""" 
    peso = []
    for i in range(naranjas): 
        peso.append(rn.randint(150,350))
    return peso

def clasificar_naranjas(peso:list[int])->tuple[int, int, int]: 
    """Clasificar las naranajas"""
    jugo = 0
    naranjas_aptas = 0
    peso_cajon = 0
    for i in range(len(peso)):
        if peso[i] >= 200 and peso[i] <= 300:
            naranjas_aptas += 1
            peso_cajon += peso[i]
        else:
            jugo += 1
    
    return naranjas_aptas, peso_cajon, jugo

def cant_camiones(cajones_completos:int, peso_cajon:float)->int:
    """Calcular la cant de camiones que se requieren"""
    capacidad_maxima = 500
    carga_minima = 500 * 0.8 
    camiones = 0
    peso_total = peso_cajon
    while peso_total > 0:
        if peso_total >= carga_minima:
            camiones += 1
            if peso_total >= capacidad_maxima:
                peso_total -= capacidad_maxima
            else:
                peso_total = 0
        else:
            break
    return camiones

def main()-> None:
    naranjas = int(input("Ingrese la cantidad de naranjas: "))
    while naranjas < 0:
        print("Error - la cantidad de naranjas es invalida")
        naranjas = int(input(" Ingrese la cantidad de naranjas: "))
    peso = generar_peso(naranjas)
    naranjas_aptas, peso_cajon, jugo = clasificar_naranjas(peso)
    peso_cajon_kg = peso_cajon / 1000 
    """paso el peso de gramos a kilogramos para poder calcular la cant de camiones"""
    cajones_completos = naranjas_aptas//100
    sobrante = naranjas_aptas - cajones_completos * 100
    camiones = cant_camiones(cajones_completos, peso_cajon_kg)    
    print(f"se pueden llenar {cajones_completos}.")
    print(f"{jugo} naranjas son para jugo.")
    print(f"sobraron {sobrante} naranjas para la proxima entrega.")
    print(f"se necesitan {camiones} camiones para transportar la cosecha.")
    
if __name__ == "__main__":
    main()
        
""""Solicitar al usuario la cantidad de viajes en subte que realizó durante el mes
    pre condicion: la cantidad de viajes ingresada es un numero entero positivo
    post condicion: devuelve el gasto total en subte según la cantidad de viajes realizados"""
    
cant_viajes = int(input("Ingrese la cantidad de viajes del mes: "))
while cant_viajes < 0:
        cant_viajes = int(input("Ingrese la cantidad de viajes del mes: "))

def calcular_costo(cant_viajes):
    """Calcular el gasto total en subte según la cantidad de viajes realizados"""
    
    if cant_viajes <= 20:
        costo = 1680    
    elif cant_viajes <= 30:
        costo = 1680 * 0.8
    elif cant_viajes <= 40:
        costo = 1680 * 0.7
    else: 
        costo = 1680 * 0.6
    return  costo * cant_viajes

costo_total = calcular_costo(cant_viajes)   
print(f"El gasto total en subte es: {costo_total: .2f}")


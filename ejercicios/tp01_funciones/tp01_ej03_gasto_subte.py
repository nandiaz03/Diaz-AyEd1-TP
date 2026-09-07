""""Solicitar al usuario la cantidad de viajes en subte que realizó durante el mes
    pre condicion: la cantidad de viajes ingresada es un numero entero positivo
    post condicion: devuelve el gasto total en subte según la cantidad de viajes realizados"""
    
cant_viajes = int(input("Ingrese la cantidad de viajes del mes: "))
while cant_viajes < 0:
        cant_viajes = int(input("Ingrese la cantidad de viajes del mes: "))
base = 1680 
descuento_1 = base * 0.8
descuento_2 = base * 0.7
descuento_3 = base * 0.6

def calcular_costo(cant_viajes):
    """Calcular el gasto total en subte según la cantidad de viajes realizados"""
    
    if cant_viajes <= 20:
        return base * cant_viajes
    elif cant_viajes <= 30:
        return 20 * base + descuento_1 * (cant_viajes - 20)
    elif cant_viajes <= 40:
        return 20 * base + descuento_1 * 10 + descuento_2 * (cant_viajes - 30)
    else: 
        return  20 * base + descuento_1 * 10 + descuento_2 * 10 + descuento_3 * (cant_viajes - 40)

costo_total = calcular_costo(cant_viajes)   
print(f"El gasto total en subte es: {costo_total: .2f}")


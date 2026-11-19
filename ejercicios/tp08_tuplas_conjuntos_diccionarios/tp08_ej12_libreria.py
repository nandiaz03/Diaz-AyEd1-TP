def crear_lista_precios()->dict:
    """ Contrato: crea la lista de precios de la librería
    precondiciones: ninguna
    postcondiciones: devuelve un diccionario con el nombre de cada ítem como clave y su precio como valor"""
    precios = {
        "Cuaderno tapa dura": 1200,
        "Cuaderno espiral": 800,
        "Lapicera": 350,
        "Goma": 150,
        "Carpeta": 2500,
        "Atlas": 8000,
    }
    return precios

def aumentar_cuadernos(precios: dict)->None:
    """Contrato: aumentar un 15% el precio de los cuadernos
    precondiciones: precios es un diccionario con nombres como clave y precios como valor
    postcondiciones: modifica precios, aumentando un 15% los ítems cuyo nombre contiene "cuaderno"""
    for item in precios:
        if "cuaderno" in item.lower():
            precios[item] = precios[item] * 1.15
            
def item_costoso(precios: dict)->str:
    """contrato: busca el ítem más costoso de la lista
    precondiciones: diccionario no debe estar vacío 
    postcondiciones: devuelve el nombre del ítem con el precio más alto"""
    costoso = ""
    precio_mayor = 0
    for item in precios:
        if precios[item] > precio_mayor:
            precio_mayor = precios[item]
            costoso = item
    return costoso
    
def main()->None:
    """contrato: ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: crea la lista de precios, aumenta los cuadernos un 15%, imprime la lista e indica el ítem más costoso"""
    precios = crear_lista_precios()
    aumentar_cuadernos(precios)
    for item in precios:
        print(f"{item}: ${precios[item]: .2f}")
    costoso = item_costoso(precios)    
    print(f"El item más costos es: {costoso} ${precios[costoso]: .2f}")
    
if __name__ == "__main__":
    main()
    
    
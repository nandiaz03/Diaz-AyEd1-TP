"""Solicitar al usuario el total de la compra y el dinero recibido"""
total_compra = int(input("Ingrese el total de la compra: "))
dinero_recibido = int(input("Ingrese el dinero recibido: "))
while dinero_recibido < total_compra:
    print("dinero recibido insuficiente")
    dinero_recibido = int(input("Ingrese el dinero recibido: "))

def calcular_cambio(total_compra, dinero_recibido):
    """Calcular el cambio que se debe devolver al cliente y los billetes necesario para devolverlo"""
    cambio = dinero_recibido - total_compra
    print(f"El cambio a devolver es: {cambio}")
    billetes = [5000,1000, 500, 200, 100, 50, 10]
    cantidad_billetes = []
    for i in range(len(billetes)):
        cantidad = cambio // billetes[i]
        cantidad_billetes.append(cantidad)
        cambio = cambio - cantidad * billetes[i]
    if cambio != 0: 
        print("Error no se puede devolver el cambio exacto")
    else:
        print("Cantidad de billetes a devolver:")
        for i in range(len(billetes)):
            if cantidad_billetes[i] > 0:
                print(f"{cantidad_billetes[i]} billetes de {billetes[i]}")
   
calcular_cambio(total_compra, dinero_recibido)
        
       
    
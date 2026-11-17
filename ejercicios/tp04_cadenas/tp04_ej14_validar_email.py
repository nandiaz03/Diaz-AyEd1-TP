def validar_email(direccion: str)->bool:
    """Contrato: Esta funcion recibe la direccion de email y valida si es correcta devolviendo True o False en caso contrario
    precondiciones: direccion debe ser una string
    postcondiciones: Devuelve True si la direccion es valida y False en caso contrario"""
    direccion = direccion.lower()
    if direccion.count("@") != 1:
        return False
    usuario, dominio = direccion.split("@")
    if not usuario.isalnum():
        return False
    if dominio.endswith(".com.ar"):
        nombre_dominio = dominio[:-len(".com.ar")]
    elif dominio.endswith(".com"):
        nombre_dominio = dominio[:-len(".com")]
    else: 
        return False
    return len(nombre_dominio)>=1

def obtener_dominio(direccion: str)->str: 
    """Contrato: 
    precondiciones: direccion es una string con un único caracter @
    postcondiciones: devuelve el dominio de direccion en minusculas"""
    return direccion.lower().split("@")[1]   

def main()->None:
    """contrato: Ejecuta el programa principal 
    precondiciones: ninguna
    postcondiciones: recibe una direccion de correo, la valida imprime los dominios de las los dominios de las direcciones validas, sin repetir y ordenas alfabeticamente"""
    dominios = []
    direccion = input("Ingrese su correo (vacio para salir): ")
    while direccion != "":
        if validar_email(direccion):
            print("Direccion valida")
            dominio = obtener_dominio(direccion)
            if dominio not in dominios:
                dominios.append(dominio)
        else: 
            print("Direccion Inválida")
        direccion = input("Ingrese su direccion de correo (vacio para terminar): ")
    dominios.sort()
    print(f"dominios ingresados: {dominios}")
    
if __name__ == "__main__":
    main()

    
    
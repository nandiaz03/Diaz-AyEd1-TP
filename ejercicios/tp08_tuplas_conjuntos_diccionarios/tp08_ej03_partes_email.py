def partes_email(direccion: str)->tuple:
    """Contrato: Separa una direccion de correo en partes
    precondiciones: direccion debe ser una string 
    postcondiciones: devuelve la tupal (usuario, partes del dominio)"""
    if direccion.count("@") != 1:
        return " "
    usuario, dominio = direccion.split("@")
    partes_dominio = dominio.split(".")
    if usuario == " " or len(partes_dominio) < 2: 
        return ("")
    for parte in partes_dominio:
        if parte == "": 
            return " "
    return (usuario,) + tuple(partes_dominio)

def main()->None:
    """Contrato: Ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: pide una direccion de correo e imprime sus partes o un mensaje de error si es invalida"""
    direccion = input("Ingrese una direccion de corre: ")
    partes = partes_email(direccion)
    if partes == " ": 
        print("Error - La direccion ingresada es invalida")
    else: 
        print(partes)
    
if __name__ == "__main__":
    main()
    
def nombre_mes(mes: int)->str:
    """Contrato: devuelve el nombre del mes que el usuario ingreso
    precondiciones: mes debe ser un numero mayor a 1 
    postcondiciones: devuelve el nombre del mes y en caso de ser menor a 1 devuelve una cadena vacia"""
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    try:
        if mes < 1:
            raise IndexError
        return meses[mes - 1]
    except IndexError:
        return ""
    
def main()->None:
    """Contrato: Ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: el usuario ingresa un numero de mes e imprime su nombre"""
    mes = int(input("Ingrese el número de mes: "))
    nombre = nombre_mes(mes)
    if nombre == "":
        print(f"numero del mes inválido")
    else: 
        print(f"El mes es: {nombre}")

if __name__ == "__main__":
    main()
        
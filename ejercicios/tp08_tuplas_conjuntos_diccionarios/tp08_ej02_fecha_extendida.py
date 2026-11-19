anio_corte = 30

def completar_anio(anio: int):
    """Contrato: pasa a un año de dos digitos a cuatro usando el año de corte
    precondiciones: anio es un entero entre 0 y 99, o mayor o igual a 1000
    postcondiciones: devuelve el año con cuatro digitos"""
    if anio >= 100:
        return anio 
    elif anio <= anio_corte: 
        return 2000 + anio
    else:
        return 1900 + anio

def extencion_fecha(fecha: tuple[int, int, int])->str:
    """contrato: expresa una fecha en formato extendido.
    precondiciones: fecha es una tupla (dia, mes, anio) con mes entre 1 y 12.
    postcondiciones: devuelve un str como "12 de Octubre de 2030"."""
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    dia, mes, anio = fecha
    anio_completo = completar_anio(anio)
    return f"{dia} de {meses[mes - 1]} de {anio_completo}"

def main()->None: 
    """Contrato: Ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: pide una fecha e imprime su formato extendido"""
    try: 
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))
    except ValueError:
        print("Error - Debe ingresar números enteros")
        return
    fecha = (dia, mes, anio)
    print(extencion_fecha(fecha))
    
if __name__ == "__main__":
    main()
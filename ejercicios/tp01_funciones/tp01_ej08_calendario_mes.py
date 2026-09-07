"""Calcular el día de la semana para una fecha dada
    pre condiciones: la fecha ingresada es valida
    post condiciones: devuelve el día de la semana correspondiente a la fecha ingresada"""

def diadelasemana(dia:int, mes:int, anio:int)->int:
    """Calcular el dia de la semana para una fecha dada"""
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
        siglo = anio // 100
        anio2 = anio % 100
        diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def anio_bisiesto(anio:int) -> bool:
    """Determinar si el año ingresado es bisiesto o no"""
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False
    
def limite(dia:int, mes:int, anio:int)->int: 
    """Determinar dia maximo del mes ingresado, teniendo en cuenta los años bisiestos"""
    match mes:
        case 1:
            dia_max = 31
        case 2:
            anio_bisiesto(anio)
            if anio_bisiesto(anio) == True:
                dia_max = 29 
            else:
                dia_max = 28
        case 3:
            dia_max = 31
        case 4:
            dia_max = 30
        case 5:
            dia_max = 31
        case 6:
            dia_max = 30
        case 7:
            dia_max = 31
        case 8:
            dia_max = 31
        case 9:
            dia_max = 30
        case 10:
            dia_max = 31
        case 11:
            dia_max = 30
        case 12:
            dia_max = 31
    return dia_max

def validar_fecha(dia:int, mes:int, anio:int)->tuple[int, int, int]:
    """Validar la fecha ingresada y solicitar nuevamente la fecha si es inválida""" 
    dia_max = limite(dia, mes, anio)
    while mes < 1 or mes > 12 or anio < 1 or dia < 1 or dia > dia_max:
        print("Fecha inválida. Ingrese nuevamente la fecha.")
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el anio: "))
    return dia, mes, anio

def def_dia_semana(dia:int, mes:int, anio:int)->str:
    """Determinar el día de la semana para una fecha dada"""
    dia_semana = diadelasemana(dia, mes, anio)
    match dia_semana:
        case 0:
            semana = "Domingo"
        case 1:
            semana = "Lunes"
        case 2:
            semana = "Martes"
        case 3:
            semana = "Miércoles"
        case 4:
            semana = "Jueves"
        case 5:
            semana = "Viernes"
        case 6:
            semana = "Sábado"
    return semana

def main()-> None:
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el anio: "))
    dia, mes, anio = validar_fecha(dia, mes, anio)
    dia_semana = diadelasemana(dia, mes, anio)
    semana = def_dia_semana(dia, mes, anio)
    print(f"La fecha {dia}/{mes}/{anio} corresponde a un {semana}.")


if __name__ == "__main__":
    main()
    








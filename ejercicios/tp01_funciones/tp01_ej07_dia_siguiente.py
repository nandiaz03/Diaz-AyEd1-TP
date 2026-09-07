"""Solicitar al usuario una fecha y devolver la fecha del día siguiente
    pre condicion: la fecha ingresada debe ser valida
    post condicion: devuelve la fecha del día siguiente a la ingresada y, la cantidad de días que hay entre la fecha ingresada y una fecha ya establecida"""
    
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
        dia = int(input("Ingrese el dia: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el anio: "))
    return dia, mes, anio
   
def diasiguiente(dia:int, mes:int, anio:int)->tuple[int, int, int]: 
    """Calcular el día siguiente a la fecha ingresada"""
    dia_max = limite(dia, mes, anio)
    if dia < dia_max:
        dia += 1
    else:
        dia = 1
        if mes < 12:
            mes += 1
        else:
            mes = 1
            anio += 1
    return dia, mes, anio
    
def dias_entre(dia:int, mes:int, anio:int, hasta_dia:int, hasta_mes:int, hasta_anio:int)->int:
    """Calcular la distancia que hay entre la fecha actual y una fecha ya establecida"""
    contador = 0
    while hasta_dia != dia or hasta_mes != mes or hasta_anio != anio:
        dia, mes, anio = diasiguiente(dia, mes, anio)
        contador += 1
        if hasta_dia == dia and hasta_mes == mes and hasta_anio == anio:
            break
    return contador

def main() -> None: 
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    dia, mes, anio = validar_fecha(dia, mes, anio) 
    hasta_dia = 3
    hasta_mes = 4
    hasta_anio = 2023
    dia_siguiente, mes_siguiente, anio_siguiente = diasiguiente(dia, mes, anio)
    dias = dias_entre(dia, mes, anio, hasta_dia, hasta_mes, hasta_anio)
    print(f"La fecha del día siguiente es: {dia_siguiente}/{mes_siguiente}/{anio_siguiente}")
    print(f"Hay {dias} dias entre {dia}/{mes}/{anio} y {hasta_dia}/{hasta_mes}/{hasta_anio}")

if __name__ == "__main__":
    main()
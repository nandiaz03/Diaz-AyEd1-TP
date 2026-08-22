"""Solicitar al usuario un dia, mes y año  
    pre condicion: verificar las fechas ingresadas sean validas, teniendo en cuenta los años bisiestos
    post condicion: devuelve true si la fecha es valida, false en caso contrario"""

dia = int(input("ingrese un dia: "))
mes = int(input("ingrese un mes: "))
año = int(input("ingrese un año: "))

def año_bisiesto(año):
    """Determinar si el año ingresado es bisiesto o no"""
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else:
        return False


def validar_fecha(dia, mes, año):
    """validar la fecha antes solicitada ydevolver true o false dependiendo si es valida o no"""
    match mes:
        case 1:
            dia_max = 31
        case 2:
            año_bisiesto(año)
            if año_bisiesto(año) == True:
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
    if mes < 1 or mes > 12 or año < 1 or dia < 1 or dia > dia_max:
        print("False")
    else: 
        print("True")

validar_fecha(dia, mes, año)

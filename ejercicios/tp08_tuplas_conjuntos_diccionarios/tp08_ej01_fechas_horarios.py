segundos_xdia = 24*60*60

def es_bisiesto(anio:int)->bool:
    """Contrato: Determina si un año es bisiesto o no
    precondiciones: anio debe ser un entero
    postcondiciones: devuelve True si anio es bisiesto y False en caso contrario"""
    if anio % 4 == 0 and anio % 100 != 0: 
        return True
    elif anio % 4 == 0 and anio % 400 == 0: 
        return True
    else: 
        return False
    
def dias_mes(mes: int, anio: int)->int:
    """contrato: cuenta la cantidad de dias que tiene el mes en el año
    precondiciones: mes debe ser un entero entre 1 y 12. anio tambien debe ser un entero
    postcondiciones: Devuelve la cantidad de dias que tiene el mes en ese año"""
    if mes == 2:
        if es_bisiesto(anio) == True: 
            return 29 
        else:
            return 28
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    else:
        return 31
    
def validar_fecha(dia: int, mes: int, anio: int)->bool:
    """contrato: valida si la fecha es correcta o no
    precondiciones: dia, mes y anio deben ser enteros
    postcondiciones: Devuelve True si dia/mes/anio corresponden a una fecha valida y False en caso contrario"""
    if anio < 1 or mes < 1 or mes > 12:
        return False
    else: 
        return 1 <= dia <= dias_mes(mes,anio)
    
def ingresar_fecha()->tuple[int, int, int]:
    """contrato: solicita al usuario una fecha valida, si no lo es la vuelve a pedir hast que ingrese una fecha valida
    precondiciones: ninguna
    postcondiciones: pide una fecha hasta que sea válida y devuelve la tupla (dia, mes, anio)"""
    while True: 
        try: 
            dia = int(input("Ingrese el día: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))
            if validar_fecha(dia, mes, anio):
                return (dia, mes, anio)
            print("Error - La fecha ingresada no existe")
        except ValueError:
            print("Error - debe ingresar un numero entero")

def sumar_dias(fecha: tuple[int, int, int], num: int)->tuple[int, int, int]:
    """Contrato: suma una cantidad de días a una fecha.
    precondiones: fecha dede ser una tupla con una fecha valida
    postondiciones: devuelve la tupla (dia, mes, anio) que resulta de sumar num días a fecha, pasando de mes y de año cuando corresponde"""
    dia, mes, anio = fecha
    for i in range(num):
        dia += 1 
        if dia > dias_mes(mes, anio):
            dia = 1 
            mes += 1
            if mes > 12: 
                mes = 1
                anio += 1
    return(dia, mes, anio)

def validar_hora(hora: int, minuto:int, segundos: int)->bool:
    """Contrato: valida que la hora sea valida
    precondiciones: hora, minutos y segundos deben ser enteros
    postcondiciones: Devuelve True si hora esta entr 0 y 23, minutos y segundos entre 0 y 59 caso contrario devuelve False"""
    if 0 <= hora <= 23 and 0 <= minuto <= 59 and 0 <= segundos <= 59:
        return True
    return False

def ingresar_horario()->tuple[int, int, int]:
    """Contrato: solicita al usuario un horario por teclado y lo vuelve a pedir hasta que sea correcto.
    precondiciones: ninguna
    postcondicioes: Devuelve la tupla (hora, minuto, segundos) con un  horario valido si se ingres un horario invalido muestra un mensaje de error"""
    while True: 
        try: 
            hora = int(input("Ingrese la hora: "))
            minuto = int(input("Ingrese el minuto: "))
            segundos = int(input("Ingrese los segundos: "))
            if validar_hora(hora, minuto, segundos):
                return (hora, minuto, segundos)
            print("Error - El horario ingresado no es correcto")
        except ValueError:
            print("Error - Debe ingresar números enteros")
    
def pasar_segundos(horario: tuple[int, int, int])->int:
    """contrato: Cuenta los segundos transcurridos en el dia
    precodiciones: horario es una tupla (hora, minuto, segundo) válida.
    Postcondiciones: devuelve la cantidad de segundos transcurridos desde las 00:00:00 hasta horario."""
    hora, minuto, segundos = horario 
    return hora * 3600 + minuto * 60 + segundos

def devolver_segundos(segundos: int)->tuple[int, int, int]:
    """contrato: convierte una cantidad de segundos a horas, minutos y segundos.
    precondiciones: segundo es un entero positivo no mayor a 86400
    postcondiciones: devuelve la tupla (horas, minutos, segundos) equivalente a la cantidad de segundos recibida."""
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    resto = segundos % 60 
    return (horas, minutos, resto)
   
def diferencia_de_horas(horario_1: tuple[int, int, int], horario_2: tuple[int, int, int])->tuple[int, int, int]:
    """contrato: calcula el tiempo que transcurre entre dos horarios
    precondiciones: horario_1 y horario_2 son tuplas (hora, minuto, segundo) válidas.
    postcondionces: Devuelve la tupla(hora, minuto, segundos) con el tiempo que transcurre entre el horario_1 y horario_2"""
    segundos_1 = pasar_segundos(horario_1)
    segundos_2 = pasar_segundos(horario_2)
    if segundos_1 <= segundos_2:
        diferencia = segundos_2 - segundos_1 
    else: 
        diferencia = segundos_2 + segundos_xdia - segundos_1
    return devolver_segundos(diferencia)

def main()->None:
    """Contrato: ejecuta el programa principal 
    precontrato: ninguna
    postcondiciones: Imprime la fecha que resulta de sumarlos e imprime la fecha que resulta de sumarlos. Luego pide dos horarios e imprime la diferencia entre ellos."""
    fecha = ingresar_fecha()
    num = int(input("Ingrese la cantidad de dias a sumar: "))
    dia, mes, anio = sumar_dias(fecha, num)
    print(f"La nueva fecha es: {dia}/{mes}/{anio}")
    horario_1 = ingresar_horario()
    print(f"primer horario: {horario_1}")
    horario_2 = ingresar_horario()
    print(f"segundo horario: {horario_2}")
    horas, minutos, segundos = diferencia_de_horas(horario_1, horario_2)
    print(f"La diferencia es de {horas} horas, {minutos} minutos y {segundos} segundos")
    
if __name__ == "__main__":
    main()

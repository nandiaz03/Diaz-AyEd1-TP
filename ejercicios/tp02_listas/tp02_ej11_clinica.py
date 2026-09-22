"""Contrato: el usuario debe cargar los datos de los pacientes atendidos y separarlos en urgentes y con turno
precondiciones: el numero de afiliado debe ser un numero entero de 4 digitos  
postcondiciones: """

def cargar_paciente()->list[int]: 
    lista_urgencia = []
    lista_turno = []
    num_afiliado = int(input("Ingrese el numero de afiliado (-1 para salir): "))
    while num_afiliado != -1:
        while (num_afiliado < 1_000 or num_afiliado > 9_999) and num_afiliado != -1: 
            print("Numero ingresado invalido")
            num_afiliado = int(input("Ingrese el numero de afiliado: "))
        if num_afiliado == -1: 
            break
        print("Ingrese 0 para urgencia y 1 si tiene turno")
        tipo = int(input("ingrese la opcion: "))
        while tipo != 0 and tipo != 1:
            print("opcion incorrecta")
            tipo = int(input("ingrese la opcion: "))
        if tipo == 0:
            lista_urgencia.append(num_afiliado)
        else: 
            lista_turno.append(num_afiliado)
        num_afiliado = int(input("Ingrese el numero de afiliado (-1 para salir): "))
    return lista_urgencia, lista_turno

def opcion_b(lista_urgencia: list[int], lista_turno: list[int])-> int: 
    buscar_num = int(input("Inrese numero de afiliado a buscar (ingrese -1 para salir): "))
    while buscar_num != buscar_num:    
        while (num_afiliado < 1_000 or num_afiliado > 9_999) and buscar_num != -1: 
                num_afiliado = int(input("Ingrese el numero de afiliado: "))
        if buscar_num == -1:
            break
    veces_urgencia = lista_urgencia.count(buscar_num)
    veces_turno = lista_turno.count(buscar_num)
    return veces_urgencia, veces_turno

def mostrar_opciones()->None:
    print("a. Ver listado de pacientes atendidos por urgencia y un listado de pacientes atendidos por turno")
    print("b. Ver cuantas veces un afiliado fue atendido por urgencia y turno")
    print("-1. Para salir")
def main()->None:
    lista_urgencia, lista_turno = cargar_paciente()
    opcion = ""
    mostrar_opciones()
    while opcion != "-1": 
        opcion = input("ingrese la opcion: ")
        if opcion == "a":
            print(lista_urgencia)
            print(lista_turno)
        elif opcion == "b":
            veces_urgencia, veces_turno = opcion_b(lista_urgencia, lista_turno)
            print(f"el filiado fue atendido {veces_urgencia} de urgencia y {veces_turno} con turno")
        else:
            print("opcion incorrecta")
        
if __name__ == "__main__":
    main()
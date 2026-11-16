def grabar_rango_alturas():
    try:
         with open("ejercicios/tp06_archivos/alturas.txt", "a", encoding = "utf-8") as archivo:
            deporte = input("Ingrese el deporte: ")
            archivo.write(f"{deporte} \n")
            altura = -1
            while altura != 0:
                altura= float(input("Ingrese la altura (0 para salir): "))
                if altura == 0:
                    break
                else:
                    archivo.write(f"{altura} \n")
    except FileNotFoundError:
        print("No se encontro el archivo")
    except OSError:
        print("No se pudo grabar el archivo")
    except:
        print("Error en los datos")
    else: 
        print("se guardo correctamente")
        
def grabar_promedio():
    pass
    

def mostrar_mas_altos():
    pass

grabar_rango_alturas()
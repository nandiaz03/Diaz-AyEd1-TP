separador = ","

try: 
    with open("ejercicios/tp06_archivos/PERSONAS.txt", "rt", encoding = "utf-8") as archivo:
        with open("ejercicios/tp06_archivos/ARMENIA.txt", "w", encoding = "utf-8") as archivo_armenia:
            with open("ejercicios/tp06_archivos/ITALIA.txt", "w", encoding = "utf-8") as archivo_italia:
                with open("ejercicios/tp06_archivos/ESPAÑA.txt", "w", encoding = "utf-8") as archivo_espana:
                    for linea in archivo:   
                        apellido, nombre = linea.strip().split(separador)
                        if apellido[-3:] == "ian":
                            archivo_armenia.write(apellido + separador + nombre + "\n")
                        elif apellido[-3:] == "ini":
                            archivo_italia.write(apellido + separador + nombre + "\n")
                        elif apellido[-2:] == "ez":
                            archivo_espana.write(apellido + separador + nombre + "\n")
                        else: 
                            pass
except FileNotFoundError:
    print("No se encontro el archivo")
except OSError:
    print("Error al abrir el archivo")
except: 
    print("Error en los datos")
else: 
    print("Archivo creado correctamente")

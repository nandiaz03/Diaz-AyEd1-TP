def limpiar_palabra(palabra: str)->str:
    """Contrato: quita los signos de puntuacion de una palabra y la pasa a minusculas
    precondiciones: palabra es una string
    postcondiciones: devuelve una string con caracteres alfanumericos de palabra en minusculas"""
    limpia = ""
    for caracter in palabra.lower():
        if caracter.isalnum():
            limpia += caracter
    return limpia

def palabras_sin_repetir(oracion: str)->str: 
    """Contrato: quita los signos de puntuación de una palabra y la pasa a minúsculas
    precondiciones: palabra es un str
    postcondiciones: devuelve un str con los caracteres alfanuméricos de palabra en minúsculas """
    conjunto = set()
    for palabra in oracion.split():
        limpia = limpiar_palabra(palabra)
        if limpia != "":
            conjunto.add(limpia)
    alfabetica = sorted(conjunto)
    return sorted(alfabetica, key = len)

def main()->None:
    """contrato: ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: pide una oracion e imprime sus palabra sin repetir, ordenadas por longitud"""
    oracion = input("Ingrese una oracion: ")
    palabras = palabras_sin_repetir(oracion) 
    print(" ".join(palabras))
    
if __name__ == "__main__":
    main()
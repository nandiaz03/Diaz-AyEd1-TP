def contar_vocales(palabra: str)->dict: 
    """Contrato: cuenta cuantas veces aparece cada vocal en una palabra
    precondiciones: palabra debe ser una string
    postcondiciones: devuelve un diccionario con cada vocal que aparece y su cantidad"""
    vocales = {}
    for letra in palabra.lower():
        if letra in "aeiou":
            if letra in vocales:
                vocales[letra] += 1
            else: 
                vocales[letra] = 1
    return vocales

def main()->None:
    """Contrato: Contrato: ejecuta el programa principal
    precondiciones: ninguna
    postcondiciones: lee una frase e imprime cada palabra con su cantidad de vocales"""
    oracion = input("Ingrese una oracion: ")
    for palabra in oracion.split():
        vocales = contar_vocales(palabra)
        total = 0
        for vocal in vocales:
            total += vocales[vocal]
        print(f"{palabra}: {total} vocales {vocales}")

if __name__ == "__main__":
    main()    
    
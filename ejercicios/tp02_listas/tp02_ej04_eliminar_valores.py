"""Contrato: Recibir una lista y un valor entero y eliminar el valor de la lista si se encuentra en ella
precondiciones: Recibir una lista de numeros enteros y un valor entero
postcondiciones: Eliminar todas las ocurrencias del valor en la lista y devolver la lista actualizada"""

def cargar_lista() -> list[int]:
    """armar una lista con numeros ingresados por el usuario"""
    lista = []
    numero = int(input("Ingrese un numero entero (ingrese -1 para finalizar): "))
    while numero != -1:
        lista.append(numero)
        numero = int(input("Ingrese un numero entero (ingrese -1 para finalizar): "))
    return lista

def eliminar_valores(lista:list[int],valores_a_eliminar:list[int])->list:
    for i in range(len(valores_a_eliminar)):
        valor = valores_a_eliminar[i]
        if valor in lista:
            lista.remove(valor)
    return lista

def main()-> None:
    print("Carga la lista")
    lista = cargar_lista()
    print("Carga los valores a eliminar")
    valores_a_eliminar = cargar_lista()
    lista_resultante = eliminar_valores
    print(f"lista original: {lista}")
    print(f"valores a eliminar: {valores_a_eliminar}")
    print(f"lista resultante {lista}")

if __name__ == "__main__":
    main()



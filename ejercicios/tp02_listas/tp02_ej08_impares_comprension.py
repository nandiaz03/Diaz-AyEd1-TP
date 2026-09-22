"""contrato: mostrar una lista de numeros impares ente 100 y 200 
precondiciones: 
postcondiciones: mostrar una lista con numeros impares"""

lista = [valor for valor in range(100,201) if valor % 2 != 0]
print(lista)
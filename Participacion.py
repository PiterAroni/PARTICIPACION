#Elaborar el código de la multiplicación de una matriz bidimensional, 
#utilizar funciones para realizar la operación multiplicación. Asimismo, 
#el resultado ordenar de manera descendente. Finalmente, realizar una función de búsqueda 
#para revisar si la matriz resultado tiene el valor 9, en caso fuese afirmativo, 
#indicar por pantalla " La matriz tiene el valor 9 y se encuentra en la posición i (fila) y 
#j (columna).
def row_multiplication(matrix):
    results = []
    mult = 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            mult *= matrix[i][j]
        results.append(mult)
        mult = 1
    return results

def search_matrix(matrix):
    encontrado = False
    row = 0
    column = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 9:
                row = 1
                column = j
                encontrado = True
    if encontrado:
        print("el numero 9 fue encontrado y esta en la posicion", row, " ",column)
    else:
        print("El numero 9 no fue encontrado")
#Metodo Burbuja
def sort_results(results):
    aux = 0
    for i in results:
        for j in range(len(results)-1):
            if results[j] < results[j+1]:
                aux = results[j]
                results[j] = results[j+1]
                results[j+1] = aux
    return results

columnas = 3
filas = 4

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12],
]
print("matriz: ")
print(matriz)

results = row_multiplication(matriz)
sort_results(results)
print("multiplicacion ordenada: ")
print(results)

search_matrix(matriz)
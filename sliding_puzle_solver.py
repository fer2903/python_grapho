# Implementar un solucionador de puzlez
# escribe una funcion que produzca una secuenciade pequeños movimientos que resuelvan el puzzle

# entrada sera n x n array/list de valores enteros en un rango empezando por 0 y terminando en n**2 -1
# si el puzle no se puede resolver retorna None
# el rango de valores para n sera de 10>=n >=3
def find_zero(matrix):
    # Encuentra las coordenadas del número 0 en la matriz
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                return i, j

def slide_puzzle(matrix):
    result = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        result.append([num for num in matrix[i]])

    i, j = find_zero(matrix)

    for k in range(cols - 1):
        if j < cols - 1:
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            j += 1
            result.append([num for num in matrix[i]])

    for k in range(rows - 1):
        if i < rows - 1:
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
            i += 1
            result.append([num for num in matrix[i]])

    return result

simple_example = [
    [1, 2, 3, 4],
    [5, 0, 6, 8],
    [9, 10, 7, 11],
    [13, 14, 15, 12]
]

result = slide_puzzle(simple_example)

for row in result:
    print(row)





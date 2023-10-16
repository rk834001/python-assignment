def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0]

    if cols1 != rows2:
        return None  # Matrices cannot be multiplied

    result = []

    for i in range(rows1):
        row = []
        for j in range(cols2):
            product = 0
            for k in range(cols1):
                product += matrix1[i][k] * matrix2[k][j]
            row.append(product)
        result.append(row)

    return result

# Input matrices
matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [5, 6],
    [7, 8]
]

# Perform matrix multiplication
result = matrix_multiplication(matrix1, matrix2)

if result is not None:
    for row in result:
        print(row)
else:
    print("Matrices cannot be multiplied due to incompatible dimensions.")

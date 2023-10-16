def matrix_addition(matrix1, matrix2):
    # Check if the dimensions of the matrices are the same
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None  # Matrices cannot be added

    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0]):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

# Input matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Perform matrix addition
result = matrix_addition(matrix1, matrix2)

if result is not None:
    for row in result:
        print(row)
else:
    print("Matrices cannot be added due to different dimensions.")

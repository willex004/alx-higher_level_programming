#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nMatrix = matrix.copy()
    for a in range(len(matrix)):
        nMatrix[a] = list(map(lambda b: b**2, matrix[a]))
        return (nMatrix)

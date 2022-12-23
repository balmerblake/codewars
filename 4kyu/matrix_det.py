# Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.
import numpy as np
def determinant(matrix):
    if len(matrix[0]) == 1 and len(matrix) == 1:
        dt = matrix[0][0]
        return dt
    else:
        dt = (np.linalg.det(matrix))
        dt_ceil = np.ceil(dt)
        dt_floor = np.floor(dt)
        if np.abs(dt_ceil - dt) < np.abs(dt_floor - dt):
            return int(dt_ceil)
        else:
            return int(dt_floor)
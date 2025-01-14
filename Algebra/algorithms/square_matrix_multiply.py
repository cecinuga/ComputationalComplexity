import numpy as np

def square_matrix_multiply(A, B):
    C = np.zeros((len(A), len(A)))

    for i in range(len(A)):
        for j in range(len(A)):
            C[i][j] = 0
            for k in range(len(A)):
                C[i][j] += A[i][k] * B[k][j] 

    return C
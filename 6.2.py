import numpy as np
import matplotlib.pyplot as plt

M1 = np.array([[6, 5, 3], [3, 5, 4], [2, 1 ,3]])
M2 = np.array([[3, 4, 2], [4, 5, 4], [1, 2, 5]])
M3 = 4
M4 = np.array([[1, 4, 2], [6, 4, 2]])
M5 = -2

def mat_operations(matrix1, matrix2):
    if np.isscalar(matrix1) == True and np.isscalar(matrix2) == True:
        print("\n",matrix1, 'Is a scalar')
        print(matrix2, 'Is a scalar'"\n")
        print("-" * 42)
        print("-" * 42)

    elif np.isscalar(matrix1) == True:
        print(matrix1,'Is a scalar'"\n")
        print("-" * 42)
        print("-" * 42)
        if matrix2.size > 0:
            is_square = True if matrix2.shape[0] == matrix2.shape[1] else False
            print(f'Matrix:\n{matrix2}\n'
                  f'\nShape:\t{matrix2.shape}'
                  f'\nSize: \t{matrix2.size}'
                  f'\nRank:\t{matrix2.ndim}'
                  f'\nSquare: {is_square}\n',
                  f'-' * 42)
        else:
            print("This Matrix is Invalid")

    elif np.isscalar(matrix2)==True:
        print(matrix2,"Is a scalar""\n")
        print("-" * 42)
        print("-" * 42)
        if matrix1.size > 0:
            is_square = True if matrix1.shape[0] == matrix1.shape[1] else False
            print(f'Matrix:\n{matrix1}\n'
                  f'\nShape:\t{matrix1.shape}'
                  f'\nSize: \t{matrix1.size}'
                  f'\nRank:\t{matrix1.ndim}'
                  f'\nSquare: {is_square}\n',
                  f'-' * 42)
        else:
            print("This Matrix is Invalid")

    elif np.isscalar(matrix1) == False and np.isscalar(matrix2) == False:
        if matrix1.size > 0 and matrix2.size > 0:
            is_square = True if matrix1.shape[0] == matrix1.shape[1] else False
            print(f'Matrix:\n{matrix1}\n'
                  f'\nShape:\t{matrix1.shape}'
                  f'\nSize: \t{matrix1.size}'
                  f'\nRank:\t{matrix1.ndim}'
                  f'\nSquare: {is_square}\n',
                  f'-' * 42)
            is_square = True if matrix2.shape[0] == matrix2.shape[1] else False
            print(f'Matrix:\n{matrix2}\n'
                  f'\nShape:\t{matrix2.shape}'
                  f'\nSize: \t{matrix2.size}'
                  f'\nRank:\t{matrix2.ndim}'
                  f'\nSquare: {is_square}\n',
                  f'-' * 42)
        else:
            print("This Matrix is Invalid")

    if np.isscalar(matrix1)==True:
        addition = matrix1 + matrix2
        substraction = matrix1 - matrix2
        multiplication = matrix1 * matrix2
        division = matrix1 // matrix2
        print(addition)
        print(substraction)
        print(multiplication)
        print(division)

    elif np.isscalar(matrix2) == True:
        addition = matrix1 + matrix2
        substraction = matrix1 - matrix2
        multiplication = matrix1 * matrix2
        division = matrix1 // matrix2
        print(addition)
        print(substraction)
        print(multiplication)
        print(division)

    elif matrix1.size == matrix2.size :
        addition = matrix1 + matrix2
        substraction = matrix1 - matrix2
        multiplication = matrix1 * matrix2
        division = matrix1 // matrix2
        print(addition)
        print(substraction)
        print(multiplication)
        print(division)

    else:
            print("ERROR MATRIX SIZE""\n")
            print("-" * 42)
            print("-" * 42)

mat_operations(M1, M2)
mat_operations(M1, M3)
mat_operations(M1, M4)
mat_operations(M3, M5)

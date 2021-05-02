import numpy as np
import matplotlib.pyplot as plt

M1 = np.array([[8, 8, 8], [6, 5, 5], [6, 6, 6]])
M2 = np.array([[9, 9, 8], [6, 5, 5], [7, 5, 5]])
M3 = np.identity(5)
M4 = np.ones([4, 5])
M5 = np.zeros([5, 4])

def describe_mat(matrix):
       is_square = True if matrix.shape[0] == matrix.shape[1] else False
       print(f'Matrix:\n{matrix}\nShape:\t{matrix.shape}\nSize:\t{matrix.size}\nRank:\t{matrix.ndim}'
             f'\nIs Square: {is_square}')

       result = sum(matrix)
       results = sum(result)
       cross = np.diagonal(matrix)
       output = 1
       for xy in cross:
           output = output * xy

       if results == 0:
           print("This Matrix is an Zero Matrix","\n")

       elif results == matrix.size:
           print("This Matrix is an Ones Matrix","\n")

       elif output == 1:
           print("This Matrix is an Identity Matrix","\n")

       else:
           print("This Matrix is Invalid","\n")

describe_mat(M1)
describe_mat(M2)
describe_mat(M3)
describe_mat(M4)
describe_mat(M5)

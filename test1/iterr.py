import functions as af
import input_output as io
import method as mt
import numpy as np
A = io.Input_matrix()
b = io.Input_matrix()
af.swap_SLAR(A, b)
def change (A):
    B = A - np.eye(len(A))
    return(B)

print(change(A))
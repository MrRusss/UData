import copy
import input_output as io

def changing_lines(A, b, i):
    # '''Find max element in the column
    # and change row '''

    max = A[i][i]
    index = i
    for m in range(i + 1, len(A)):
        if abs(A[m][i]) > abs(max):
            max = A[m][i]
            index = m
    if max == 0:
        return -i
    temp = b[index][0]
    b[index][0] = b[i][0]
    b[i][0] = temp
    for j in range(len(A[0])):
        temp = A[index][j]
        A[index][j] = A[i][j]
        A[i][j] = temp
    return i

def Gauss(A, a):
    # '''Just solve system
    #  and return number of iterations'''

    B = copy.deepcopy(A)
    b = copy.deepcopy(a)
    for i in range(len(B) - 1):
        i = changing_lines(B, b, i)
        io.print_matrix(B, str(i) + " iteration:")
        io.print_matrix(b, "b: ")
        if i < 0:
            return i
        for k in range(i + 1, len(B)):
            temp = B[k][i] / B[i][i]
            b[k][0] -= temp * b[i][0]
            for j in range(i, len(B[0])):
                B[k][j] -= temp * B[i][j]
        io.print_matrix(B, str(i) + " iteration:")
        io.print_matrix(b, "b: ")
    if B[-1][-1] == 0:
        return (len(B) - 1)
    x = [[0] * 1 for i in range(len(B[0]))]
    x[-1][0] = b[-1][0] / B[-1][-1]
    for i in range(len(B) - 2, -1, -1):
        sum = 0
        for j in range(i + 1, len(B[0])):
            sum += B[i][j] * x[j][0]
        x[i][0] = 1 / B[i][i] * (b[i][0] - sum)
    return x
import copy

def Factorization(A):
    # ''' Just do factorization and check not to div 0 u[i][i]'''

    if len(A) != len(A[0]):
        return (False, False)
    U = copy.deepcopy(A)
    L = [[0] * len(U[0]) for i in range(len(U))]
    for i in range(len(U)):
        if U[i][i] == 0:
            return (False, False)
        L[i][i] = 1
        for k in range(i + 1, len(U)):
            L[k][i] = U[k][i] / U[i][i]
            for j in range(i, len(U[0])):
                U[k][j] -= L[k][i] * U[i][j]
    return (L, U)

def Inversed_matrix(L, U):
   # find inverse matrix

    A = [[0]* len(U) for i in range(len(U))]
    for k in range(len(U)):
        e = [1 if j == k else 0 for j in range(len(U))]
        y = []
        y.append([])
        y[0].append(e[0])
        for i in range(1, len(U)):
            sum = 0
            for j in range(i):
                sum += L[i][j] * y[j][0]
            y.append([])
            y[i].append(e[i] - sum)
        e[-1] = y[-1][0] / U[-1][-1]
        for i in range(len(U) - 2, -1, -1):
            sum = 0
            for j in range(i + 1, len(U)):
                sum += e[j] * U[i][j]
            e[i] = 1 / U[i][i] * (y[i][0] - sum)
        for i in range(len(U)):
            A[i][k] = e[i]
    return A

def matrix_norm(A):
    # '''find the octahedral norm.'''

    max = 0
    for j in range(len(A[0])):
        sum = 0
        for i in range(len(A)):
            sum += abs(A[i][j])
        if sum > max:
            max = sum
    return max
def swap_SLAR(A, a):
    # '''Takes two matrix as argument.
    # Just check correct accordingly matix '''

    m = len(A[0])
    for i in range(1, len(A)):
        if len(A[i]) != m:
            print("Invalid matrix")
            quit(-1)
    if len(a) != len(A):
        print("Invalid vector")
        quit(-1)

def multiplying(A, B):

    if(len(A[0]) != len(B)):
        return False
    tmp = []
    for i in range(len(A)):
        tmp.append([])
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A[0])):
                sum = sum + A[i][k] * B[k][j]
            tmp[i].append(sum)
    return tmp

def subtraction(A, B):
    '''Takes two matrix as argument and returns their
    subtraction if can do it. Else returns False'''

    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if len(A[i]) != len(B[i]):
            return False
    tmp = []
    for i in range(len(A)):
        tmp.append([])
        for j in range(len(A[0])):
            tmp[i].append(A[i][j] - B[i][j])
    return tmp
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
def addition(A, B):
    '''Takes two matrix as argument and returns their
        addition if can do it. Else returns False'''

    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if len(A[i]) != len(B[i]):
            return False
    tmp = []
    for i in range(len(A)):
        tmp.append([])
        for j in range(len(A[0])):
            tmp[i].append(A[i][j] + B[i][j])
    return tmp

def epsilon(x, y):
    '''Takes two vectors as argument.
    Returns their cubic norm.'''

    max = 0
    for i in range(len(x)):
        if abs(x[i][0] - y[i][0]) > max:
            max = abs(x[i][0] - y[i][0])
    return max
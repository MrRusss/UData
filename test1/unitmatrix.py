import copy
def input_matrix(n,m):
    A=[]
    for i in range(n):
        A.append([])
        for j in range(m):
            A[i].append(int(input()))
    return A

def multiplying(A,B):
    if len(A[0])!= len(B):
        print ('wrong dimension')
        quit(228)
    C=[]
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            C[i].append([])
            sum = 0
            for k in range(len(A[0])):
                sum+=A[i][k]*B[k][j]
            C[i][j] = sum
    return C
A = input_matrix(2, 3)
B = input_matrix(3, 1)
C = multiplying(A, B)
D = copy.deepcopy(C)
print(A)
print(B)
print(C)
print(D)
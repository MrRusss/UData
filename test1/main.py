n = int(input('number row'))
k = int(input('number column'))
a = []
b = []
for i in range(n):
    a.append([])
    for j in range(k):
        a[i].append(input())
for r in a:
    print(a)
for i in range(k):
    b.append([])
    for j in range(n):
        b[i].append(int(input()))
for r in b:
    print(b)
s=[]
def mulplus(i,j):
    for i in range(n):
        for j in range(k):
            sum=0
            for g in range()
            mulplus += a[i][j]*b[j][i]
    return mulplus

def mul():
    mul = 1
    for i in range(k):
        for j in range(1,n):
            mul = mulplus(i,j)

s = mulplus(n,k)
import random
n = int(input('number'))
m = []
for i in range(n):
    m.append([])
    for j in range(n):
        m[i].append(random.randint(1,10))
for r in m:
    print(m)
def gauss(n):
    for i in range(n):

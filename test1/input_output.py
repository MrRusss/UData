def print_matrix(A, text):
    # output matrix with the text

    print(text)
    for i in range(len(A)):
        for j in range(len(A[i])):
            print('{:>6}'.format(round(A[i][j], 3)), end = ' ')
        print()

def Input_matrix():
    # Input matix

    print("Input amount of lines: ")
    try:
        n = int(input())
    except(Exception):
        print('Invalid dimension')
        quit(1)
    if(n <= 0):
        print('Invalid dimension')
        quit(1)
    print('Input values: ')
    try:
        A = [[float(j) for j in input().split()] for i in range(n)]
    except(Exception):
        print('Invalid value')
        quit(1)
    return A







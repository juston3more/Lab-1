RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
X = 10
Y = 10
A = [ [0]*X for i in range(Y) ]
B = [ [0]*X for i in range(Y) ]
def Switzerland():
    for i in range(10):
        if i < 2 or i > 7:
            print(f'{RED}{" " * (35)}{END}')
        if (i > 1 and i < 4) or (i > 5 and i < 8): 
            print(f'{RED}{" " * (14)}{WHITE}{" " * (7)}{RED}{" " * (14)}{END}')
        if i > 3 and i < 6: 
            print(f'{RED}{" " * (7)}{WHITE}{" " * (21)}{RED}{" " * (7)}{END}')
def circles():
    for i in range(7):
        if i == 0 or i == 6:
            print(f'{" " * 6}{WHITE}{" " * 9}{END}{" " * 6 }'*2)
        elif i ==1 or i == 5:
            print(f'{" " * 3}{WHITE}{" " * 3}{END}{" " * 9}{WHITE}{" " * 3}{END}{" " * 3}'*2)
        else:
            print(f'{WHITE}{" " * 3}{END}{" " * 15}{WHITE}{" " * 3}{END}'*2)
def func():
    for i in range(len(A)):
        for j in range(len(A[i])):
            if 3*i <= j:
                A[i][j] = f'{RED}{" " * (2)}{END}'
            else:
                A[i][j] = f'{WHITE}{" " * (2)}{END}'

    for i in range(len(A)-1):
        for j in range(len(A[i])):
            if A[i][j] == f'{RED}{" " * (2)}{END}' and A[i+1][j] == f'{RED}{" " * (2)}{END}':
                A[i][j] = A[i][j] = f'{WHITE}{" " * (2)}{END}'

    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] = A[-i-1][j]
        
    for row in B:
        for elem in row:
            print(elem, end = '')
        print()
def percents():
    with open('sequence.txt', 'r') as f:
        k3=0
        k = 0
        for e in f:
            if abs(float(e[:-1]))<=3:
                k3+=1
            else:
                k+=1
        print(k3*100/(k3+k),'%'+' from -3 to 3', " ", k*100/(k3+k), '%' + ' of the rest')

print('press 1 to see flag')
print('press 2 to see circles')
print('press 3 to see func')
print('press 4 to see percents')
a=int(input())

if a == 1:
    Switzerland()
if a == 2:
    circles()
if a == 3:
    func()
if a == 4:
    percents()

# Matrix Addition
A = []
B = []
C = []
rows = int(input('Enter number of rows: '))
cols = int(input('Enter number of columns: '))

print('MATRIX A')
for i in range(rows):
    row=[]
    for j in range(cols):
        value = int(input(f'Enter input of A[{i}][{j}] :'))
        row.append(value)
    A.append(row)

print('\nMATRIX B' )
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f'Enter input of B[{i}][{j}] :'))
        row.append(value)
    B.append(row)

print ('\nMATRIX A')
for i in range(rows):
    print(A[i])

print ('\nMATRIX B')
for i in range(rows):
    print(B[i])



print('\nSUM of A & B :')
for i in range (rows):
   row = []
   for j in range (cols):
        sum = A[i][j] + B[i][j]
        row.append(sum)
   C.append(row)

for i in range(rows):
    print(C[i])

